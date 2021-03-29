#proper getrequest from HA, looks like simple URL hacking is possible?
#     '''job_id will be inserted into a URL that is passed, job_id should be a string, this is the one that returns a possible feature dictionary'''
import requests
import json
def report(job_id):
    url = f"https://www.hybrid-analysis.com/api/v2/report/{job_id}/report/misp-json?_timestamp=1614629473094"
    headers = {'api-key': 'zcxpuuhp272a1e1bvcq18bg46bd2d94609x2l9xv1eef8812c5pu6hmi9a438676', 'user-agent': 'Falcon Sandbox', 'accept': 'application/json', 'accept-encoding': 'gzip'}
    
    r = requests.get(url, headers=headers)
    
    report = json.loads(r.text)
    
    return(report)

def test_report():
    rep = report("5f9a05839fb71b523c1a2b59")
    assert len(rep['response']['Event']['Attribute']) == 535