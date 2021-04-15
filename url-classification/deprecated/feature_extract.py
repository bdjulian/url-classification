# can open all files in reports - this will become my core feature extraction
import json
a_dict = {}
category_list = ['Artifacts dropped', 'External analysis', 'Network activity', 'Payload delivery', 'Payload installation', 'Persistence mechanism']
types_list = ['filename|md5', 'user-agent', 'domain|ip', 'mutex', 'ip-dst', 'regkey|value', 'comment', 'filename|sha512', 'domain', 'filename|sha256', 'link', 'filename|sha1']
def feature_extraction(my_list):
    for i in my_list:
        with open(f'reports/reports{i}.txt') as json_file:
            features = []
            job_id = i
            x = json.load(json_file)


            #acg length of attribute vlaues
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


            a_dict[f'{job_id}'] = features
    return(a_dict)