import xtrack as xt
import numpy as np

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

tw1 = lhc.b1.twiss4d()
tw2 = lhc.b2.twiss4d()

# mbw.d6l7.b1
# mbw.c6l7.b1

# mbw.b6l7.b1
# mbw.a6l7.b1

# mbw.a6r7.b1
# mbw.b6r7.b1

# mbw.c6r7.b1
# mbw.d6r7.b1

lhc.b1.cycle('ip6')
lhc.b2.cycle('ip6')

# sep_arc
# sep_ir7

sv_b1 = lhc.b1.survey(element0='ip7', X0=lhc['sep_ir7']/2)
sv_b2 = lhc.b2.survey(element0='ip7', X0=-lhc['sep_ir7']/2, theta0=np.pi)

import matplotlib.pyplot as plt
plt.close('all')
plt.figure(1)
plt.plot(sv_b1.Z, sv_b1.X, label='b1')
plt.plot(sv_b2.Z, sv_b2.X, label='b2')
plt.legend()
plt.xlabel('Z [m]')
plt.ylabel('X [m]')
plt.title('Survey of IP7 region')
plt.grid()
