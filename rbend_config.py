
def config_rbend_ir15(lhc):

    # Adapt elements
    lhc['mbxf.4r5/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4r5/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4r5/b1'].angle = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].rbend_angle_diff = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].k0 = -lhc.ref['kd1.r5']
    lhc['mbxf.4r5/b1'].rbend_shift = -lhc.ref['sep_mid_d1.r5'] / 2
    lhc['mbxf.4r5/b1'].edge_entry_angle_fdown = 0
    lhc['mbxf.4r5/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4r5/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4r1/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4r1/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4r1/b1'].angle = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].rbend_angle_diff = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].k0 = -lhc.ref['kd1.r1']
    lhc['mbxf.4r1/b1'].rbend_shift = -lhc.ref['sep_mid_d1.r1'] / 2
    lhc['mbxf.4r1/b1'].edge_entry_angle_fdown = 0
    lhc['mbxf.4r1/b1'].edge_exit_angle_fdown = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4r1/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4l5/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4l5/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4l5/b1'].angle = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].rbend_angle_diff = -lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].k0 = lhc.ref['kd1.l5']
    lhc['mbxf.4l5/b1'].rbend_shift = lhc.ref['sep_mid_d1.l5'] / 2
    lhc['mbxf.4l5/b1'].edge_entry_angle_fdown = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b1'].edge_exit_angle_fdown = 0
    lhc['mbxf.4l5/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4l5/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4l1/b1'].rbend_model = 'straight-body'
    lhc['mbxf.4l1/b1'].rbend_compensate_sagitta = False
    lhc['mbxf.4l1/b1'].angle = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].rbend_angle_diff = -lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].k0 = lhc.ref['kd1.l1']
    lhc['mbxf.4l1/b1'].rbend_shift = lhc.ref['sep_mid_d1.l1'] / 2
    lhc['mbxf.4l1/b1'].edge_entry_angle_fdown = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b1'].edge_exit_angle_fdown = 0
    lhc['mbxf.4l1/b1'].edge_entry_model = 'linear'
    lhc['mbxf.4l1/b1'].edge_exit_model = 'linear'

    lhc['mbxf.4r5/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4r5/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4r5/b2'].angle = -lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].rbend_angle_diff = lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].k0 = -lhc.ref['kd1.r5']
    lhc['mbxf.4r5/b2'].rbend_shift = -lhc.ref['sep_mid_d1.r5'] / 2
    lhc['mbxf.4r5/b2'].edge_entry_angle_fdown = lhc.ref['ad1.r5']
    lhc['mbxf.4r5/b2'].edge_exit_angle_fdown = 0
    lhc['mbxf.4r5/b2'].edge_entry_model = 'linear'
    lhc['mbxf.4r5/b2'].edge_exit_model = 'linear'

    lhc['mbxf.4r1/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4r1/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4r1/b2'].angle = -lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].rbend_angle_diff = lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].k0 = -lhc.ref['kd1.r1']
    lhc['mbxf.4r1/b2'].rbend_shift = -lhc.ref['sep_mid_d1.r1'] / 2
    lhc['mbxf.4r1/b2'].edge_entry_angle_fdown = lhc.ref['ad1.r1']
    lhc['mbxf.4r1/b2'].edge_exit_angle_fdown = 0
    lhc['mbxf.4r1/b2'].edge_entry_model = 'linear'
    lhc['mbxf.4r1/b2'].edge_exit_model = 'linear'

    lhc['mbxf.4l5/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4l5/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4l5/b2'].angle = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b2'].rbend_angle_diff = lhc.ref['ad1.l5']
    lhc['mbxf.4l5/b2'].k0 = lhc.ref['kd1.l5']
    lhc['mbxf.4l5/b2'].rbend_shift = lhc.ref['sep_mid_d1.l5'] / 2
    lhc['mbxf.4l5/b2'].edge_entry_angle_fdown = 0
    lhc['mbxf.4l5/b2'].edge_exit_angle_fdown = lhc.ref['ad1.r5']
    lhc['mbxf.4l5/b2'].edge_entry_model = 'linear'
    lhc['mbxf.4l5/b2'].edge_exit_model = 'linear'

    lhc['mbxf.4l1/b2'].rbend_model = 'straight-body'
    lhc['mbxf.4l1/b2'].rbend_compensate_sagitta = False
    lhc['mbxf.4l1/b2'].angle = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b2'].rbend_angle_diff = lhc.ref['ad1.l1']
    lhc['mbxf.4l1/b2'].k0 = lhc.ref['kd1.l1']
    lhc['mbxf.4l1/b2'].rbend_shift = lhc.ref['sep_mid_d1.l1'] / 2
    lhc['mbxf.4l1/b2'].edge_entry_angle_fdown = 0
    lhc['mbxf.4l1/b2'].edge_exit_angle_fdown = lhc.ref['ad1.l1']

    lhc['mbrd.4r5.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4r5.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4r5.b1'].angle = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].rbend_angle_diff = -lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].k0 = lhc.ref['kd2.r5']
    lhc['mbrd.4r5.b1'].rbend_shift = -lhc.ref['shift_d2.r5']
    lhc['mbrd.4r5.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b1'].edge_exit_angle_fdown = 0
    lhc['mbrd.4r5.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4r5.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4r1.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4r1.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4r1.b1'].angle = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].rbend_angle_diff = -lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].k0 = lhc.ref['kd2.r1']
    lhc['mbrd.4r1.b1'].rbend_shift = -lhc.ref['shift_d2.r1']
    lhc['mbrd.4r1.b1'].edge_entry_angle_fdown = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b1'].edge_exit_angle_fdown = 0
    lhc['mbrd.4r1.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4r1.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4l5.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4l5.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4l5.b1'].angle = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b1'].rbend_angle_diff = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b1'].k0 = -lhc.ref['kd2.l5']
    lhc['mbrd.4l5.b1'].rbend_shift = lhc.ref['shift_d2.l5']
    lhc['mbrd.4l5.b1'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l5.b1'].edge_exit_angle_fdown = -lhc.ref['ad2.r5']
    lhc['mbrd.4l5.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4l5.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4l1.b1'].rbend_model = 'straight-body'
    lhc['mbrd.4l1.b1'].rbend_compensate_sagitta = False
    lhc['mbrd.4l1.b1'].angle = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].rbend_angle_diff = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].k0 = -lhc.ref['kd2.l1']
    lhc['mbrd.4l1.b1'].rbend_shift = lhc.ref['shift_d2.l1']
    lhc['mbrd.4l1.b1'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l1.b1'].edge_exit_angle_fdown = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b1'].edge_entry_model = 'linear'
    lhc['mbrd.4l1.b1'].edge_exit_model = 'linear'

    lhc['mbrd.4r5.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4r5.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4r5.b2'].angle = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].rbend_angle_diff = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].k0 = lhc.ref['kd2.r5']
    lhc['mbrd.4r5.b2'].rbend_shift = -lhc.ref['shift_d2.r5']
    lhc['mbrd.4r5.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4r5.b2'].edge_exit_angle_fdown = lhc.ref['ad2.r5']
    lhc['mbrd.4r5.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4r5.b2'].edge_exit_model = 'linear'

    lhc['mbrd.4r1.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4r1.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4r1.b2'].angle = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].rbend_angle_diff = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].k0 = lhc.ref['kd2.r1']
    lhc['mbrd.4r1.b2'].rbend_shift = -lhc.ref['shift_d2.r1']
    lhc['mbrd.4r1.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4r1.b2'].edge_exit_angle_fdown = lhc.ref['ad2.r1']
    lhc['mbrd.4r1.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4r1.b2'].edge_exit_model = 'linear'

    lhc['mbrd.4l5.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4l5.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4l5.b2'].angle = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].rbend_angle_diff = lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].k0 = -lhc.ref['kd2.l5']
    lhc['mbrd.4l5.b2'].rbend_shift = lhc.ref['shift_d2.l5']
    lhc['mbrd.4l5.b2'].edge_entry_angle_fdown = 0
    lhc['mbrd.4l5.b2'].edge_exit_angle_fdown = -lhc.ref['ad2.l5']
    lhc['mbrd.4l5.b2'].edge_entry_model = 'linear'
    lhc['mbrd.4l5.b2'].edge_exit_model = 'linear'

    lhc['mbrd.4l1.b2'].rbend_model = 'straight-body'
    lhc['mbrd.4l1.b2'].rbend_compensate_sagitta = False
    lhc['mbrd.4l1.b2'].angle = -lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].rbend_angle_diff = lhc.ref['ad2.l1']
    lhc['mbrd.4l1.b2'].k0 = -lhc.ref['kd2.l1']
    lhc['mbrd.4l1.b2'].rbend_shift = lhc.ref['shift_d2.l1']
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

def config_rbend_ir7(lhc):

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
