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