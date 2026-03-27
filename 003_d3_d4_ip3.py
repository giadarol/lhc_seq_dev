import xtrack as xt
import numpy as np

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

tw1 = lhc.b1.twiss4d()
tw2 = lhc.b2.twiss4d()

lhc['sep_d34.lr3'] = 0.190 # To be checked!!!!!

lhc['mbw.a6r3.b1'].angle = 0
lhc['mbw.b6r3.b1'].angle = 0
lhc['mbw.c6r3.b1'].angle = 0
lhc['mbw.d6r3.b1'].angle = 0
lhc['mbw.e6r3.b1'].angle = 0
lhc['mbw.f6r3.b1'].angle = 0

lhc['mbw.a6r3.b1'].k0 = -lhc.ref['kd34.lr3']
lhc['mbw.b6r3.b1'].k0 = -lhc.ref['kd34.lr3']
lhc['mbw.c6r3.b1'].k0 = -lhc.ref['kd34.lr3']
lhc['mbw.d6r3.b1'].k0 = lhc.ref['kd34.lr3']
lhc['mbw.e6r3.b1'].k0 = lhc.ref['kd34.lr3']
lhc['mbw.f6r3.b1'].k0 = lhc.ref['kd34.lr3']

opt = lhc.b1.match(
    solve=False,
    betx=1, bety=1, x=0, init_at='ip3',
    start='mbw.f6l3.b1', end='mbw.f6r3.b1',
    vary=[xt.VaryList(['kd34.lr3'], step=1e-5)],
    targets=xt.TargetSet(x=(lhc['sep_ir3']/2 - lhc['sep_arc']/2), at=xt.END)
)
opt.solve()

tw0 = lhc.b1.twiss(init_at='ip3', betx=1, bety=1,
                   start='mbw.f6l3.b1', end='mbw.f6r3.b1',
                   strengths=True)
name_magnets_right = ['mbw.a6r3.b1', 'mbw.b6r3.b1', 'mbw.c6r3.b1',
                      'mbw.d6r3.b1', 'mbw.e6r3.b1', 'mbw.f6r3.b1']

for nn in name_magnets_right:

    lhc[nn].rbend_compensate_sagitta = False
    lhc[nn].rbend_model = 'straight-body'

    angle_in = np.arcsin(tw0['px', nn])
    angle_out = -np.arcsin(tw0['px', nn + '>>1'])

    angle = angle_in + angle_out
    rbend_angle_diff = angle_out - angle_in

    lhc[nn].angle = angle
    lhc[nn].rbend_angle_diff = rbend_angle_diff

    lhc[nn].rbend_shift = (lhc[nn]._x0_in - tw0['x', nn] + lhc['sep_ir3']/2
                           - lhc['sep_d34.lr3']/2)

lhc['abw.a6r3'] = lhc['mbw.a6r3.b1'].angle
lhc['abw.b6r3'] = lhc['mbw.b6r3.b1'].angle
lhc['abw.c6r3'] = lhc['mbw.c6r3.b1'].angle
lhc['abw.d6r3'] = lhc['mbw.d6r3.b1'].angle
lhc['abw.e6r3'] = lhc['mbw.e6r3.b1'].angle
lhc['abw.f6r3'] = lhc['mbw.f6r3.b1'].angle
lhc['abw.a6l3'] = lhc['abw.a6r3']
lhc['abw.b6l3'] = lhc['abw.b6r3']
lhc['abw.c6l3'] = lhc['abw.c6r3']
lhc['abw.d6l3'] = lhc['abw.d6r3']
lhc['abw.e6l3'] = lhc['abw.e6r3']
lhc['abw.f6l3'] = lhc['abw.f6r3']

lhc['adiff.bw.a6r3'] = lhc['mbw.a6r3.b1'].rbend_angle_diff
lhc['adiff.bw.b6r3'] = lhc['mbw.b6r3.b1'].rbend_angle_diff
lhc['adiff.bw.c6r3'] = lhc['mbw.c6r3.b1'].rbend_angle_diff
lhc['adiff.bw.d6r3'] = lhc['mbw.d6r3.b1'].rbend_angle_diff
lhc['adiff.bw.e6r3'] = lhc['mbw.e6r3.b1'].rbend_angle_diff
lhc['adiff.bw.f6r3'] = lhc['mbw.f6r3.b1'].rbend_angle_diff
lhc['adiff.bw.a6l3'] = -lhc['adiff.bw.a6r3']
lhc['adiff.bw.b6l3'] = -lhc['adiff.bw.b6r3']
lhc['adiff.bw.c6l3'] = -lhc['adiff.bw.c6r3']
lhc['adiff.bw.d6l3'] = -lhc['adiff.bw.d6r3']
lhc['adiff.bw.e6l3'] = -lhc['adiff.bw.e6r3']
lhc['adiff.bw.f6l3'] = -lhc['adiff.bw.f6r3']

lhc['shift.bw.a6r3'] = lhc['mbw.a6r3.b1'].rbend_shift
lhc['shift.bw.b6r3'] = lhc['mbw.b6r3.b1'].rbend_shift
lhc['shift.bw.c6r3'] = lhc['mbw.c6r3.b1'].rbend_shift
lhc['shift.bw.d6r3'] = lhc['mbw.d6r3.b1'].rbend_shift
lhc['shift.bw.e6r3'] = lhc['mbw.e6r3.b1'].rbend_shift
lhc['shift.bw.f6r3'] = lhc['mbw.f6r3.b1'].rbend_shift
lhc['shift.bw.a6l3'] = lhc['shift.bw.a6r3']
lhc['shift.bw.b6l3'] = lhc['shift.bw.b6r3']
lhc['shift.bw.c6l3'] = lhc['shift.bw.c6r3']
lhc['shift.bw.d6l3'] = lhc['shift.bw.d6r3']
lhc['shift.bw.e6l3'] = lhc['shift.bw.e6r3']
lhc['shift.bw.f6l3'] = lhc['shift.bw.f6r3']

lhc['afd.ipside.bw.a6r3'] = lhc['mbw.a6r3.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.b6r3'] = lhc['mbw.b6r3.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.c6r3'] = lhc['mbw.c6r3.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.d6r3'] = lhc['mbw.d6r3.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.e6r3'] = lhc['mbw.e6r3.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.f6r3'] = lhc['mbw.f6r3.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.a6l3'] = lhc['afd.ipside.bw.a6r3']
lhc['afd.ipside.bw.b6l3'] = lhc['afd.ipside.bw.b6r3']
lhc['afd.ipside.bw.c6l3'] = lhc['afd.ipside.bw.c6r3']
lhc['afd.ipside.bw.d6l3'] = lhc['afd.ipside.bw.d6r3']
lhc['afd.ipside.bw.e6l3'] = lhc['afd.ipside.bw.e6r3']
lhc['afd.ipside.bw.f6l3'] = lhc['afd.ipside.bw.f6r3']

lhc['afd.arcside.bw.a6r3'] = lhc['mbw.a6r3.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.b6r3'] = lhc['mbw.b6r3.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.c6r3'] = lhc['mbw.c6r3.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.d6r3'] = lhc['mbw.d6r3.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.e6r3'] = lhc['mbw.e6r3.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.f6r3'] = lhc['mbw.f6r3.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.a6l3'] = lhc['afd.arcside.bw.a6r3']
lhc['afd.arcside.bw.b6l3'] = lhc['afd.arcside.bw.b6r3']
lhc['afd.arcside.bw.c6l3'] = lhc['afd.arcside.bw.c6r3']
lhc['afd.arcside.bw.d6l3'] = lhc['afd.arcside.bw.d6r3']
lhc['afd.arcside.bw.e6l3'] = lhc['afd.arcside.bw.e6r3']
lhc['afd.arcside.bw.f6l3'] = lhc['afd.arcside.bw.f6r3']

# Adapt magnets

for mm in ['a', 'b', 'c', 'd', 'e', 'f']:
    pol = -1 if mm in ['a', 'b', 'c'] else 1
    lhc['mbw.'+mm+'6r3.b1'].rbend_model = 'straight-body'
    lhc['mbw.'+mm+'6r3.b1'].rbend_compensate_sagitta = False
    lhc['mbw.'+mm+'6r3.b1'].angle = lhc.ref['abw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b1'].rbend_angle_diff = lhc.ref['adiff.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b1'].k0 = pol * lhc.ref['kd34.lr3']
    lhc['mbw.'+mm+'6r3.b1'].rbend_shift = lhc.ref['shift.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b1'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b1'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b1'].edge_entry_model = 'linear'
    lhc['mbw.'+mm+'6r3.b1'].edge_exit_model = 'linear'

    lhc['mbw.'+mm+'6r3.b2'].rbend_model = 'straight-body'
    lhc['mbw.'+mm+'6r3.b2'].rbend_compensate_sagitta = False
    lhc['mbw.'+mm+'6r3.b2'].angle = lhc.ref['abw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b2'].k0 = pol * lhc.ref['kd34.lr3']
    lhc['mbw.'+mm+'6r3.b2'].rbend_shift = lhc.ref['shift.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b2'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b2'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.'+mm+'6r3']
    lhc['mbw.'+mm+'6r3.b2'].edge_entry_model = 'linear'
    lhc['mbw.'+mm+'6r3.b2'].edge_exit_model = 'linear'

for mm in ['a', 'b', 'c', 'd', 'e', 'f']:
    pol = -1 if mm in ['a', 'b', 'c'] else 1
    lhc['mbw.'+mm+'6l3.b1'].rbend_model = 'straight-body'
    lhc['mbw.'+mm+'6l3.b1'].rbend_compensate_sagitta = False
    lhc['mbw.'+mm+'6l3.b1'].angle = lhc.ref['abw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b1'].rbend_angle_diff = lhc.ref['adiff.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b1'].k0 = pol * lhc.ref['kd34.lr3']
    lhc['mbw.'+mm+'6l3.b1'].rbend_shift = lhc.ref['shift.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b1'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b1'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b1'].edge_entry_model = 'linear'
    lhc['mbw.'+mm+'6l3.b1'].edge_exit_model = 'linear'

    lhc['mbw.'+mm+'6l3.b2'].rbend_model = 'straight-body'
    lhc['mbw.'+mm+'6l3.b2'].rbend_compensate_sagitta = False
    lhc['mbw.'+mm+'6l3.b2'].angle = lhc.ref['abw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b2'].k0 = pol * lhc.ref['kd34.lr3']
    lhc['mbw.'+mm+'6l3.b2'].rbend_shift = lhc.ref['shift.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b2'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b2'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.'+mm+'6l3']
    lhc['mbw.'+mm+'6l3.b2'].edge_entry_model = 'linear'
    lhc['mbw.'+mm+'6l3.b2'].edge_exit_model = 'linear'




lhc.b1.cycle('ip6')
lhc.b2.cycle('ip6')

for line in [lhc.b1, lhc.b2]:
    line.slice_thick_elements(
            slicing_strategies=[
                # Slicing with thin elements
                xt.Strategy(slicing=None),
                xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbx.*'),
                xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbrc.*'),
                xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbrd.*'),
                xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbw.*'),
        ])

sv_b1_ip3 = lhc.b1.survey(element0='ip3', X0=-lhc['sep_ir3']/2)
sv_b2_ip3 = lhc.b2.survey(element0='ip3', X0=lhc['sep_ir3']/2, theta0=np.pi)

tw_b1_ip3 = lhc.b1.twiss4d(init_at='ip3', betx=tw1['betx', 'ip3'], bety=tw1['bety', 'ip3'])
tw_b2_ip3 = lhc.b2.twiss4d(init_at='ip3', betx=tw2['betx', 'ip3'], bety=tw2['bety', 'ip3'])

trajectory_b1_ip3 = sv_b1_ip3.p0 + tw_b1_ip3.x[:, None] * sv_b1_ip3.ex + tw_b1_ip3.y[:, None] * sv_b1_ip3.ey
trajectory_b2_ip3 = sv_b2_ip3.p0 + tw_b2_ip3.x[:, None] * sv_b2_ip3.ex + tw_b2_ip3.y[:, None] * sv_b2_ip3.ey

import matplotlib.pyplot as plt
plt.close('all')
plt.figure(1)
plt.plot(sv_b1_ip3.Z, sv_b1_ip3.X, label='Survey b1')
plt.plot(sv_b2_ip3.Z, sv_b2_ip3.X, label='Survey b2')
plt.plot(trajectory_b1_ip3[:, 2], trajectory_b1_ip3[:, 0], label='b1 ip3')
plt.plot(trajectory_b2_ip3[:, 2], trajectory_b2_ip3[:, 0], label='b2 ip3')
plt.legend()
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.title('Survey of IP3 region')
plt.xlim(-250, 250)
plt.ylim(-0.15, 0.15)
plt.grid()
plt.show()