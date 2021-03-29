import json
def dict_make(dates_from):
    my_dict = {}
    for i in range(len(dates_from)):
        with open(f'data/data{i}.txt') as json_file:
            my_dict[i] = json.load(json_file)
    return(my_dict)

def test_dictmake():
    a_list = [1,2]
    my_dict = dict_make(a_list)
    
    assert len(my_dict) == len(a_list)