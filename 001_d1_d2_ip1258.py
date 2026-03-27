import xtrack as xt
import numpy as np

from rbend_config import config_rbend_ir15, config_rbend_ir28

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

tw1 = lhc.b1.twiss4d().rows['ip.*'].cols['betx bety x y px py']
tw2 = lhc.b2.twiss4d().rows['ip.*'].cols['betx bety x y px py']

for ip_name in ['ip5', 'ip2']:

    if ip_name == 'ip5':
        d1_name = 'mbxf.4r5/b1'
        d2_name = 'mbrd.4r5.b1'
        k0_d1_var_name = 'kd1.r5'
        k0_d2_var_name = 'kd2.r5'
        angle_d1_var_name = 'ad1.r5'
        angle_d2_var_name = 'ad2.r5'
        sep_d2 = 0.188
        orientation = 1 # 1 if b1 is going from inside to outside, -1 otherwise

    elif ip_name == 'ip2':
        ip_name = 'ip2'
        d1_name = 'mbx.4r2/b1'
        d2_name = 'mbrc.4r2.b1'
        k0_d1_var_name = 'kd1.r2'
        k0_d2_var_name = 'kd2.r2'
        angle_d1_var_name = 'ad1.r2'
        angle_d2_var_name = 'ad2.r2'
        sep_d2 = 0.188
        orientation = -1 # 1 if b1 is going from inside to outside, -1 otherwise


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
                    start=ip_name, end=tt.rows[d2_name + '>>1'].name[-1])

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
    line[d2_name].rbend_shift = line[d2_name]._x0_out - tw0['x', '_end_point'] + orientation * sep_d2 / 2

    if ip_name == 'ip5':
        # Adapt variables
        lhc['ad1.r5'] = np.abs(line[d1_name].angle)
        lhc['ad1.l5'] = np.abs(line[d1_name].angle)
        lhc['ad2.r5'] = np.abs(line[d2_name].angle)
        lhc['ad2.l5'] = np.abs(line[d2_name].angle)
        lhc['ad1.r1'] = np.abs(line[d1_name].angle)
        lhc['ad1.l1'] = np.abs(line[d1_name].angle)
        lhc['ad2.r1'] = np.abs(line[d2_name].angle)
        lhc['ad2.l1'] = np.abs(line[d2_name].angle)

        lhc['kd1.r5'] = np.abs(line[d1_name].k0)
        lhc['kd1.l5'] = np.abs(line[d1_name].k0)
        lhc['kd2.r5'] = np.abs(line[d2_name].k0)
        lhc['kd2.l5'] = np.abs(line[d2_name].k0)
        lhc['kd1.r1'] = np.abs(line[d1_name].k0)
        lhc['kd1.l1'] = np.abs(line[d1_name].k0)
        lhc['kd2.r1'] = np.abs(line[d2_name].k0)
        lhc['kd2.l1'] = np.abs(line[d2_name].k0)

        lhc['sep_mid_d1.r5'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['sep_mid_d1.l5'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['sep_mid_d1.r1'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['sep_mid_d1.l1'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['shift_d2.r5'] = line[d2_name].rbend_shift
        lhc['shift_d2.l5'] = line[d2_name].rbend_shift
        lhc['shift_d2.r1'] = line[d2_name].rbend_shift
        lhc['shift_d2.l1'] = line[d2_name].rbend_shift

        config_rbend_ir15(lhc)

    elif ip_name == 'ip2':
        # Adapt variables
        lhc['ad1.r8'] = np.abs(line[d1_name].angle)
        lhc['ad1.l8'] = np.abs(line[d1_name].angle)
        lhc['ad2.r8'] = np.abs(line[d2_name].angle)
        lhc['ad2.l8'] = np.abs(line[d2_name].angle)
        lhc['ad1.r2'] = np.abs(line[d1_name].angle)
        lhc['ad1.l2'] = np.abs(line[d1_name].angle)
        lhc['ad2.r2'] = np.abs(line[d2_name].angle)
        lhc['ad2.l2'] = np.abs(line[d2_name].angle)

        lhc['kd1.r8'] = np.abs(line[d1_name].k0)
        lhc['kd1.l8'] = np.abs(line[d1_name].k0)
        lhc['kd2.r8'] = np.abs(line[d2_name].k0)
        lhc['kd2.l8'] = np.abs(line[d2_name].k0)
        lhc['kd1.r2'] = np.abs(line[d1_name].k0)
        lhc['kd1.l2'] = np.abs(line[d1_name].k0)
        lhc['kd2.r2'] = np.abs(line[d2_name].k0)
        lhc['kd2.l2'] = np.abs(line[d2_name].k0)

        lhc['sep_mid_d1.r8'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['sep_mid_d1.l8'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['sep_mid_d1.r2'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['sep_mid_d1.l2'] = 2 * np.abs(line[d1_name].rbend_shift)
        lhc['shift_d2.r8'] = np.abs(line[d2_name].rbend_shift)
        lhc['shift_d2.l8'] = np.abs(line[d2_name].rbend_shift)
        lhc['shift_d2.r2'] = np.abs(line[d2_name].rbend_shift)
        lhc['shift_d2.l2'] = np.abs(line[d2_name].rbend_shift)

        config_rbend_ir28(lhc)

tt_vars = lhc.vars.get_table()

tt_angle = tt_vars.rows['ad.*[lr][1,2,5,8]']
tt_sep = tt_vars.rows['sep_mid_d1.*[lr][1,2,5,8]']
tt_shift = tt_vars.rows['shift_d2.*[lr][1,2,5,8]']

tt_k0 = tt_vars.rows['kd.*[lr][1,2,5,8]']


# Save here

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

        ])

sv_b1_ip5 = lhc.b1.survey(element0='ip5')
tw_b1_ip5 = lhc.b1.twiss4d(init_at='ip5', betx=0.15, bety=0.15)
trajectory_b1_ip5 = sv_b1_ip5.p0 + tw_b1_ip5.x[:, None] * sv_b1_ip5.ex + tw_b1_ip5.y[:, None] * sv_b1_ip5.ey
sv_b2_ip5 = lhc.b2.survey(element0='ip5', theta0=np.pi)
tw_b2_ip5 = lhc.b2.twiss4d(init_at='ip5', betx=0.15, bety=0.15)
trajectory_b2_ip5 = sv_b2_ip5.p0 + tw_b2_ip5.x[:, None] * sv_b2_ip5.ex + tw_b2_ip5.y[:, None] * sv_b2_ip5.ey

sv_b1_ip1 = lhc.b1.survey(element0='ip1')
tw_b1_ip1 = lhc.b1.twiss4d(init_at='ip1', betx=0.15, bety=0.15)
trajectory_b1_ip1 = sv_b1_ip1.p0 + tw_b1_ip1.x[:, None] * sv_b1_ip1.ex + tw_b1_ip1.y[:, None] * sv_b1_ip1.ey
sv_b2_ip1 = lhc.b2.survey(element0='ip1', theta0=np.pi)
tw_b2_ip1 = lhc.b2.twiss4d(init_at='ip1')
trajectory_b2_ip1 = sv_b2_ip1.p0 + tw_b2_ip1.x[:, None] * sv_b2_ip1.ex + tw_b2_ip1.y[:, None] * sv_b2_ip1.ey

sv_b1_ip2 = lhc.b1.survey(element0='ip2')
tw_b1_ip2 = lhc.b1.twiss4d(init_at='ip2', betx=tw1['betx', 'ip2'], bety=tw1['bety', 'ip2'])
trajectory_b1_ip2 = sv_b1_ip2.p0 + tw_b1_ip2.x[:, None] * sv_b1_ip2.ex + tw_b1_ip2.y[:, None] * sv_b1_ip2.ey
sv_b2_ip2 = lhc.b2.survey(element0='ip2', theta0=np.pi)
tw_b2_ip2 = lhc.b2.twiss4d(init_at='ip2', betx=tw2['betx', 'ip2'], bety=tw2['bety', 'ip2'])
trajectory_b2_ip2 = sv_b2_ip2.p0 + tw_b2_ip2.x[:, None] * sv_b2_ip2.ex + tw_b2_ip2.y[:, None] * sv_b2_ip2.ey

sv_b1_ip8 = lhc.b1.survey(element0='ip8')
tw_b1_ip8 = lhc.b1.twiss4d(init_at='ip8', betx=0.15, bety=0.15)
trajectory_b1_ip8 = sv_b1_ip8.p0 + tw_b1_ip8.x[:, None] * sv_b1_ip8.ex + tw_b1_ip8.y[:, None] * sv_b1_ip8.ey
sv_b2_ip8 = lhc.b2.survey(element0='ip8', theta0=np.pi)
tw_b2_ip8 = lhc.b2.twiss4d(init_at='ip8', betx=0.15, bety=0.15)
trajectory_b2_ip8 = sv_b2_ip8.p0 + tw_b2_ip8.x[:, None] * sv_b2_ip8.ex + tw_b2_ip8.y[:, None] * sv_b2_ip8.ey

import matplotlib.pyplot as plt
plt.close('all')

plt.figure(5)
plt.suptitle('IP5')
plt.plot(sv_b1_ip5.Z, sv_b1_ip5.X, label='X survey B1')
plt.plot(sv_b2_ip5.Z, sv_b2_ip5.X, label='X survey B2')
plt.plot(trajectory_b1_ip5[:, 2], trajectory_b1_ip5[:, 0], '--', label='X trajectory B1')
plt.plot(trajectory_b2_ip5[:, 2], trajectory_b2_ip5[:, 0], '--', label='X trajectory B2')
plt.xlim(-180, 180)
plt.ylim(-0.15, 0.15)
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.legend()

plt.figure(1)
plt.suptitle('IP1')
plt.plot(sv_b1_ip1.Z, sv_b1_ip1.X, label='X survey B1')
plt.plot(sv_b2_ip1.Z, sv_b2_ip1.X, label='X survey B2')
plt.plot(trajectory_b1_ip1[:, 2], trajectory_b1_ip1[:, 0], '--', label='X trajectory B1')
plt.plot(trajectory_b2_ip1[:, 2], trajectory_b2_ip1[:, 0], '--', label='X trajectory B2')
plt.xlim(-180, 180)
plt.ylim(-0.15, 0.15)
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.legend()

plt.figure(2)
plt.suptitle('IP2')
plt.plot(sv_b1_ip2.Z, sv_b1_ip2.X, label='X survey B1')
plt.plot(sv_b2_ip2.Z, sv_b2_ip2.X, label='X survey B2')
plt.plot(trajectory_b1_ip2[:, 2], trajectory_b1_ip2[:, 0], '--', label='X trajectory B1')
plt.plot(trajectory_b2_ip2[:, 2], trajectory_b2_ip2[:, 0], '--', label='X trajectory B2')
plt.xlim(-180, 180)
plt.ylim(-0.15, 0.15)
plt.xlabel('Z [m]')
plt.ylabel('X [m]')

plt.figure(8)
plt.suptitle('IP8')
plt.plot(sv_b1_ip8.Z, sv_b1_ip8.X, label='X survey B1')
plt.plot(sv_b2_ip8.Z, sv_b2_ip8.X, label='X survey B2')
plt.plot(trajectory_b1_ip8[:, 2], trajectory_b1_ip8[:, 0], '--', label='X trajectory B1')
plt.plot(trajectory_b2_ip8[:, 2], trajectory_b2_ip8[:, 0], '--', label='X trajectory B2')
plt.xlim(-180, 180)
plt.ylim(-0.15, 0.15)
plt.xlabel('Z [m]')
plt.ylabel('X [m]')

plt.show()

# k0_d1_name 
