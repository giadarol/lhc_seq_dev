import xtrack as xt

import xtrack as xt
import numpy as np

from rbend_config import config_rbend_ir4

lhc = xt.load('_lhc_raw.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

tw1 = lhc.b1.twiss4d()
tw2 = lhc.b2.twiss4d()

# mbrb --> 194
# mbrs --> 220
lhc['sep_mbrb.lr4'] = 0.194 # To be checked!!!!!
lhc['sep_mbrs.lr4'] = 0.414 # To be checked!!!!!

# Reference
# https://edms.cern.ch/ui/file/397126/2/vacrev.pdf


# mbrb.5l4.b1        9868.6 RBend           True     False None        None       
# mbrs.5l4.b1        9940.5 RBend           True     False None        None       
# mbrs.5r4.b1       10044.1 RBend           True     False None        None       
# mbrb.5r4.b1         10116 RBend           True     False None        None       

lhc['mbrs.5r4.b1'].angle = 0
lhc['mbrb.5r4.b1'].angle = 0

lhc['mbrs.5r4.b1'].k0 = -lhc.ref['kd3.r4']
lhc['mbrb.5r4.b1'].k0 = lhc.ref['kd4.r4']

opt = lhc.b1.match(
    solve=False,
    betx=1, bety=1, x=0, init_at='ip4',
    start='ip4', end='mbrb.5r4.b1',
    vary=[xt.VaryList(['kd3.r4', 'kd4.r4'], step=1e-5)],
    targets=xt.TargetSet(x=(lhc['sep_ir4']/2 - lhc['sep_arc']/2), at=xt.END)
)
opt.solve()

tw0 = lhc.b1.twiss(init_at='ip4', betx=1, bety=1,
                   start='ip4', end='mbrb.5r4.b1',
                   strengths=True)

for nn in ['mbrs.5r4.b1', 'mbrb.5r4.b1']:

    lhc[nn].rbend_compensate_sagitta = False
    lhc[nn].rbend_model = 'straight-body'

    angle_in = np.arcsin(tw0['px', nn])
    angle_out = -np.arcsin(tw0['px', nn + '>>1'])

    angle = angle_in + angle_out
    rbend_angle_diff = angle_out - angle_in

    lhc[nn].angle = angle
    lhc[nn].rbend_angle_diff = rbend_angle_diff

lhc['mbrs.5r4.b1'].rbend_shift = (lhc['mbrs.5r4.b1']._x0_in - tw0['x', 'mbrs.5r4.b1']
                                  + (lhc['sep_ir4']/2 - lhc['sep_mbrs.lr4']/2))
lhc['mbrb.5r4.b1'].rbend_shift = (lhc['mbrb.5r4.b1']._x0_in - tw0['x', 'mbrb.5r4.b1']
                                  + (lhc['sep_ir4']/2 - lhc['sep_mbrb.lr4']/2))

lhc['ad3.r4'] = -lhc['mbrs.5r4.b1'].angle
lhc['ad4.r4'] = lhc['mbrb.5r4.b1'].angle
lhc['ad4.l4'] = lhc['ad4.r4']
lhc['ad3.l4'] = lhc['ad3.r4']

lhc['shift.mbrs.r4'] = lhc['mbrs.5r4.b1'].rbend_shift
lhc['shift.mbrb.r4'] = lhc['mbrb.5r4.b1'].rbend_shift
lhc['shift.mbrs.l4'] = lhc['shift.mbrs.r4']
lhc['shift.mbrb.l4'] = lhc['shift.mbrb.r4']

tt_vars = lhc.vars.get_table()

tt_angles = tt_vars.rows[r'ad[34]\.[lr]4']
tt_shifts = tt_vars.rows[r'shift\.mbr[sb]\.[lr]4']
tt_k0 = tt_vars.rows[r'kd[34]\.[lr]4']

out_lines = []
out_lines.append('! IR4 RBend angles')
for nn in sorted(tt_angles.name):
    out_lines.append(f'{nn} = {tt_angles["value", nn]:.10e};')
out_lines.append('\n! IR4 RBend shifts')
for nn in sorted(tt_shifts.name):
    out_lines.append(f'{nn} = {tt_shifts["value", nn]:.10e};')
with open('rbend_config_ip4.madx', 'w') as fid:
    fid.write('\n'.join(out_lines))

out_lines = []
out_lines.append('! IR4 RBend k0')
for nn in sorted(tt_k0.name):
    out_lines.append(f'{nn} = {tt_k0["value", nn]:.10e};')
with open('rbend_strengths_ip4.madx', 'w') as fid:
    fid.write('\n'.join(out_lines))

# Adapt magnets
config_rbend_ir4(lhc)

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
                xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbrs.*'),
                xt.Strategy(slicing=xt.Uniform(3, mode='thick'), name='mbrb.*'),
        ])

sv_b1_ip4 = lhc.b1.survey(element0='ip4', X0=-lhc['sep_ir4']/2)
sv_b2_ip4 = lhc.b2.survey(element0='ip4', X0=lhc['sep_ir4']/2, theta0=np.pi)

tw_b1_ip4 = lhc.b1.twiss4d(init_at='ip4', betx=tw1['betx', 'ip4'], bety=tw1['bety', 'ip4'])
tw_b2_ip4 = lhc.b2.twiss4d(init_at='ip4', betx=tw2['betx', 'ip4'], bety=tw2['bety', 'ip4'])

trajectory_b1_ip4 = sv_b1_ip4.p0 + tw_b1_ip4.x[:, None] * sv_b1_ip4.ex + tw_b1_ip4.y[:, None] * sv_b1_ip4.ey
trajectory_b2_ip4 = sv_b2_ip4.p0 + tw_b2_ip4.x[:, None] * sv_b2_ip4.ex + tw_b2_ip4.y[:, None] * sv_b2_ip4.ey

import matplotlib.pyplot as plt
plt.close('all')
plt.figure(1)
plt.plot(sv_b1_ip4.Z, sv_b1_ip4.X, label='Survey b1')
plt.plot(sv_b2_ip4.Z, sv_b2_ip4.X, label='Survey b2')
plt.plot(trajectory_b1_ip4[:, 2], trajectory_b1_ip4[:, 0], label='b1 ip4')
plt.plot(trajectory_b2_ip4[:, 2], trajectory_b2_ip4[:, 0], label='b2 ip4')
plt.legend()
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.title('Survey of IP4 region')
plt.xlim(-160, 160)
plt.ylim(-0.23, 0.23)
plt.grid()

plt.show()