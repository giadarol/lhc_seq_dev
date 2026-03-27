import xtrack as xt

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
