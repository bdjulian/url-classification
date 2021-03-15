def job_id_extract(data):
    list = []
    for i in data['result']:
        list.append(i['job_id'])
        
    return(list)