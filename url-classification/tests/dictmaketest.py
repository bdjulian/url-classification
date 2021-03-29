import sys
import FailedTest
from FailedTest import ErrorFailedTest
sys.path.append('../')
import json
from dict_make import dict_make

a_list = [1,2]
my_dict = dict_make(a_list)

if len(my_dict) != len(a_list):
    raise ErrorFailedTest("failed test")
else:
    print('Test Successful')