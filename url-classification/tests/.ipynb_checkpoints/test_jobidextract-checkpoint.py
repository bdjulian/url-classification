import json
import os
import sys
sys.path.append('..')
from the_functions import *
dates_from = ['2020-09-28 00:00', '2020-09-29 00:00']

def test_jobidextract():
    my_dict = dict_make(dates_from)
    my_list = job_id_extract(my_dict)
    
    errors = []
    if len(my_list) != 4:
        errors.append('missing job IDs')
    if my_list[0] not in '5f72774a50643e7bc7460603':
        errors.append('incorrect job IDs')
    assert not errors, "errors occured:\n{}".format("\n".join(errors))