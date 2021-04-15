import pandas as pd

def threat_score_extract(my_dict):
    a_dict = {}
    my_list = []
    for i in my_dict:
        try:
            for i in my_dict[i]['result']:
                try:
                    job_id = i['job_id']
                    my_list.append(i['threat_score'])
                    a_dict[job_id] = i['threat_score']
                except:
                    pass
        except:
            pass
    as_series = pd.Series(a_dict)
    return(as_series)