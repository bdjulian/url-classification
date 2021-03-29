import json
def job_id_extract(my_dict):
    my_list = []
    for i in my_dict:
        try:
            for i in my_dict[i]['result']:
                try:
                    my_list.append(i['job_id'])
                except:
                    pass
        except:
            pass
    return(my_list)


# def job_id_extract(a_dict):
#     list = []
#     for i in a_dict:
#         list.append(a_dict[i]['result'][i]['job_id'])
        
#     return(list)
dates_from = ['2020-09-28 00:00', '2020-09-29 00:00']
def dict_make(dates_from):
    my_dict = {}
    for i in range(len(dates_from)):
        with open(f'data/data{i}.txt') as json_file:
            my_dict[i] = json.load(json_file)
    return(my_dict)

def test_jobidextract():
    my_dict = dict_make(dates_from)
    my_list = job_id_extract(my_dict)
    
    errors = []
    if len(my_list) != 4:
        errors.append('missing job IDs')
    if my_list[0] not in '5f72774a50643e7bc7460603':
        errors.append('incorrect job IDs')
    assert not errors, "errors occured:\n{}".format("\n".join(errors))