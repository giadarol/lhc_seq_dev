import xtrack as xt
import rbend_config as rbc

fpath = './lhc.seq'

with open(fpath, 'r') as fid:
    seq_text = fid.read()

seq_text = seq_text.lower()

# Recover expressions in at arguments of the sequences
assert ' at=' in seq_text
assert ',at=' not in seq_text
assert 'at =' not in seq_text
seq_text = seq_text.replace(' at=', 'at:=')

# Rename sequences
assert 'LHCB1' not in seq_text
assert 'LHCB2' not in seq_text
seq_text = seq_text.replace('lhcb1', 'b1')
seq_text = seq_text.replace('lhcb2', 'b2')

lhc = xt.load(string=seq_text, format='madx', reverse_lines=['b2'], _rbend_correct_k0=True)

# Force k0_from_h to False (k0 are all provided)
for nn in list(lhc.elements.keys()):
    if hasattr(lhc.elements[nn], 'k0_from_h'):
        lhc.elements[nn].k0_from_h = False

lhc.to_json('_lhc_raw.json')

lhc.vars.load('rbend_config_ip1258.madx')
lhc.vars.load('rbend_config_ip3.madx')
lhc.vars.load('rbend_config_ip4.madx')
lhc.vars.load('rbend_config_ip7.madx')

rbc.config_rbend_ir15(lhc)
rbc.config_rbend_ir28(lhc)
rbc.config_rbend_ir3(lhc)
rbc.config_rbend_ir4(lhc)
rbc.config_rbend_ir7(lhc)

lhc.to_json('lhc.json')
