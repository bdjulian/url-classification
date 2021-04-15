import json
import os
import sys
sys.path.append('..')
from the_functions import *

def test_dictmake():
    from the_functions import dict_make
    a_list = [1,2]
    my_dict = dict_make(a_list)
    
    assert len(my_dict) == len(a_list)