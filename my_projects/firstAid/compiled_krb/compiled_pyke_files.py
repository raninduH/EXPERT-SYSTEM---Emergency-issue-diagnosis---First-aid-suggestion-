# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'bc.krb'):
           [1733381895.348166, 'bc_bc.py'],
         ('', '', 'facts.kfb'):
           [1733381895.4011135, 'facts.fbc'],
         ('', '', 'fc.krb'):
           [1733381895.653898, 'fc_fc.py'],
         ('', '', 'questions.kqb'):
           [1733381895.694358, 'questions.qbc'],
        },
        compiler_version)

