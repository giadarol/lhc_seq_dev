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

# Patch triplet
lhc.vars.load(string='''
kqx.l1             := kqx2a.l1           ;
ktqx1.l1           := kqx1.l1-kqx2a.l1   ;
ktqx3.l1           := kqx3.l1-kqx2a.l1   ;
kqx.r1             := kqx2a.r1           ;
ktqx1.r1           := kqx1.r1-kqx2a.r1   ;
ktqx3.r1           := kqx3.r1-kqx2a.r1   ;
kqx.l5             := kqx2a.l5           ;
ktqx1.l5           := kqx1.l5-kqx2a.l5   ;
ktqx3.l5           := kqx3.l5-kqx2a.l5   ;
kqx.r5             := kqx2a.r5           ;
ktqx1.r5           := kqx1.r5-kqx2a.r5   ;
ktqx3.r5           := kqx3.r5-kqx2a.r5   ;
''', format='madx')

# Rename lines
lhc.lines['b1'] = lhc.lines['lhcb1']
lhc.lines['b2'] = lhc.lines['lhcb2']
del lhc.lines['lhcb1']
del lhc.lines['lhcb2']

# Force k0_from_h to False (k0 are all provided)
for nn in list(lhc.elements.keys()):
    if hasattr(lhc.elements[nn], 'k0_from_h'):
        lhc.elements[nn].k0_from_h = False

lhc.to_json('lhc.json')
# lpg.write_py_lattice_file(lhc, output_fname='lhc_seq.py')