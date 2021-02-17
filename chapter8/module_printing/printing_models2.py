# from printing_models1 import*

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

from printing_models1 import print_models as pm
from printing_models1 import show_completed_models as pmc

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
pm(unprinted_designs, completed_models)
pmc(completed_models)
