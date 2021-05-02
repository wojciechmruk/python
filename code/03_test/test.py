"""
# This is small, handy function for the purpose of testing
# other functions while learning Python.

# Example

from test import *


def test_yes_man(arg):
    if arg == 'Yes': return True
    if arg == 'Yes Sir': return True
    return False


args = {"Yes": True, "Yes Sir" : True, "No": False} # Create arguments
test(test_yes_man, args)
"""

# Provide function and arguments
def test(function, args):
    for k, v in args.items():
        result = function(k)
        if result == v:
            print("K: {0}\t\t\t RESULT: {1} [OK]".format(str(k), str(result)))
        else:
            print("K: {0}\t\t\t RESULT: {1} [NOT OK]".format(str(k), str(result)))
