import xtrack as xt
import numpy as np

from rbend_config import config_rbend_ir3

lhc = xt.load('_lhc_raw.json')
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

# Adapt magnets
config_rbend_ir3(lhc)

tt_vars = lhc.vars.get_table()
tt_angles = tt_vars.rows[r'abw\.[a-f]6[lr]3']
tt_diff_angles = tt_vars.rows[r'adiff\.bw\.[a-f]6[lr]3']
tt_shifts = tt_vars.rows[r'shift\.bw\.[a-f]6[lr]3']
tt_k0 = tt_vars.rows[r'kd34\.lr3']

out_lines = []
out_lines.append('! Angles for RBends in IR3')
for nn in sorted(tt_angles.name):
    out_lines.append(f'{nn} = {tt_angles["value", nn]:.10e};')
out_lines.append('')
out_lines.append('! In-out angle differences for RBends in IR3')
for nn in sorted(tt_diff_angles.name):
    out_lines.append(f'{nn} = {tt_diff_angles["value", nn]:.10e};')
out_lines.append('')
out_lines.append('! Shifts for RBends in IR3')
for nn in sorted(tt_shifts.name):
    out_lines.append(f'{nn} = {tt_shifts["value", nn]:.10e};')

with open('rbend_config_ip3.madx', 'w') as fid:
    fid.write('\n'.join(out_lines))

out_lines = []
out_lines.append('! k0 for RBends in IR3')
for nn in sorted(tt_k0.name):
    out_lines.append(f'{nn} = {tt_k0["value", nn]:.10e};')

with open('rbend_strengths_ip3.madx', 'w') as fid:
    fid.write('\n'.join(out_lines))

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