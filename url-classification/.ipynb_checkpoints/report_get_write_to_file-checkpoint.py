import json
import time
from report_get import report
def report_write(job_list):
    for i in job_list:
        rep = report(i)
        with open(f'reports/reports{i}.txt', 'w') as outfile:
            json.dump(rep, outfile)
        time.sleep(5)