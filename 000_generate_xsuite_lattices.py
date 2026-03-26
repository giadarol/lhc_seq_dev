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

env = xt.load(string=seq_text, format='madx', reverse_lines=['lhcb2'], _rbend_correct_k0=True)

# Rename lines
env.lines['b1'] = env.lines['lhcb1']
env.lines['b2'] = env.lines['lhcb2']
del env.lines['lhcb1']
del env.lines['lhcb2']

# Force k0_from_h to False (k0 are all provided)
for nn in list(env.elements.keys()):
    if hasattr(env.elements[nn], 'k0_from_h'):
        env.elements[nn].k0_from_h = False

env.to_json('lhc.json')
# lpg.write_py_lattice_file(env, output_fname='lhc_seq.py')