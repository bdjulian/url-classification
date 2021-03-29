# url-classification
Project for URL classification attempting to replicate Hybrid Analysis threat
score using regression. Unique feature engineering is done on reports gathered from their dynamic testing suite Falcon Sandbox.
functions and their uses:

I had serious issues with whitespace indentation and syntax stuff trying to do
(1) store multiple functions in a .py and (2) add docstrings, so for now all docstring-esque explanations
of functions will be here.

search_query.py  
search(date_from, date_to, verdict):
This function uses the requests package to make a POST request to the Hybrid Analysis API.
It uses a single date window so iterate a list of dates you want.
date format is 'yyyy-mm-dd HH:MM', verdict is 1-5: Available options: 1 'whitelisted', 2 'no verdict', 3 'no specific threat', 4 'suspicious', 5 'malicious
the filetype is restricted to URL in the function.

search_write_to_file(dates_from, dates_to) - passes the date lists to search_query and gets the returns that contain the threat scores, then saves them as dataX

dict_make(dates_from) - makes a combined dictionary of all downloaded data files from using search_and_write. Dates_from is
not utilized for any reason other than establishing a correct
range of numbers to use in the loop.

job_id_extract(my_dict) - loops through the dictionary created by dict_make to append the job_id to a list. Will pass on failed or missing job_id's

report_get - the GET request used in report_write
uses curl and requests to retrieve feature information on URL's
aquired through search_query.

report_write - takes the job_id list extracted from job_id_extract and queries hybrid_analysis for the report that contains features
