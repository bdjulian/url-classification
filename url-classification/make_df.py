import pandas as pd

def frame_maker(a_dict):
    df = pd.DataFrame(a_dict).T
    cols = ['job_id','avg_val_len', 'total_val_len','category_count','Artifacts dropped', 'External analysis', 'Network activity', 'Payload delivery', 'Payload installation', 'Persistence mechanism', 'filename|md5', 'user-agent', 'domain|ip', 'mutex', 'ip-dst', 'regkey|value', 'comment', 'filename|sha512', 'domain', 'filename|sha256', 'link', 'filename|sha1']
    df = df.reset_index()
    df.columns = cols
    
    return(df)
