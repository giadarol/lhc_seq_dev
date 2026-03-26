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
    line[nn].edge_entry_angle_fdown = 0
    line[nn].edge_exit_angle_fdown = 0

# # Introduce magnet curvatures
# for nn, vv_ang in [d1_name, d2_name]:
#     line[nn].k0 = 0
#     line[nn].k0_from_h = True
#     line[nn].rbend_compensate_sagitta = False
#     line[nn].rbend_model = 'straight-body'



d1_angle_in = np.arcsin(tw0['px', d1_name])
d2_angle_in  = np.arcsin(tw0['px', d2_name])
d1_angle_out = -d2_angle_in
d2_angle_out  = -np.arcsin(tw0['px', '_end_point'])

line[d1_name].angle = d1_angle_in + d1_angle_out
line[d2_name].angle  = d2_angle_in  + d2_angle_out

line[d1_name].rbend_angle_diff = d1_angle_out - d1_angle_in
line[d2_name].rbend_angle_diff  = d2_angle_out  - d2_angle_in

# Set rbend shifts
line[d1_name].rbend_shift += line[d1_name]._x0_in - tw0['y', d1_name]
line[d2_name].rbend_shift += line[d2_name]._x0_out - tw0['y', '_end_point']

# Restore expressions on angles
lhc[angle_d1_var_name] = -orientation * line[d1_name].angle
lhc[angle_d2_var_name] = orientation * line[d2_name].angle
lhc[d1_name].angle = -lhc.ref[angle_d1_var_name]
lhc[d2_name].angle = lhc.ref[angle_d2_var_name]

sv = line.survey(element0=ip_name)



# k0_d1_name 
