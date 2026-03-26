import xtrack as xt
from xtrack._temp.python_lattice_writer import lattice_py_generation as lpg

fpath = './lhc.seq'

with open(fpath, 'r') as fid:
    seq_text = fid.read()

# Recover expressions in at arguments of the sequences
assert ' at=' in seq_text
assert ',at=' not in seq_text
assert 'at =' not in seq_text
seq_text = seq_text.replace(' at=', 'at:=')

lhc = xt.load(string=seq_text, format='madx', reverse_lines=['lhcb2'], _rbend_correct_k0=True)

# Rename lines
lhc.lines['b1'] = lhc.lines['lhcb1']
lhc.lines['b2'] = lhc.lines['lhcb2']
del lhc.lines['lhcb1']
del lhc.lines['lhcb2']

# Rename elements
for bname in ['b1', 'b2']:
    tt = lhc[bname].get_table()
    tt_to_rename = tt.rows['.*/lhc'+bname]
    for nn in tt_to_rename.name:
        new_name = nn.replace('/lhc'+bname, '/'+bname)
        lhc.new(new_name, nn)
        lhc[bname].replace(nn, new_name)
        del lhc.elements[nn]

# Force k0_from_h to False (k0 are all provided)
for nn in list(lhc.elements.keys()):
    if hasattr(lhc.elements[nn], 'k0_from_h'):
        lhc.elements[nn].k0_from_h = False

lhc.to_json('lhc.json')
# lpg.write_py_lattice_file(lhc, output_fname='lhc_seq.py')