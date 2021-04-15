import requests
import json
import os
import sys
sys.path.append('..')
from the_functions import *
def test_search():
    assert len(search('2020-09-28 00:00', '2020-09-29 00:00', 5)) == 3