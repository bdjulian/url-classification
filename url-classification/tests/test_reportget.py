#proper getrequest from HA, looks like simple URL hacking is possible?
#     '''job_id will be inserted into a URL that is passed, job_id should be a string, this is the one that returns a possible feature dictionary'''
import requests
import json
import os
import sys
sys.path.append('..')
from the_functions import *
def test_report():
    rep = report("5f9a05839fb71b523c1a2b59")
    assert len(rep['response']['Event']['Attribute']) == 535