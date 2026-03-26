import xtrack as xt

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

lhc.b1.twiss4d().rows['ip.*'].cols['betx bety x y px py']
lhc.b2.twiss4d().rows['ip.*'].cols['betx bety x y px py']