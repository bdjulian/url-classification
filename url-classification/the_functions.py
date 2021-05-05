import pandas as pd
import time
import json
import requests

def dict_make(dates_from):
    my_dict = {}
    for i in range(len(dates_from)):
        with open(f'data/data{i}.txt') as json_file:
            my_dict[i] = json.load(json_file)
    return(my_dict)

# can open all files in reports - this will become my core feature extraction

a_dict = {}
category_list = ['Artifacts dropped', 'External analysis', 'Network activity', 'Payload delivery', 'Payload installation', 'Persistence mechanism']
types_list = ['filename|md5', 'user-agent', 'domain|ip', 'mutex', 'ip-dst', 'regkey|value', 'comment', 'filename|sha512', 'domain', 'filename|sha256', 'link', 'filename|sha1']
def feature_extraction(my_list):
    for i in my_list:
        try:
            with open(f'reports/reports{i}.txt') as json_file:
                features = []
                job_id = i
                x = json.load(json_file)
#                 print(i)
                #avg length of attribute vlaues
                lenRep = len(x['response']['Event']['Attribute'])
                list_of_lengths = []
                sum = 0

                for i in x['response']['Event']['Attribute']:
                    list_of_lengths.append(i['value'])
                for i in list_of_lengths:
                    sum += len(i)
                avg_len = (sum/lenRep)

                features.append(avg_len)


                # total length of attribute values
                list_of_lengths = []
                sum = 0

                for i in x['response']['Event']['Attribute']:
                    list_of_lengths.append(i['value'])
                for i in list_of_lengths:
                    sum += len(i)

                features.append(sum)

                # count of categories
                list = []
                for i in x['response']['Event']['Attribute']:
                    list.append(i['category'])
                len_list = len(list)

                features.append(len_list)

                # one hotting categories
                cats = []
                for i in x['response']['Event']['Attribute']:
                    cats.append(i['category'])
                cats = set(cats)
                for i in category_list:
                    if i in cats:
                        features.append(1)
                    else:
                        features.append(0)

                types = []
                for i in x['response']['Event']['Attribute']:
                    types.append(i['type'])
                types = set(types)
                for i in types_list:
                    if i in types:
                        features.append(1)
                    else:
                        features.append(0)

                frequencies = {'External analysis': 0, 'Payload delivery': 0, 'Network activity': 0, 'Payload installation': 0, 'Persistence mechanism': 0, 'Artifacts dropped': 0}
                for i in x['response']['Event']['Attribute']:
                    if i['category'] in frequencies:
                        frequencies[i['category']] += 1
                    else:
                        frequencies[i['category']] = 0
                for i in frequencies.values():
                        features.append(i)
    # 'EA_count', 'PD_count', 'NA_count', 'PI_count', 'PM_count', 'AD_count'


                a_dict[f'{job_id}'] = features
        except:
            pass
    return(a_dict)

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

def frame_maker(dict_of_features, dict_make_dict):
    df = pd.DataFrame(dict_of_features).T
    cols = ['job_id','avg_val_len', 'total_val_len','category_count','Artifacts dropped', 'External analysis', 'Network activity', 'Payload delivery', 'Payload installation', 'Persistence mechanism', 'filename|md5', 'user-agent', 'domain|ip', 'mutex', 'ip-dst', 'regkey|value', 'comment', 'filename|sha512', 'domain', 'filename|sha256', 'link', 'filename|sha1', 'EA_count', 'PD_count', 'NA_count', 'PI_count', 'PM_count', 'AD_count']
    df = df.reset_index()
    df.columns = cols

    target = threat_score_extract(dict_make_dict)
    target.name = 'target'

    df = df.join(target, 'job_id')

    return(df)

def report_write(job_list):
    for i in job_list:
        rep = report(i)
        with open(f'reports/reports{i}.txt', 'w') as outfile:
            json.dump(rep, outfile)
        time.sleep(5)

#proper getrequest from HA, looks like simple URL hacking is possible?
#     '''job_id will be inserted into a URL that is passed, job_id should be a string, this is the one that returns a possible feature dictionary'''

import json
def report(job_id):
    url = f"https://www.hybrid-analysis.com/api/v2/report/{job_id}/report/misp-json?_timestamp=1614629473094"
    headers = {'api-key': 'zcxpuuhp272a1e1bvcq18bg46bd2d94609x2l9xv1eef8812c5pu6hmi9a438676', 'user-agent': 'Falcon Sandbox', 'accept': 'application/json', 'accept-encoding': 'gzip'}

    r = requests.get(url, headers=headers)

    report = json.loads(r.text)

    return(report)

def search(date_from, date_to, verdict):
    url = "https://www.hybrid-analysis.com/api/v2/search/terms?_timestamp=1614630850155"
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'api-key': 'zcxpuuhp272a1e1bvcq18bg46bd2d94609x2l9xv1eef8812c5pu6hmi9a438676', 'user-agent': 'Falcon Sandbox', 'accept': 'application/json'}
    payload = {
        'filetype': 'url',
        'env_id': 100,
        'verdict': verdict,
        'date_from': date_from,
        'date_to': date_to,
    }
    r = requests.post(url, data=payload, headers=headers)

    data = r.json()

    return(data)


def search_and_write(dates_from, dates_to):
    for i in range(len(dates_from)):
        data = search(dates_from[i], dates_to[i], 5)
        with open(f'data/data{i}.txt', 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(2)

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
