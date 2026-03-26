import xtrack as xt
import numpy as np

# TODO:
# linear model of the edge

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

lhc.b1.twiss4d().rows['ip.*'].cols['betx bety x y px py']
lhc.b2.twiss4d().rows['ip.*'].cols['betx bety x y px py']

ip_name = 'ip5'
d1_name = 'mbxf.4r5/b1'
d2_name = 'mbrd.4r5.b1'
k0_d1_var_name = 'kd1.r5'
k0_d2_var_name = 'kd2.r5'
angle_d1_var_name = 'ad1.r5'
angle_d2_var_name = 'ad2.r5'
sep_d2_r5 = 0.188
orientation = 1 # 1 if b1 is going from inside to outside, -1 otherwise

line = lhc.b1
tt = line.get_table()

lhc[d1_name].rbend_model = 'straight-body'
lhc[d2_name].rbend_model = 'straight-body'

original_d1_k0_expr = lhc.ref[d1_name].k0._expr
original_d2_k0_expr = lhc.ref[d2_name].k0._expr
original_d1_angle_expr = lhc.ref[d1_name].angle._expr
original_d2_angle_expr = lhc.ref[d2_name].angle._expr

assert original_d1_k0_expr is not None
assert original_d2_k0_expr is not None
assert original_d1_angle_expr is not None
assert original_d2_angle_expr is not None


lhc[d1_name].angle = 0
lhc[d2_name].angle = 0
lhc[d1_name].k0 = -orientation * lhc.ref[k0_d1_var_name]
lhc[d2_name].k0 = orientation * lhc.ref[k0_d2_var_name]

opt = line.match(
    solve=False,
    start=ip_name,
    end=d2_name,
    betx=1, bety=1,
    vary=[xt.VaryList([k0_d1_var_name, k0_d2_var_name], step=1e-5)],
    targets=xt.TargetSet(x=orientation * lhc['sep_arc'] / 2, px=0.0, at=xt.END),
)
opt.solve()

tw0 = line.twiss(betx=1, bety=1, init_at=ip_name,
                 start=ip_name, end=tt.rows[d2_name + '>>10'].name[-1])

# Set fdown angles to match the trajectory (used only for linear edges)
for nn in [d1_name, d2_name]:
    line[nn].edge_entry_model = 'linear'
    line[nn].edge_exit_model = 'linear'
    line[nn].edge_entry_angle_fdown = np.arcsin(tw0['px', nn])
    line[nn].edge_exit_angle_fdown = -np.arcsin(tw0['px', nn + '>>1'])
    line[nn].rbend_compensate_sagitta = False
    line[nn].rbend_model = 'straight-body'

d1_angle_in = np.arcsin(tw0['px', d1_name])
d2_angle_in  = np.arcsin(tw0['px', d2_name])
d1_angle_out = -d2_angle_in
d2_angle_out  = -np.arcsin(tw0['px', '_end_point'])

line[d1_name].angle = d1_angle_in + d1_angle_out
line[d2_name].angle  = d2_angle_in  + d2_angle_out

line[d1_name].rbend_angle_diff = d1_angle_out - d1_angle_in
line[d2_name].rbend_angle_diff  = d2_angle_out  - d2_angle_in

# Set rbend shifts
line[d1_name].rbend_shift = line[d1_name]._x0_in - tw0['x', d1_name]
line[d2_name].rbend_shift = line[d2_name]._x0_out - tw0['x', '_end_point'] + sep_d2_r5 / 2

# Adapt elements
lhc['ad1.r5'] = -orientation * line[d1_name].angle
lhc['ad2.r5'] = orientation * line[d2_name].angle
lhc['sep_mid_d1.r5'] = 2 * line[d1_name].rbend_shift
lhc['shift_d2.r5'] = line[d2_name].rbend_shift

lhc['mbxf.4r5/b1'].rbend_model = 'straight-body'
lhc['mbxf.4r5/b1'].rbend_compensate_sagitta = False
lhc['mbxf.4r5/b1'].angle = -lhc.ref['ad1.r5']
lhc['mbxf.4r5/b1'].rbend_angle_diff = -lhc.ref['ad1.r5']
lhc['mbxf.4r5/b1'].k0 = -lhc.ref['kd1.r5']
lhc['mbxf.4r5/b1'].rbend_shift = lhc.ref['sep_mid_d1.r5'] / 2
lhc['mbxf.4r5/b1'].edge_entry_angle_fdown = 0
lhc['mbxf.4r5/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r5']
lhc['mbxf.4r5/b1'].edge_entry_model = 'linear'
lhc['mbxf.4r5/b1'].edge_exit_model = 'linear'

lhc['mbrd.4r5.b1'].rbend_model = 'straight-body'
lhc['mbrd.4r5.b1'].rbend_compensate_sagitta = False
lhc['mbrd.4r5.b1'].angle = lhc.ref['ad2.r5']
lhc['mbrd.4r5.b1'].rbend_angle_diff = -lhc.ref['ad2.r5']
lhc['mbrd.4r5.b1'].k0 = lhc.ref['kd2.r5']
lhc['mbrd.4r5.b1'].rbend_shift = lhc.ref['shift_d2.r5']
lhc['mbrd.4r5.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r5']
lhc['mbrd.4r5.b1'].edge_exit_angle_fdown = 0
lhc['mbrd.4r5.b1'].edge_entry_model = 'linear'
lhc['mbrd.4r5.b1'].edge_exit_model = 'linear'


line.slice_thick_elements(
        slicing_strategies=[
            # Slicing with thin elements
            xt.Strategy(slicing=None),
            xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbx.*'),
            xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbrd.*'),

    ])

sv = line.survey(element0=ip_name)


import matplotlib.pyplot as plt
plt.close('all')
plt.figure(1)
plt.plot(sv.Z, sv.X, label='X')
plt.xlim(-180, 180)
plt.ylim(-0.15, 0.15)
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.legend()

# k0_d1_name 
