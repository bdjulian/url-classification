import requests
import json
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