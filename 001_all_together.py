import xtrack as xt
import numpy as np

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

# Patch rbend k0 from the optics
lhc.vars.load('rbend_strengths_ip1258.madx')
lhc.vars.load('rbend_strengths_ip3.madx')
lhc.vars.load('rbend_strengths_ip4.madx')
lhc.vars.load('rbend_strengths_ip7.madx')

tw1 = lhc.b1.twiss4d()
tw2 = lhc.b2.twiss4d()

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

sv_b1_ip7 = lhc.b1.survey(element0='ip7', X0=lhc['sep_ir7']/2)
sv_b2_ip7 = lhc.b2.survey(element0='ip7', X0=-lhc['sep_ir7']/2, theta0=np.pi)

tw_b1_ip7 = lhc.b1.twiss4d(init_at='ip7', betx=tw1['betx', 'ip7'], bety=tw1['bety', 'ip7'])
tw_b2_ip7 = lhc.b2.twiss4d(init_at='ip7', betx=tw2['betx', 'ip7'], bety=tw2['bety', 'ip7'])

trajectory_b1_ip7 = sv_b1_ip7.p0 + tw_b1_ip7.x[:, None] * sv_b1_ip7.ex + tw_b1_ip7.y[:, None] * sv_b1_ip7.ey
trajectory_b2_ip7 = sv_b2_ip7.p0 + tw_b2_ip7.x[:, None] * sv_b2_ip7.ex + tw_b2_ip7.y[:, None] * sv_b2_ip7.ey

sv_b1_ip3 = lhc.b1.survey(element0='ip3', X0=-lhc['sep_ir3']/2)
sv_b2_ip3 = lhc.b2.survey(element0='ip3', X0=lhc['sep_ir3']/2, theta0=np.pi)

tw_b1_ip3 = lhc.b1.twiss4d(init_at='ip3', betx=tw1['betx', 'ip3'], bety=tw1['bety', 'ip3'])
tw_b2_ip3 = lhc.b2.twiss4d(init_at='ip3', betx=tw2['betx', 'ip3'], bety=tw2['bety', 'ip3'])

trajectory_b1_ip3 = sv_b1_ip3.p0 + tw_b1_ip3.x[:, None] * sv_b1_ip3.ex + tw_b1_ip3.y[:, None] * sv_b1_ip3.ey
trajectory_b2_ip3 = sv_b2_ip3.p0 + tw_b2_ip3.x[:, None] * sv_b2_ip3.ex + tw_b2_ip3.y[:, None] * sv_b2_ip3.ey

sv_b1_ip4 = lhc.b1.survey(element0='ip4', X0=-lhc['sep_ir4']/2)
sv_b2_ip4 = lhc.b2.survey(element0='ip4', X0=lhc['sep_ir4']/2, theta0=np.pi)

tw_b1_ip4 = lhc.b1.twiss4d(init_at='ip4', betx=tw1['betx', 'ip4'], bety=tw1['bety', 'ip4'])
tw_b2_ip4 = lhc.b2.twiss4d(init_at='ip4', betx=tw2['betx', 'ip4'], bety=tw2['bety', 'ip4'])

trajectory_b1_ip4 = sv_b1_ip4.p0 + tw_b1_ip4.x[:, None] * sv_b1_ip4.ex + tw_b1_ip4.y[:, None] * sv_b1_ip4.ey
trajectory_b2_ip4 = sv_b2_ip4.p0 + tw_b2_ip4.x[:, None] * sv_b2_ip4.ex + tw_b2_ip4.y[:, None] * sv_b2_ip4.ey

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

plt.figure(3)
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

plt.figure(4)
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

plt.figure(7)
plt.plot(sv_b1_ip7.Z, sv_b1_ip7.X, label='Survey b1')
plt.plot(sv_b2_ip7.Z, sv_b2_ip7.X, label='Survey b2')
plt.plot(trajectory_b1_ip7[:, 2], trajectory_b1_ip7[:, 0], label='b1 ip7')
plt.plot(trajectory_b2_ip7[:, 2], trajectory_b2_ip7[:, 0], label='b2 ip7')
plt.legend()
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.title('Survey of IP7 region')
plt.xlim(-250, 250)
plt.ylim(-0.15, 0.15)




plt.show()
