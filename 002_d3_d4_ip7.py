import xtrack as xt
import numpy as np

lhc = xt.load('lhc.json')
lhc.vars.load('opt_150.madx')

lhc.b1.set_particle_ref('proton', energy0=7e12)
lhc.b2.set_particle_ref('proton', energy0=7e12)

tw1 = lhc.b1.twiss4d()
tw2 = lhc.b2.twiss4d()

lhc['sep_d34.lr7'] = 0.190 # To be checked!!!!!

lhc['mbw.a6r7.b1'].angle = 0
lhc['mbw.b6r7.b1'].angle = 0
lhc['mbw.c6r7.b1'].angle = 0
lhc['mbw.d6r7.b1'].angle = 0

lhc['mbw.d6l7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.c6l7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.b6l7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.a6l7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.a6r7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.b6r7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.c6r7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.d6r7.b1'].k0 = -lhc.ref['kd34.lr7']

opt = lhc.b1.match(
    solve=False,
    betx=1, bety=1, x=0, init_at='ip7',
    start='mbw.d6l7.b1', end='mbw.d6r7.b1',
    vary=[xt.VaryList(['kd34.lr7'], step=1e-5)],
    targets=xt.TargetSet(x=-(lhc['sep_ir7']/2 - lhc['sep_arc']/2), at=xt.END)
)
opt.solve()

tw0 = lhc.b1.twiss(init_at='ip7', betx=1, bety=1,
                   start='mbw.d6l7.b1', end='mbw.d6r7.b1',
                   strengths=True)
name_mangets_right = ['mbw.a6r7.b1', 'mbw.b6r7.b1', 'mbw.c6r7.b1', 'mbw.d6r7.b1']

for nn in name_mangets_right:

    lhc[nn].rbend_compensate_sagitta = False
    lhc[nn].rbend_model = 'straight-body'

    angle_in = np.arcsin(tw0['px', nn])
    angle_out = -np.arcsin(tw0['px', nn + '>>1'])

    angle = angle_in + angle_out
    rbend_angle_diff = angle_out - angle_in

    lhc[nn].angle = angle
    lhc[nn].rbend_angle_diff = rbend_angle_diff

    lhc[nn].rbend_shift = (lhc[nn]._x0_in - tw0['x', nn] - lhc['sep_ir7']/2
                           + lhc['sep_d34.lr7']/2)

lhc['abw.a6r7'] = lhc['mbw.a6r7.b1'].angle
lhc['abw.b6r7'] = lhc['mbw.b6r7.b1'].angle
lhc['abw.c6r7'] = lhc['mbw.c6r7.b1'].angle
lhc['abw.d6r7'] = lhc['mbw.d6r7.b1'].angle
lhc['abw.a6l7'] = lhc['abw.a6r7']
lhc['abw.b6l7'] = lhc['abw.b6r7']
lhc['abw.c6l7'] = lhc['abw.c6r7']
lhc['abw.d6l7'] = lhc['abw.d6r7']

lhc['adiff.bw.a6r7'] = lhc['mbw.a6r7.b1'].rbend_angle_diff
lhc['adiff.bw.b6r7'] = lhc['mbw.b6r7.b1'].rbend_angle_diff
lhc['adiff.bw.c6r7'] = lhc['mbw.c6r7.b1'].rbend_angle_diff
lhc['adiff.bw.d6r7'] = lhc['mbw.d6r7.b1'].rbend_angle_diff
lhc['adiff.bw.a6l7'] = -lhc['adiff.bw.a6r7']
lhc['adiff.bw.b6l7'] = -lhc['adiff.bw.b6r7']
lhc['adiff.bw.c6l7'] = -lhc['adiff.bw.c6r7']
lhc['adiff.bw.d6l7'] = -lhc['adiff.bw.d6r7']

lhc['shift.bw.a6r7'] = lhc['mbw.a6r7.b1'].rbend_shift
lhc['shift.bw.b6r7'] = lhc['mbw.b6r7.b1'].rbend_shift
lhc['shift.bw.c6r7'] = lhc['mbw.c6r7.b1'].rbend_shift
lhc['shift.bw.d6r7'] = lhc['mbw.d6r7.b1'].rbend_shift
lhc['shift.bw.a6l7'] = lhc['shift.bw.a6r7']
lhc['shift.bw.b6l7'] = lhc['shift.bw.b6r7']
lhc['shift.bw.c6l7'] = lhc['shift.bw.c6r7']
lhc['shift.bw.d6l7'] = lhc['shift.bw.d6r7']

lhc['afd.ipside.bw.a6r7'] = lhc['mbw.a6r7.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.b6r7'] = lhc['mbw.b6r7.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.c6r7'] = lhc['mbw.c6r7.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.d6r7'] = lhc['mbw.d6r7.b1'].edge_entry_angle_fdown
lhc['afd.ipside.bw.a6l7'] = lhc['afd.ipside.bw.a6r7']
lhc['afd.ipside.bw.b6l7'] = lhc['afd.ipside.bw.b6r7']
lhc['afd.ipside.bw.c6l7'] = lhc['afd.ipside.bw.c6r7']
lhc['afd.ipside.bw.d6l7'] = lhc['afd.ipside.bw.d6r7']

lhc['afd.arcside.bw.a6r7'] = lhc['mbw.a6r7.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.b6r7'] = lhc['mbw.b6r7.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.c6r7'] = lhc['mbw.c6r7.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.d6r7'] = lhc['mbw.d6r7.b1'].edge_exit_angle_fdown
lhc['afd.arcside.bw.a6l7'] = lhc['afd.arcside.bw.a6r7']
lhc['afd.arcside.bw.b6l7'] = lhc['afd.arcside.bw.b6r7']
lhc['afd.arcside.bw.c6l7'] = lhc['afd.arcside.bw.c6r7']
lhc['afd.arcside.bw.d6l7'] = lhc['afd.arcside.bw.d6r7']

# Adapt magnets
lhc['mbw.a6r7.b1'].rbend_model = 'straight-body'
lhc['mbw.a6r7.b1'].rbend_compensate_sagitta = False
lhc['mbw.a6r7.b1'].angle = lhc.ref['abw.a6r7']
lhc['mbw.a6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.a6r7']
lhc['mbw.a6r7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.a6r7.b1'].rbend_shift = lhc.ref['shift.bw.a6r7']
lhc['mbw.a6r7.b1'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.a6r7']
lhc['mbw.a6r7.b1'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.a6r7']
lhc['mbw.a6r7.b1'].edge_entry_model = 'linear'
lhc['mbw.a6r7.b1'].edge_exit_model = 'linear'

lhc['mbw.a6r7.b2'].rbend_model = 'straight-body'
lhc['mbw.a6r7.b2'].rbend_compensate_sagitta = False
lhc['mbw.a6r7.b2'].angle = lhc.ref['abw.a6r7']
lhc['mbw.a6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.a6r7']
lhc['mbw.a6r7.b2'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.a6r7.b2'].rbend_shift = lhc.ref['shift.bw.a6r7']
lhc['mbw.a6r7.b2'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.a6r7']
lhc['mbw.a6r7.b2'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.a6r7']
lhc['mbw.a6r7.b2'].edge_entry_model = 'linear'
lhc['mbw.a6r7.b2'].edge_exit_model = 'linear'

lhc['mbw.b6r7.b1'].rbend_model = 'straight-body'
lhc['mbw.b6r7.b1'].rbend_compensate_sagitta = False
lhc['mbw.b6r7.b1'].angle = lhc.ref['abw.b6r7']
lhc['mbw.b6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.b6r7']
lhc['mbw.b6r7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.b6r7.b1'].rbend_shift = lhc.ref['shift.bw.b6r7']
lhc['mbw.b6r7.b1'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.b6r7']
lhc['mbw.b6r7.b1'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.b6r7']
lhc['mbw.b6r7.b1'].edge_entry_model = 'linear'
lhc['mbw.b6r7.b1'].edge_exit_model = 'linear'

lhc['mbw.b6r7.b2'].rbend_model = 'straight-body'
lhc['mbw.b6r7.b2'].rbend_compensate_sagitta = False
lhc['mbw.b6r7.b2'].angle = lhc.ref['abw.b6r7']
lhc['mbw.b6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.b6r7']
lhc['mbw.b6r7.b2'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.b6r7.b2'].rbend_shift = lhc.ref['shift.bw.b6r7']
lhc['mbw.b6r7.b2'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.b6r7']
lhc['mbw.b6r7.b2'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.b6r7']
lhc['mbw.b6r7.b2'].edge_entry_model = 'linear'
lhc['mbw.b6r7.b2'].edge_exit_model = 'linear'

lhc['mbw.c6r7.b1'].rbend_model = 'straight-body'
lhc['mbw.c6r7.b1'].rbend_compensate_sagitta = False
lhc['mbw.c6r7.b1'].angle = lhc.ref['abw.c6r7']
lhc['mbw.c6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.c6r7']
lhc['mbw.c6r7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.c6r7.b1'].rbend_shift = lhc.ref['shift.bw.c6r7']
lhc['mbw.c6r7.b1'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.c6r7']
lhc['mbw.c6r7.b1'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.c6r7']
lhc['mbw.c6r7.b1'].edge_entry_model = 'linear'
lhc['mbw.c6r7.b1'].edge_exit_model = 'linear'

lhc['mbw.c6r7.b2'].rbend_model = 'straight-body'
lhc['mbw.c6r7.b2'].rbend_compensate_sagitta = False
lhc['mbw.c6r7.b2'].angle = lhc.ref['abw.c6r7']
lhc['mbw.c6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.c6r7']
lhc['mbw.c6r7.b2'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.c6r7.b2'].rbend_shift = lhc.ref['shift.bw.c6r7']
lhc['mbw.c6r7.b2'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.c6r7']
lhc['mbw.c6r7.b2'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.c6r7']
lhc['mbw.c6r7.b2'].edge_entry_model = 'linear'
lhc['mbw.c6r7.b2'].edge_exit_model = 'linear'

lhc['mbw.d6r7.b1'].rbend_model = 'straight-body'
lhc['mbw.d6r7.b1'].rbend_compensate_sagitta = False
lhc['mbw.d6r7.b1'].angle = lhc.ref['abw.d6r7']
lhc['mbw.d6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.d6r7']
lhc['mbw.d6r7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.d6r7.b1'].rbend_shift = lhc.ref['shift.bw.d6r7']
lhc['mbw.d6r7.b1'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.d6r7']
lhc['mbw.d6r7.b1'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.d6r7']
lhc['mbw.d6r7.b1'].edge_entry_model = 'linear'
lhc['mbw.d6r7.b1'].edge_exit_model = 'linear'

lhc['mbw.d6r7.b2'].rbend_model = 'straight-body'
lhc['mbw.d6r7.b2'].rbend_compensate_sagitta = False
lhc['mbw.d6r7.b2'].angle = lhc.ref['abw.d6r7']
lhc['mbw.d6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.d6r7']
lhc['mbw.d6r7.b2'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.d6r7.b2'].rbend_shift = lhc.ref['shift.bw.d6r7']
lhc['mbw.d6r7.b2'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.d6r7']
lhc['mbw.d6r7.b2'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.d6r7']
lhc['mbw.d6r7.b2'].edge_entry_model = 'linear'
lhc['mbw.d6r7.b2'].edge_exit_model = 'linear'

lhc['mbw.a6l7.b1'].rbend_model = 'straight-body'
lhc['mbw.a6l7.b1'].rbend_compensate_sagitta = False
lhc['mbw.a6l7.b1'].angle = lhc.ref['abw.a6l7']
lhc['mbw.a6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.a6l7']
lhc['mbw.a6l7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.a6l7.b1'].rbend_shift = lhc.ref['shift.bw.a6l7']
lhc['mbw.a6l7.b1'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.a6l7']
lhc['mbw.a6l7.b1'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.a6l7']
lhc['mbw.a6l7.b1'].edge_entry_model = 'linear'
lhc['mbw.a6l7.b1'].edge_exit_model = 'linear'

lhc['mbw.a6l7.b2'].rbend_model = 'straight-body'
lhc['mbw.a6l7.b2'].rbend_compensate_sagitta = False
lhc['mbw.a6l7.b2'].angle = lhc.ref['abw.a6l7']
lhc['mbw.a6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.a6l7']
lhc['mbw.a6l7.b2'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.a6l7.b2'].rbend_shift = lhc.ref['shift.bw.a6l7']
lhc['mbw.a6l7.b2'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.a6l7']
lhc['mbw.a6l7.b2'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.a6l7']
lhc['mbw.a6l7.b2'].edge_entry_model = 'linear'
lhc['mbw.a6l7.b2'].edge_exit_model = 'linear'

lhc['mbw.b6l7.b1'].rbend_model = 'straight-body'
lhc['mbw.b6l7.b1'].rbend_compensate_sagitta = False
lhc['mbw.b6l7.b1'].angle = lhc.ref['abw.b6l7']
lhc['mbw.b6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.b6l7']
lhc['mbw.b6l7.b1'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.b6l7.b1'].rbend_shift = lhc.ref['shift.bw.b6l7']
lhc['mbw.b6l7.b1'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.b6l7']
lhc['mbw.b6l7.b1'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.b6l7']
lhc['mbw.b6l7.b1'].edge_entry_model = 'linear'
lhc['mbw.b6l7.b1'].edge_exit_model = 'linear'

lhc['mbw.b6l7.b2'].rbend_model = 'straight-body'
lhc['mbw.b6l7.b2'].rbend_compensate_sagitta = False
lhc['mbw.b6l7.b2'].angle = lhc.ref['abw.b6l7']
lhc['mbw.b6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.b6l7']
lhc['mbw.b6l7.b2'].k0 = lhc.ref['kd34.lr7']
lhc['mbw.b6l7.b2'].rbend_shift = lhc.ref['shift.bw.b6l7']
lhc['mbw.b6l7.b2'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.b6l7']
lhc['mbw.b6l7.b2'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.b6l7']
lhc['mbw.b6l7.b2'].edge_entry_model = 'linear'
lhc['mbw.b6l7.b2'].edge_exit_model = 'linear'

lhc['mbw.c6l7.b1'].rbend_model = 'straight-body'
lhc['mbw.c6l7.b1'].rbend_compensate_sagitta = False
lhc['mbw.c6l7.b1'].angle = lhc.ref['abw.c6l7']
lhc['mbw.c6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.c6l7']
lhc['mbw.c6l7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.c6l7.b1'].rbend_shift = lhc.ref['shift.bw.c6l7']
lhc['mbw.c6l7.b1'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.c6l7']
lhc['mbw.c6l7.b1'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.c6l7']
lhc['mbw.c6l7.b1'].edge_entry_model = 'linear'
lhc['mbw.c6l7.b1'].edge_exit_model = 'linear'

lhc['mbw.c6l7.b2'].rbend_model = 'straight-body'
lhc['mbw.c6l7.b2'].rbend_compensate_sagitta = False
lhc['mbw.c6l7.b2'].angle = lhc.ref['abw.c6l7']
lhc['mbw.c6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.c6l7']
lhc['mbw.c6l7.b2'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.c6l7.b2'].rbend_shift = lhc.ref['shift.bw.c6l7']
lhc['mbw.c6l7.b2'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.c6l7']
lhc['mbw.c6l7.b2'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.c6l7']
lhc['mbw.c6l7.b2'].edge_entry_model = 'linear'
lhc['mbw.c6l7.b2'].edge_exit_model = 'linear'

lhc['mbw.d6l7.b1'].rbend_model = 'straight-body'
lhc['mbw.d6l7.b1'].rbend_compensate_sagitta = False
lhc['mbw.d6l7.b1'].angle = lhc.ref['abw.d6l7']
lhc['mbw.d6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.d6l7']
lhc['mbw.d6l7.b1'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.d6l7.b1'].rbend_shift = lhc.ref['shift.bw.d6l7']
lhc['mbw.d6l7.b1'].edge_entry_angle_fdown = lhc.ref['afd.arcside.bw.d6l7']
lhc['mbw.d6l7.b1'].edge_exit_angle_fdown = lhc.ref['afd.ipside.bw.d6l7']
lhc['mbw.d6l7.b1'].edge_entry_model = 'linear'
lhc['mbw.d6l7.b1'].edge_exit_model = 'linear'

lhc['mbw.d6l7.b2'].rbend_model = 'straight-body'
lhc['mbw.d6l7.b2'].rbend_compensate_sagitta = False
lhc['mbw.d6l7.b2'].angle = lhc.ref['abw.d6l7']
lhc['mbw.d6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.d6l7']
lhc['mbw.d6l7.b2'].k0 = -lhc.ref['kd34.lr7']
lhc['mbw.d6l7.b2'].rbend_shift = lhc.ref['shift.bw.d6l7']
lhc['mbw.d6l7.b2'].edge_entry_angle_fdown = lhc.ref['afd.ipside.bw.d6l7']
lhc['mbw.d6l7.b2'].edge_exit_angle_fdown = lhc.ref['afd.arcside.bw.d6l7']
lhc['mbw.d6l7.b2'].edge_entry_model = 'linear'
lhc['mbw.d6l7.b2'].edge_exit_model = 'linear'

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

sv_b1_ip7 = lhc.b1.survey(element0='ip7', X0=lhc['sep_ir7']/2)
sv_b2_ip7 = lhc.b2.survey(element0='ip7', X0=-lhc['sep_ir7']/2, theta0=np.pi)

tw_b1_ip7 = lhc.b1.twiss4d(init_at='ip7', betx=tw1['betx', 'ip7'], bety=tw1['bety', 'ip7'])
tw_b2_ip7 = lhc.b2.twiss4d(init_at='ip7', betx=tw2['betx', 'ip7'], bety=tw2['bety', 'ip7'])

trajectory_b1_ip7 = sv_b1_ip7.p0 + tw_b1_ip7.x[:, None] * sv_b1_ip7.ex + tw_b1_ip7.y[:, None] * sv_b1_ip7.ey
trajectory_b2_ip7 = sv_b2_ip7.p0 + tw_b2_ip7.x[:, None] * sv_b2_ip7.ex + tw_b2_ip7.y[:, None] * sv_b2_ip7.ey

import matplotlib.pyplot as plt
plt.close('all')
plt.figure(1)
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
plt.grid()
