
def config_rbend_ir15(lhc):

    # Adapt elements
    lhc['mbxf.4r5/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4r5/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4r5/b1'].angle = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].rbend_angle_diff = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].k0 = -lhc.ref['kd1.r5']
    lhc['mbxf.4r5/b1'].rbend_shift = -lhc.ref['sep_mid_d1.r5'] / 2

    lhc['mbxf.4r1/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4r1/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4r1/b1'].angle = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].rbend_angle_diff = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].k0 = -lhc.ref['kd1.r1']
    lhc['mbxf.4r1/b1'].rbend_shift = -lhc.ref['sep_mid_d1.r1'] / 2

    lhc['mbxf.4l5/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4l5/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4l5/b1'].angle = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].rbend_angle_diff = -lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].k0 = lhc.ref['kd1.l5']
    lhc['mbxf.4l5/b1'].rbend_shift = lhc.ref['sep_mid_d1.l5'] / 2

    lhc['mbxf.4l1/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4l1/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4l1/b1'].angle = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].rbend_angle_diff = -lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].k0 = lhc.ref['kd1.l1']
    lhc['mbxf.4l1/b1'].rbend_shift = lhc.ref['sep_mid_d1.l1'] / 2

    lhc['mbxf.4r5/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4r5/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4r5/b2'].angle = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].rbend_angle_diff = lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].k0 = -lhc.ref['kd1.r5']
    lhc['mbxf.4r5/b2'].rbend_shift = -lhc.ref['sep_mid_d1.r5'] / 2

    lhc['mbxf.4r1/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4r1/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4r1/b2'].angle = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].rbend_angle_diff = lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].k0 = -lhc.ref['kd1.r1']
    lhc['mbxf.4r1/b2'].rbend_shift = -lhc.ref['sep_mid_d1.r1'] / 2

    lhc['mbxf.4l5/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4l5/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4l5/b2'].angle = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b2'].rbend_angle_diff = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b2'].k0 = lhc.ref['kd1.l5']
    lhc['mbxf.4l5/b2'].rbend_shift = lhc.ref['sep_mid_d1.l5'] / 2

    lhc['mbxf.4l1/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4l1/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4l1/b2'].angle = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b2'].rbend_angle_diff = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b2'].k0 = lhc.ref['kd1.l1']
    lhc['mbxf.4l1/b2'].rbend_shift = lhc.ref['sep_mid_d1.l1'] / 2

    lhc['mbrd.4r5.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4r5.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4r5.b1'].angle = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].rbend_angle_diff = -lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].k0 = lhc.ref['kd2.r5']
    lhc['mbrd.4r5.b1'].rbend_shift = -lhc.ref['shift_d2.r5']

    lhc['mbrd.4r1.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4r1.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4r1.b1'].angle = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].rbend_angle_diff = -lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].k0 = lhc.ref['kd2.r1']
    lhc['mbrd.4r1.b1'].rbend_shift = -lhc.ref['shift_d2.r1']

    lhc['mbrd.4l5.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4l5.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4l5.b1'].angle = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b1'].rbend_angle_diff = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b1'].k0 = -lhc.ref['kd2.l5']
    lhc['mbrd.4l5.b1'].rbend_shift = lhc.ref['shift_d2.l5']

    lhc['mbrd.4l1.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4l1.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4l1.b1'].angle = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].rbend_angle_diff = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].k0 = -lhc.ref['kd2.l1']
    lhc['mbrd.4l1.b1'].rbend_shift = lhc.ref['shift_d2.l1']

    lhc['mbrd.4r5.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4r5.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4r5.b2'].angle = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].rbend_angle_diff = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].k0 = lhc.ref['kd2.r5']
    lhc['mbrd.4r5.b2'].rbend_shift = -lhc.ref['shift_d2.r5']

    lhc['mbrd.4r1.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4r1.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4r1.b2'].angle = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].rbend_angle_diff = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].k0 = lhc.ref['kd2.r1']
    lhc['mbrd.4r1.b2'].rbend_shift = -lhc.ref['shift_d2.r1']

    lhc['mbrd.4l5.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4l5.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4l5.b2'].angle = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].rbend_angle_diff = lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].k0 = -lhc.ref['kd2.l5']
    lhc['mbrd.4l5.b2'].rbend_shift = lhc.ref['shift_d2.l5']

    lhc['mbrd.4l1.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4l1.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4l1.b2'].angle = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].rbend_angle_diff = lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].k0 = -lhc.ref['kd2.l1']
    lhc['mbrd.4l1.b2'].rbend_shift = lhc.ref['shift_d2.l1']

def config_rbend_ir28(lhc):

    # Adapt elements
    lhc['mbx.4r2/b1'].rbend_model = 'straight-body'
    lhc['mbx.4r2/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4r2/b1'].angle = lhc.ref['ad1.r2']
    lhc['mbx.4r2/b1'].rbend_angle_diff = lhc.ref['ad1.r2']
    lhc['mbx.4r2/b1'].k0 = lhc.ref['kd1.r2']
    lhc['mbx.4r2/b1'].rbend_shift = lhc.ref['sep_mid_d1.r2'] / 2

    lhc['mbx.4r2/b2'].rbend_model = 'straight-body'
    lhc['mbx.4r2/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4r2/b2'].angle = lhc.ref['ad1.r2']
    lhc['mbx.4r2/b2'].rbend_angle_diff = -lhc.ref['ad1.r2']
    lhc['mbx.4r2/b2'].k0 = lhc.ref['kd1.r2']
    lhc['mbx.4r2/b2'].rbend_shift = lhc.ref['sep_mid_d1.r2'] / 2

    lhc['mbx.4l2/b1'].rbend_model = 'straight-body'
    lhc['mbx.4l2/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4l2/b1'].angle = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b1'].rbend_angle_diff = lhc.ref['ad1.l2']
    lhc['mbx.4l2/b1'].k0 = -lhc.ref['kd1.l2']
    lhc['mbx.4l2/b1'].rbend_shift = -lhc.ref['sep_mid_d1.l2'] / 2

    lhc['mbx.4l2/b2'].rbend_model = 'straight-body'
    lhc['mbx.4l2/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4l2/b2'].angle = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b2'].rbend_angle_diff = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b2'].k0 = -lhc.ref['kd1.l2']
    lhc['mbx.4l2/b2'].rbend_shift = -lhc.ref['sep_mid_d1.l2'] / 2

    lhc['mbx.4r8/b1'].rbend_model = 'straight-body'
    lhc['mbx.4r8/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4r8/b1'].angle = lhc.ref['ad1.r8']
    lhc['mbx.4r8/b1'].rbend_angle_diff = lhc.ref['ad1.r8']
    lhc['mbx.4r8/b1'].k0 = lhc.ref['kd1.r8']
    lhc['mbx.4r8/b1'].rbend_shift = lhc.ref['sep_mid_d1.r8'] / 2

    lhc['mbx.4r8/b2'].rbend_model = 'straight-body'
    lhc['mbx.4r8/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4r8/b2'].angle = lhc.ref['ad1.r8']
    lhc['mbx.4r8/b2'].rbend_angle_diff = -lhc.ref['ad1.r8']
    lhc['mbx.4r8/b2'].k0 = lhc.ref['kd1.r8']
    lhc['mbx.4r8/b2'].rbend_shift = lhc.ref['sep_mid_d1.r8'] / 2

    lhc['mbx.4l8/b1'].rbend_model = 'straight-body'
    lhc['mbx.4l8/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4l8/b1'].angle = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b1'].rbend_angle_diff = lhc.ref['ad1.l8']
    lhc['mbx.4l8/b1'].k0 = -lhc.ref['kd1.l8']
    lhc['mbx.4l8/b1'].rbend_shift = -lhc.ref['sep_mid_d1.l8'] / 2

    lhc['mbx.4l8/b2'].rbend_model = 'straight-body'
    lhc['mbx.4l8/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4l8/b2'].angle = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b2'].rbend_angle_diff = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b2'].k0 = -lhc.ref['kd1.l8']
    lhc['mbx.4l8/b2'].rbend_shift = -lhc.ref['sep_mid_d1.l8'] / 2

    lhc['mbrc.4r2.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4r2.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4r2.b1'].angle = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b1'].rbend_angle_diff = lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b1'].k0 = -lhc.ref['kd2.r2']
    lhc['mbrc.4r2.b1'].rbend_shift = lhc.ref['shift_d2.r2']

    lhc['mbrc.4r8.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4r8.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4r8.b1'].angle = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b1'].rbend_angle_diff = lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b1'].k0 = -lhc.ref['kd2.r8']
    lhc['mbrc.4r8.b1'].rbend_shift = lhc.ref['shift_d2.r8']

    lhc['mbrc.4r2.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4r2.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4r2.b2'].angle = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b2'].rbend_angle_diff = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b2'].k0 = -lhc.ref['kd2.r2']
    lhc['mbrc.4r2.b2'].rbend_shift = lhc.ref['shift_d2.r2']

    lhc['mbrc.4r8.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4r8.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4r8.b2'].angle = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b2'].rbend_angle_diff = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b2'].k0 = -lhc.ref['kd2.r8']
    lhc['mbrc.4r8.b2'].rbend_shift = lhc.ref['shift_d2.r8']

    lhc['mbrc.4l2.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4l2.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4l2.b1'].angle = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b1'].rbend_angle_diff = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b1'].k0 = lhc.ref['kd2.l2']
    lhc['mbrc.4l2.b1'].rbend_shift = -lhc.ref['shift_d2.l2']

    lhc['mbrc.4l8.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4l8.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4l8.b1'].angle = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b1'].rbend_angle_diff = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b1'].k0 = lhc.ref['kd2.l8']
    lhc['mbrc.4l8.b1'].rbend_shift = -lhc.ref['shift_d2.l8']

    lhc['mbrc.4l2.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4l2.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4l2.b2'].angle = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b2'].rbend_angle_diff = -lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b2'].k0 = lhc.ref['kd2.l2']
    lhc['mbrc.4l2.b2'].rbend_shift = -lhc.ref['shift_d2.l2']

    lhc['mbrc.4l8.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4l8.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4l8.b2'].angle = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b2'].rbend_angle_diff = -lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b2'].k0 = lhc.ref['kd2.l8']
    lhc['mbrc.4l8.b2'].rbend_shift = -lhc.ref['shift_d2.l8']

def config_rbend_ir7(lhc):

    lhc['mbw.a6r7.b1'].rbend_model = 'straight-body'
    lhc['mbw.a6r7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.a6r7.b1'].angle = lhc.ref['abw.a6r7']
    lhc['mbw.a6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.a6r7']
    lhc['mbw.a6r7.b1'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.a6r7.b1'].rbend_shift = -lhc.ref['shift.bw.a6r7']

    lhc['mbw.a6r7.b2'].rbend_model = 'straight-body'
    lhc['mbw.a6r7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.a6r7.b2'].angle = lhc.ref['abw.a6r7']
    lhc['mbw.a6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.a6r7']
    lhc['mbw.a6r7.b2'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.a6r7.b2'].rbend_shift = -lhc.ref['shift.bw.a6r7']

    lhc['mbw.b6r7.b1'].rbend_model = 'straight-body'
    lhc['mbw.b6r7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.b6r7.b1'].angle = lhc.ref['abw.b6r7']
    lhc['mbw.b6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.b6r7']
    lhc['mbw.b6r7.b1'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.b6r7.b1'].rbend_shift = -lhc.ref['shift.bw.b6r7']

    lhc['mbw.b6r7.b2'].rbend_model = 'straight-body'
    lhc['mbw.b6r7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.b6r7.b2'].angle = lhc.ref['abw.b6r7']
    lhc['mbw.b6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.b6r7']
    lhc['mbw.b6r7.b2'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.b6r7.b2'].rbend_shift = -lhc.ref['shift.bw.b6r7']

    lhc['mbw.c6r7.b1'].rbend_model = 'straight-body'
    lhc['mbw.c6r7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.c6r7.b1'].angle = lhc.ref['abw.c6r7']
    lhc['mbw.c6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.c6r7']
    lhc['mbw.c6r7.b1'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.c6r7.b1'].rbend_shift = -lhc.ref['shift.bw.c6r7']

    lhc['mbw.c6r7.b2'].rbend_model = 'straight-body'
    lhc['mbw.c6r7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.c6r7.b2'].angle = lhc.ref['abw.c6r7']
    lhc['mbw.c6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.c6r7']
    lhc['mbw.c6r7.b2'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.c6r7.b2'].rbend_shift = -lhc.ref['shift.bw.c6r7']

    lhc['mbw.d6r7.b1'].rbend_model = 'straight-body'
    lhc['mbw.d6r7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.d6r7.b1'].angle = lhc.ref['abw.d6r7']
    lhc['mbw.d6r7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.d6r7']
    lhc['mbw.d6r7.b1'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.d6r7.b1'].rbend_shift = -lhc.ref['shift.bw.d6r7']

    lhc['mbw.d6r7.b2'].rbend_model = 'straight-body'
    lhc['mbw.d6r7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.d6r7.b2'].angle = lhc.ref['abw.d6r7']
    lhc['mbw.d6r7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.d6r7']
    lhc['mbw.d6r7.b2'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.d6r7.b2'].rbend_shift = -lhc.ref['shift.bw.d6r7']

    lhc['mbw.a6l7.b1'].rbend_model = 'straight-body'
    lhc['mbw.a6l7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.a6l7.b1'].angle = lhc.ref['abw.a6l7']
    lhc['mbw.a6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.a6l7']
    lhc['mbw.a6l7.b1'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.a6l7.b1'].rbend_shift = -lhc.ref['shift.bw.a6l7']

    lhc['mbw.a6l7.b2'].rbend_model = 'straight-body'
    lhc['mbw.a6l7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.a6l7.b2'].angle = lhc.ref['abw.a6l7']
    lhc['mbw.a6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.a6l7']
    lhc['mbw.a6l7.b2'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.a6l7.b2'].rbend_shift = -lhc.ref['shift.bw.a6l7']

    lhc['mbw.b6l7.b1'].rbend_model = 'straight-body'
    lhc['mbw.b6l7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.b6l7.b1'].angle = lhc.ref['abw.b6l7']
    lhc['mbw.b6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.b6l7']
    lhc['mbw.b6l7.b1'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.b6l7.b1'].rbend_shift = -lhc.ref['shift.bw.b6l7']

    lhc['mbw.b6l7.b2'].rbend_model = 'straight-body'
    lhc['mbw.b6l7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.b6l7.b2'].angle = lhc.ref['abw.b6l7']
    lhc['mbw.b6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.b6l7']
    lhc['mbw.b6l7.b2'].k0 = lhc.ref['kd34.lr7']
    lhc['mbw.b6l7.b2'].rbend_shift = -lhc.ref['shift.bw.b6l7']

    lhc['mbw.c6l7.b1'].rbend_model = 'straight-body'
    lhc['mbw.c6l7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.c6l7.b1'].angle = lhc.ref['abw.c6l7']
    lhc['mbw.c6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.c6l7']
    lhc['mbw.c6l7.b1'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.c6l7.b1'].rbend_shift = -lhc.ref['shift.bw.c6l7']

    lhc['mbw.c6l7.b2'].rbend_model = 'straight-body'
    lhc['mbw.c6l7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.c6l7.b2'].angle = lhc.ref['abw.c6l7']
    lhc['mbw.c6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.c6l7']
    lhc['mbw.c6l7.b2'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.c6l7.b2'].rbend_shift = -lhc.ref['shift.bw.c6l7']

    lhc['mbw.d6l7.b1'].rbend_model = 'straight-body'
    lhc['mbw.d6l7.b1'].rbend_compensate_sagitta = False
    lhc['mbw.d6l7.b1'].angle = lhc.ref['abw.d6l7']
    lhc['mbw.d6l7.b1'].rbend_angle_diff = lhc.ref['adiff.bw.d6l7']
    lhc['mbw.d6l7.b1'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.d6l7.b1'].rbend_shift = -lhc.ref['shift.bw.d6l7']

    lhc['mbw.d6l7.b2'].rbend_model = 'straight-body'
    lhc['mbw.d6l7.b2'].rbend_compensate_sagitta = False
    lhc['mbw.d6l7.b2'].angle = lhc.ref['abw.d6l7']
    lhc['mbw.d6l7.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.d6l7']
    lhc['mbw.d6l7.b2'].k0 = -lhc.ref['kd34.lr7']
    lhc['mbw.d6l7.b2'].rbend_shift = -lhc.ref['shift.bw.d6l7']

def config_rbend_ir3(lhc):

    for mm in ['a', 'b', 'c', 'd', 'e', 'f']:
        pol = -1 if mm in ['a', 'b', 'c'] else 1
        lhc['mbw.'+mm+'6r3.b1'].rbend_model = 'straight-body'
        lhc['mbw.'+mm+'6r3.b1'].rbend_compensate_sagitta = False
        lhc['mbw.'+mm+'6r3.b1'].angle = lhc.ref['abw.'+mm+'6r3']
        lhc['mbw.'+mm+'6r3.b1'].rbend_angle_diff = lhc.ref['adiff.bw.'+mm+'6r3']
        lhc['mbw.'+mm+'6r3.b1'].k0 = pol * lhc.ref['kd34.lr3']
        lhc['mbw.'+mm+'6r3.b1'].rbend_shift = lhc.ref['shift.bw.'+mm+'6r3']

        lhc['mbw.'+mm+'6r3.b2'].rbend_model = 'straight-body'
        lhc['mbw.'+mm+'6r3.b2'].rbend_compensate_sagitta = False
        lhc['mbw.'+mm+'6r3.b2'].angle = lhc.ref['abw.'+mm+'6r3']
        lhc['mbw.'+mm+'6r3.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.'+mm+'6r3']
        lhc['mbw.'+mm+'6r3.b2'].k0 = pol * lhc.ref['kd34.lr3']
        lhc['mbw.'+mm+'6r3.b2'].rbend_shift = lhc.ref['shift.bw.'+mm+'6r3']

    for mm in ['a', 'b', 'c', 'd', 'e', 'f']:
        pol = -1 if mm in ['a', 'b', 'c'] else 1
        lhc['mbw.'+mm+'6l3.b1'].rbend_model = 'straight-body'
        lhc['mbw.'+mm+'6l3.b1'].rbend_compensate_sagitta = False
        lhc['mbw.'+mm+'6l3.b1'].angle = lhc.ref['abw.'+mm+'6l3']
        lhc['mbw.'+mm+'6l3.b1'].rbend_angle_diff = lhc.ref['adiff.bw.'+mm+'6l3']
        lhc['mbw.'+mm+'6l3.b1'].k0 = pol * lhc.ref['kd34.lr3']
        lhc['mbw.'+mm+'6l3.b1'].rbend_shift = lhc.ref['shift.bw.'+mm+'6l3']

        lhc['mbw.'+mm+'6l3.b2'].rbend_model = 'straight-body'
        lhc['mbw.'+mm+'6l3.b2'].rbend_compensate_sagitta = False
        lhc['mbw.'+mm+'6l3.b2'].angle = lhc.ref['abw.'+mm+'6l3']
        lhc['mbw.'+mm+'6l3.b2'].rbend_angle_diff = -lhc.ref['adiff.bw.'+mm+'6l3']
        lhc['mbw.'+mm+'6l3.b2'].k0 = pol * lhc.ref['kd34.lr3']
        lhc['mbw.'+mm+'6l3.b2'].rbend_shift = lhc.ref['shift.bw.'+mm+'6l3']

def config_rbend_ir4(lhc):
    lhc['mbrs.5r4.b1'].rbend_model = 'straight-body'
    lhc['mbrs.5r4.b1'].rbend_compensate_sagitta = False
    lhc['mbrs.5r4.b1'].angle = -lhc['ad3.r4']
    lhc['mbrs.5r4.b1'].rbend_angle_diff = -lhc['ad3.r4']
    lhc['mbrs.5r4.b1'].k0 = -lhc.ref['kd3.r4']
    lhc['mbrs.5r4.b1'].rbend_shift = lhc['shift.mbrs.r4']

    lhc['mbrs.5r4.b2'].rbend_model = 'straight-body'
    lhc['mbrs.5r4.b2'].rbend_compensate_sagitta = False
    lhc['mbrs.5r4.b2'].angle = -lhc['ad3.r4']
    lhc['mbrs.5r4.b2'].rbend_angle_diff = lhc['ad3.r4']
    lhc['mbrs.5r4.b2'].k0 = -lhc.ref['kd3.r4']
    lhc['mbrs.5r4.b2'].rbend_shift = lhc['shift.mbrs.r4']

    lhc['mbrb.5r4.b1'].rbend_model = 'straight-body'
    lhc['mbrb.5r4.b1'].rbend_compensate_sagitta = False
    lhc['mbrb.5r4.b1'].angle = lhc['ad4.r4']
    lhc['mbrb.5r4.b1'].rbend_angle_diff = -lhc['ad4.r4']
    lhc['mbrb.5r4.b1'].k0 = lhc.ref['kd4.r4']
    lhc['mbrb.5r4.b1'].rbend_shift = lhc['shift.mbrb.r4']

    lhc['mbrb.5r4.b2'].rbend_model = 'straight-body'
    lhc['mbrb.5r4.b2'].rbend_compensate_sagitta = False
    lhc['mbrb.5r4.b2'].angle = lhc['ad4.r4']
    lhc['mbrb.5r4.b2'].rbend_angle_diff = lhc['ad4.r4']
    lhc['mbrb.5r4.b2'].k0 = lhc.ref['kd4.r4']
    lhc['mbrb.5r4.b2'].rbend_shift = lhc['shift.mbrb.r4']

    lhc['mbrs.5l4.b1'].rbend_model = 'straight-body'
    lhc['mbrs.5l4.b1'].rbend_compensate_sagitta = False
    lhc['mbrs.5l4.b1'].angle = -lhc['ad3.l4']
    lhc['mbrs.5l4.b1'].rbend_angle_diff = lhc['ad3.l4']
    lhc['mbrs.5l4.b1'].k0 = -lhc.ref['kd3.l4']
    lhc['mbrs.5l4.b1'].rbend_shift = lhc['shift.mbrs.l4']

    lhc['mbrs.5l4.b2'].rbend_model = 'straight-body'
    lhc['mbrs.5l4.b2'].rbend_compensate_sagitta = False
    lhc['mbrs.5l4.b2'].angle = -lhc['ad3.l4']
    lhc['mbrs.5l4.b2'].rbend_angle_diff = -lhc['ad3.l4']
    lhc['mbrs.5l4.b2'].k0 = -lhc.ref['kd3.l4']
    lhc['mbrs.5l4.b2'].rbend_shift = lhc['shift.mbrs.l4']

    lhc['mbrb.5l4.b1'].rbend_model = 'straight-body'
    lhc['mbrb.5l4.b1'].rbend_compensate_sagitta = False
    lhc['mbrb.5l4.b1'].angle = lhc['ad4.l4']
    lhc['mbrb.5l4.b1'].rbend_angle_diff = lhc['ad4.l4']
    lhc['mbrb.5l4.b1'].k0 = lhc.ref['kd4.l4']
    lhc['mbrb.5l4.b1'].rbend_shift = lhc['shift.mbrb.l4']

    lhc['mbrb.5l4.b2'].rbend_model = 'straight-body'
    lhc['mbrb.5l4.b2'].rbend_compensate_sagitta = False
    lhc['mbrb.5l4.b2'].angle = lhc['ad4.l4']
    lhc['mbrb.5l4.b2'].rbend_angle_diff = -lhc['ad4.l4']
    lhc['mbrb.5l4.b2'].k0 = lhc.ref['kd4.l4']
    lhc['mbrb.5l4.b2'].rbend_shift = lhc['shift.mbrb.l4']