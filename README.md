# url-classification
Project for URL classification as malicious or benign using a combination of static and dynamic features

functions and their uses:

I had serious  issues with whitespace indentation and syntax stuff trying to do
(1) store multiple functions in a .py and (2) add docstrings, so for now all docstring-esque explanations
of functions will be here.

search_query.py  
search(date_from, date_to, verdict):
This function uses the requests package to make a POST request to the Hybrid Analysis API.
It uses a single date window so iterate a list of dates you want.
date format is 'yyyy-mm-dd HH:MM', verdict is 1-5: Available options: 1 'whitelisted', 2 'no verdict', 3 'no specific threat', 4 'suspicious', 5 'malicious
the filetype is restricted to URL in the function.
