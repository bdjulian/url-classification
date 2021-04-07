import pandas as pd
from target_extract import threat_score_extract


def frame_maker(dict_of_features, dict_make_dict):
    df = pd.DataFrame(dict_of_features).T
    cols = ['job_id','avg_val_len', 'total_val_len','category_count','Artifacts dropped', 'External analysis', 'Network activity', 'Payload delivery', 'Payload installation', 'Persistence mechanism', 'filename|md5', 'user-agent', 'domain|ip', 'mutex', 'ip-dst', 'regkey|value', 'comment', 'filename|sha512', 'domain', 'filename|sha256', 'link', 'filename|sha1']
    df = df.reset_index()
    df.columns = cols
    
    target = threat_score_extract(dict_make_dict)
    target.name = 'target'
    
    df = df.join(target, 'job_id')
    
    return(df)
