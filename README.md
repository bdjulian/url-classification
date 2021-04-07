# url-classification
Project for URL classification attempting to replicate Hybrid Analysis threat
score using regression. Unique feature engineering is done on reports gathered from their dynamic testing suite Falcon Sandbox.
functions and their uses:

I had serious issues with whitespace indentation and syntax stuff trying to do
(1) store multiple functions in a .py and (2) add docstrings, so for now all docstring-esque explanations
of functions will be here.

## Function Explanations

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


## General project flow

Building the project for yourself is particularly easy _please don't submit a lot of api requests_ my api key is currently embeded in all the relevant functions
so please don't cap me out, I also intentionally sleep the functions so I don't break their server. If you'd like to get the reports and the data for yourself delete the contents of both 'data' and 'reports'- The un-commented date ranges found in the notebook are big enough to have the code function. If you don't care to collect the data yourself you can just clone this repo and run my notebook, otherwise start at step 1. _FYI most functions do not share the name of their .py file, please inspect each to see the real name of the function._


### Step 1

The first step is to use search_and_write.py to submit POST requests to Hybrid-Analysis.com. Use the provided date range as the input into the function, the function has no saveable output, it will just grab the data in JSON format and save it to your 'data' directory. The data contained in this JSON file is relatively unimportant, what is important are the 'job_id' and the 'threat_score'. The 'job_id' will be utilized later to obtain feature information for each job. And the 'threat_score' will be the target variable when it comes time for our regression predictions. Each job is also a single URL (typically).

### Step 2

Now that we have the data that contains the 'job_id' - use dict_make.py to combine each item from your 'data' directory into a single dictionary. Save the output.

### Step 3

Use job_id_extract.py on your dictionary to get each 'job_id' and save it to a list, these will now be used to obtain feature information for each collected URL.

### Step 4

Time to use report_get_write.py to take your list of job_id's and retreive each job/url's features. This function will submit GET requests for each job_id passed. There is no saved output, it will save the results into your reports directory.

### Step 5

Now pass the list from job_id_extract.py to feature_extract.py to get a dictionary that has jobs as keys and basic features as values. Save the output.

### Step 6

Pass this dictionary to make_df.py and save the output as this is the final dataframe. Using the code and date range provided it should have 159 rows and 22 columns - 1 of which is the target.

### Step 7

Now you have a complete sample dataset to experiment with as you please. A simple ML analysis is located in my .ipynb notebook.