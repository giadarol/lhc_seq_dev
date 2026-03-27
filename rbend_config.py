
def config_rbend_ir15(lhc):

    # Adapt elements
    lhc['mbxf.4r5/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4r5/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4r5/b1'].angle = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].rbend_angle_diff = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].k0 = -lhc.ref['kd1.r5']
    lhc['mbxf.4r5/b1'].rbend_shift = lhc.ref['sep_mid_d1.r5'] / 2
    lhc['mbxf.4r5/b1'].edge_entry_angle_fdown = 0
    lhc['mbxf.4r5/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4r5/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4r1/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4r1/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4r1/b1'].angle = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].rbend_angle_diff = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].k0 = -lhc.ref['kd1.r1']
    lhc['mbxf.4r1/b1'].rbend_shift = lhc.ref['sep_mid_d1.r1'] / 2
    lhc['mbxf.4r1/b1'].edge_entry_angle_fdown = 0
    lhc['mbxf.4r1/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4r1/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4l5/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4l5/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4l5/b1'].angle = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].rbend_angle_diff = -lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].k0 = lhc.ref['kd1.l5']
    lhc['mbxf.4l5/b1'].rbend_shift = -lhc.ref['sep_mid_d1.l5'] / 2
    lhc['mbxf.4l5/b1'].edge_entry_angle_fdown = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].edge_exit_angle_fdown = 0
    lhc['mbxf.4l5/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4l5/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4l1/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4l1/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4l1/b1'].angle = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].rbend_angle_diff = -lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].k0 = lhc.ref['kd1.l1']
    lhc['mbxf.4l1/b1'].rbend_shift = -lhc.ref['sep_mid_d1.l1'] / 2
    lhc['mbxf.4l1/b1'].edge_entry_angle_fdown = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].edge_exit_angle_fdown = 0
    lhc['mbxf.4l1/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4l1/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4r5/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4r5/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4r5/b2'].angle = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].rbend_angle_diff = lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].k0 = -lhc.ref['kd1.r5']
    lhc['mbxf.4r5/b2'].rbend_shift = lhc.ref['sep_mid_d1.r5'] / 2
    lhc['mbxf.4r5/b2'].edge_entry_angle_fdown = lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].edge_exit_angle_fdown = 0
    lhc['mbxf.4r5/b2'].edge_entry_model = 'linear'
    lhc['mbxf.4r5/b2'].edge_exit_model = 'linear'

    lhc['mbxf.4r1/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4r1/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4r1/b2'].angle = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].rbend_angle_diff = lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].k0 = -lhc.ref['kd1.r1']
    lhc['mbxf.4r1/b2'].rbend_shift = lhc.ref['sep_mid_d1.r1'] / 2
    lhc['mbxf.4r1/b2'].edge_entry_angle_fdown = lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].edge_exit_angle_fdown = 0
    lhc['mbxf.4r1/b2'].edge_entry_model = 'linear'
    lhc['mbxf.4r1/b2'].edge_exit_model = 'linear'

    lhc['mbxf.4l5/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4l5/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4l5/b2'].angle = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b2'].rbend_angle_diff = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b2'].k0 = lhc.ref['kd1.l5']
    lhc['mbxf.4l5/b2'].rbend_shift = -lhc.ref['sep_mid_d1.l5'] / 2
    lhc['mbxf.4l5/b2'].edge_entry_angle_fdown = 0
    lhc['mbxf.4l5/b2'].edge_exit_angle_fdown = lhc.ref['ad1.r5']
    lhc['mbxf.4l5/b2'].edge_entry_model = 'linear'
    lhc['mbxf.4l5/b2'].edge_exit_model = 'linear'

    lhc['mbxf.4l1/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4l1/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4l1/b2'].angle = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b2'].rbend_angle_diff = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b2'].k0 = lhc.ref['kd1.l1']
    lhc['mbxf.4l1/b2'].rbend_shift = -lhc.ref['sep_mid_d1.l1'] / 2
    lhc['mbxf.4l1/b2'].edge_entry_angle_fdown = 0
    lhc['mbxf.4l1/b2'].edge_exit_angle_fdown = lhc.ref['ad1.l1']

    lhc['mbrd.4r5.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4r5.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4r5.b1'].angle = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].rbend_angle_diff = -lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].k0 = lhc.ref['kd2.r5']
    lhc['mbrd.4r5.b1'].rbend_shift = lhc.ref['shift_d2.r5']
    lhc['mbrd.4r5.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].edge_exit_angle_fdown = 0
    lhc['mbrd.4r5.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4r5.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4r1.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4r1.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4r1.b1'].angle = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].rbend_angle_diff = -lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].k0 = lhc.ref['kd2.r1']
    lhc['mbrd.4r1.b1'].rbend_shift = lhc.ref['shift_d2.r1']
    lhc['mbrd.4r1.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].edge_exit_angle_fdown = 0
    lhc['mbrd.4r1.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4r1.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4l5.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4l5.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4l5.b1'].angle = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b1'].rbend_angle_diff = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b1'].k0 = -lhc.ref['kd2.l5']
    lhc['mbrd.4l5.b1'].rbend_shift = -lhc.ref['shift_d2.l5']
    lhc['mbrd.4l5.b1'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l5.b1'].edge_exit_angle_fdown = -lhc.ref['ad2.r5']
    lhc['mbrd.4l5.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4l5.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4l1.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4l1.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4l1.b1'].angle = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].rbend_angle_diff = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].k0 = -lhc.ref['kd2.l1']
    lhc['mbrd.4l1.b1'].rbend_shift = -lhc.ref['shift_d2.l1']
    lhc['mbrd.4l1.b1'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l1.b1'].edge_exit_angle_fdown = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4l1.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4r5.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4r5.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4r5.b2'].angle = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].rbend_angle_diff = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].k0 = lhc.ref['kd2.r5']
    lhc['mbrd.4r5.b2'].rbend_shift = lhc.ref['shift_d2.r5']
    lhc['mbrd.4r5.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4r5.b2'].edge_exit_angle_fdown = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4r5.b2'].edge_exit_model = 'linear'

    lhc['mbrd.4r1.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4r1.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4r1.b2'].angle = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].rbend_angle_diff = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].k0 = lhc.ref['kd2.r1']
    lhc['mbrd.4r1.b2'].rbend_shift = lhc.ref['shift_d2.r1']
    lhc['mbrd.4r1.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4r1.b2'].edge_exit_angle_fdown = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4r1.b2'].edge_exit_model = 'linear'

    lhc['mbrd.4l5.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4l5.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4l5.b2'].angle = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].rbend_angle_diff = lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].k0 = -lhc.ref['kd2.l5']
    lhc['mbrd.4l5.b2'].rbend_shift = -lhc.ref['shift_d2.l5']
    lhc['mbrd.4l5.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l5.b2'].edge_exit_angle_fdown = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4l5.b2'].edge_exit_model = 'linear'

    lhc['mbrd.4l1.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4l1.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4l1.b2'].angle = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].rbend_angle_diff = lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].k0 = -lhc.ref['kd2.l1']
    lhc['mbrd.4l1.b2'].rbend_shift = -lhc.ref['shift_d2.l1']
    lhc['mbrd.4l1.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l1.b2'].edge_exit_angle_fdown = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4l1.b2'].edge_exit_model = 'linear'

def config_rbend_ir28(lhc):

    # Adapt elements
    lhc['mbx.4r2/b1'].rbend_model = 'straight-body'
    lhc['mbx.4r2/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4r2/b1'].angle = lhc.ref['ad1.r2']
    lhc['mbx.4r2/b1'].rbend_angle_diff = lhc.ref['ad1.r2']
    lhc['mbx.4r2/b1'].k0 = lhc.ref['kd1.r2']
    lhc['mbx.4r2/b1'].rbend_shift = lhc.ref['sep_mid_d1.r2'] / 2
    lhc['mbx.4r2/b1'].edge_entry_angle_fdown = 0
    lhc['mbx.4r2/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r2']
    lhc['mbx.4r2/b1'].edge_entry_model = 'linear'
    lhc['mbx.4r2/b1'].edge_exit_model = 'linear'

    lhc['mbx.4r2/b2'].rbend_model = 'straight-body'
    lhc['mbx.4r2/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4r2/b2'].angle = lhc.ref['ad1.r2']
    lhc['mbx.4r2/b2'].rbend_angle_diff = -lhc.ref['ad1.r2']
    lhc['mbx.4r2/b2'].k0 = lhc.ref['kd1.r2']
    lhc['mbx.4r2/b2'].rbend_shift = lhc.ref['sep_mid_d1.r2'] / 2
    lhc['mbx.4r2/b2'].edge_entry_angle_fdown = -lhc.ref['ad1.r2']
    lhc['mbx.4r2/b2'].edge_exit_angle_fdown = 0
    lhc['mbx.4r2/b2'].edge_entry_model = 'linear'
    lhc['mbx.4r2/b2'].edge_exit_model = 'linear'

    lhc['mbx.4l2/b1'].rbend_model = 'straight-body'
    lhc['mbx.4l2/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4l2/b1'].angle = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b1'].rbend_angle_diff = lhc.ref['ad1.l2']
    lhc['mbx.4l2/b1'].k0 = -lhc.ref['kd1.l2']
    lhc['mbx.4l2/b1'].rbend_shift = -lhc.ref['sep_mid_d1.l2'] / 2
    lhc['mbx.4l2/b1'].edge_entry_angle_fdown = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b1'].edge_exit_angle_fdown = 0
    lhc['mbx.4l2/b1'].edge_entry_model = 'linear'
    lhc['mbx.4l2/b1'].edge_exit_model = 'linear'

    lhc['mbx.4l2/b2'].rbend_model = 'straight-body'
    lhc['mbx.4l2/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4l2/b2'].angle = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b2'].rbend_angle_diff = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b2'].k0 = -lhc.ref['kd1.l2']
    lhc['mbx.4l2/b2'].rbend_shift = -lhc.ref['sep_mid_d1.l2'] / 2
    lhc['mbx.4l2/b2'].edge_entry_angle_fdown = 0
    lhc['mbx.4l2/b2'].edge_exit_angle_fdown = -lhc.ref['ad1.l2']
    lhc['mbx.4l2/b2'].edge_entry_model = 'linear'
    lhc['mbx.4l2/b2'].edge_exit_model = 'linear'

    lhc['mbx.4r8/b1'].rbend_model = 'straight-body'
    lhc['mbx.4r8/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4r8/b1'].angle = lhc.ref['ad1.r8']
    lhc['mbx.4r8/b1'].rbend_angle_diff = lhc.ref['ad1.r8']
    lhc['mbx.4r8/b1'].k0 = lhc.ref['kd1.r8']
    lhc['mbx.4r8/b1'].rbend_shift = lhc.ref['sep_mid_d1.r8'] / 2
    lhc['mbx.4r8/b1'].edge_entry_angle_fdown = 0
    lhc['mbx.4r8/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r8']
    lhc['mbx.4r8/b1'].edge_entry_model = 'linear'
    lhc['mbx.4r8/b1'].edge_exit_model = 'linear'

    lhc['mbx.4r8/b2'].rbend_model = 'straight-body'
    lhc['mbx.4r8/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4r8/b2'].angle = lhc.ref['ad1.r8']
    lhc['mbx.4r8/b2'].rbend_angle_diff = -lhc.ref['ad1.r8']
    lhc['mbx.4r8/b2'].k0 = lhc.ref['kd1.r8']
    lhc['mbx.4r8/b2'].rbend_shift = lhc.ref['sep_mid_d1.r8'] / 2
    lhc['mbx.4r8/b2'].edge_entry_angle_fdown = -lhc.ref['ad1.r8']
    lhc['mbx.4r8/b2'].edge_exit_angle_fdown = 0
    lhc['mbx.4r8/b2'].edge_entry_model = 'linear'
    lhc['mbx.4r8/b2'].edge_exit_model = 'linear'

    lhc['mbx.4l8/b1'].rbend_model = 'straight-body'
    lhc['mbx.4l8/b1'].rbend_compensate_sagitta = False
    lhc['mbx.4l8/b1'].angle = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b1'].rbend_angle_diff = lhc.ref['ad1.l8']
    lhc['mbx.4l8/b1'].k0 = -lhc.ref['kd1.l8']
    lhc['mbx.4l8/b1'].rbend_shift = -lhc.ref['sep_mid_d1.l8'] / 2
    lhc['mbx.4l8/b1'].edge_entry_angle_fdown = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b1'].edge_exit_angle_fdown = 0
    lhc['mbx.4l8/b1'].edge_entry_model = 'linear'
    lhc['mbx.4l8/b1'].edge_exit_model = 'linear'

    lhc['mbx.4l8/b2'].rbend_model = 'straight-body'
    lhc['mbx.4l8/b2'].rbend_compensate_sagitta = False
    lhc['mbx.4l8/b2'].angle = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b2'].rbend_angle_diff = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b2'].k0 = -lhc.ref['kd1.l8']
    lhc['mbx.4l8/b2'].rbend_shift = -lhc.ref['sep_mid_d1.l8'] / 2
    lhc['mbx.4l8/b2'].edge_entry_angle_fdown = 0
    lhc['mbx.4l8/b2'].edge_exit_angle_fdown = -lhc.ref['ad1.l8']
    lhc['mbx.4l8/b2'].edge_entry_model = 'linear'
    lhc['mbx.4l8/b2'].edge_exit_model = 'linear'

    lhc['mbrc.4r2.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4r2.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4r2.b1'].angle = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b1'].rbend_angle_diff = lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b1'].k0 = -lhc.ref['kd2.r2']
    lhc['mbrc.4r2.b1'].rbend_shift = lhc.ref['shift_d2.r2']
    lhc['mbrc.4r2.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b1'].edge_exit_angle_fdown = 0
    lhc['mbrc.4r2.b1'].edge_entry_model = 'linear'
    lhc['mbrc.4r2.b1'].edge_exit_model = 'linear'

    lhc['mbrc.4r8.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4r8.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4r8.b1'].angle = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b1'].rbend_angle_diff = lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b1'].k0 = -lhc.ref['kd2.r8']
    lhc['mbrc.4r8.b1'].rbend_shift = lhc.ref['shift_d2.r8']
    lhc['mbrc.4r8.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b1'].edge_exit_angle_fdown = 0
    lhc['mbrc.4r8.b1'].edge_entry_model = 'linear'
    lhc['mbrc.4r8.b1'].edge_exit_model = 'linear'

    lhc['mbrc.4r2.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4r2.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4r2.b2'].angle = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b2'].rbend_angle_diff = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b2'].k0 = -lhc.ref['kd2.r2']
    lhc['mbrc.4r2.b2'].rbend_shift = lhc.ref['shift_d2.r2']
    lhc['mbrc.4r2.b2'].edge_entry_angle_fdown = 0
    lhc['mbrc.4r2.b2'].edge_exit_angle_fdown = -lhc.ref['ad2.r2']
    lhc['mbrc.4r2.b2'].edge_entry_model = 'linear'
    lhc['mbrc.4r2.b2'].edge_exit_model = 'linear'

    lhc['mbrc.4r8.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4r8.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4r8.b2'].angle = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b2'].rbend_angle_diff = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b2'].k0 = -lhc.ref['kd2.r8']
    lhc['mbrc.4r8.b2'].rbend_shift = lhc.ref['shift_d2.r8']
    lhc['mbrc.4r8.b2'].edge_entry_angle_fdown = 0
    lhc['mbrc.4r8.b2'].edge_exit_angle_fdown = -lhc.ref['ad2.r8']
    lhc['mbrc.4r8.b2'].edge_entry_model = 'linear'
    lhc['mbrc.4r8.b2'].edge_exit_model = 'linear'

    lhc['mbrc.4l2.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4l2.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4l2.b1'].angle = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b1'].rbend_angle_diff = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b1'].k0 = lhc.ref['kd2.l2']
    lhc['mbrc.4l2.b1'].rbend_shift = -lhc.ref['shift_d2.l2']
    lhc['mbrc.4l2.b1'].edge_entry_angle_fdown = 0
    lhc['mbrc.4l2.b1'].edge_exit_angle_fdown = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b1'].edge_entry_model = 'linear'
    lhc['mbrc.4l2.b1'].edge_exit_model = 'linear'

    lhc['mbrc.4l8.b1'].rbend_model = 'straight-body'
    lhc['mbrc.4l8.b1'].rbend_compensate_sagitta = False
    lhc['mbrc.4l8.b1'].angle = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b1'].rbend_angle_diff = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b1'].k0 = lhc.ref['kd2.l8']
    lhc['mbrc.4l8.b1'].rbend_shift = -lhc.ref['shift_d2.l8']
    lhc['mbrc.4l8.b1'].edge_entry_angle_fdown = 0
    lhc['mbrc.4l8.b1'].edge_exit_angle_fdown = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b1'].edge_entry_model = 'linear'
    lhc['mbrc.4l8.b1'].edge_exit_model = 'linear'

    lhc['mbrc.4l2.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4l2.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4l2.b2'].angle = lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b2'].rbend_angle_diff = -lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b2'].k0 = lhc.ref['kd2.l2']
    lhc['mbrc.4l2.b2'].rbend_shift = -lhc.ref['shift_d2.l2']
    lhc['mbrc.4l2.b2'].edge_entry_angle_fdown = -lhc.ref['ad2.l2']
    lhc['mbrc.4l2.b2'].edge_exit_angle_fdown = 0
    lhc['mbrc.4l2.b2'].edge_entry_model = 'linear'
    lhc['mbrc.4l2.b2'].edge_exit_model = 'linear'

    lhc['mbrc.4l8.b2'].rbend_model = 'straight-body'
    lhc['mbrc.4l8.b2'].rbend_compensate_sagitta = False
    lhc['mbrc.4l8.b2'].angle = lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b2'].rbend_angle_diff = -lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b2'].k0 = lhc.ref['kd2.l8']
    lhc['mbrc.4l8.b2'].rbend_shift = -lhc.ref['shift_d2.l8']
    lhc['mbrc.4l8.b2'].edge_entry_angle_fdown = -lhc.ref['ad2.l8']
    lhc['mbrc.4l8.b2'].edge_exit_angle_fdown = 0
    lhc['mbrc.4l8.b2'].edge_entry_model = 'linear'
    lhc['mbrc.4l8.b2'].edge_exit_model = 'linear'