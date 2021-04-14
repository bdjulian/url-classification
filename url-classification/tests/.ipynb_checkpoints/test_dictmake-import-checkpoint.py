import json
def test_dictmake():
    from the_functions import dict_make
    a_list = [1,2]
    my_dict = dict_make(a_list)
    
    assert len(my_dict) == len(a_list)