#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import re
import sys
sys.path.append("../tools/")
from feature_format import featureFormat
from feature_format import targetFeatureSplit

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Number of people in enron dataset:", len(enron_data)
max_cnt = 0
for key,val in enron_data.items():
  count = 0
  for i in val:
    count = count + 1
  if max_cnt < count:
    max_cnt = count
print "Number of features for each person:", max_cnt
poi_count = 0

poi_nan_count = 0
poi_list = []

"""
feature_list = ["poi", "total_payments"] 
data_array = featureFormat( enron_data, feature_list )
label, features = targetFeatureSplit(data_array)
print label
print features
"""

for k, v in enron_data.items():
  for key, val in v.items():
    if key == "poi" and val:
      poi_count = poi_count + 1
      poi_list.append(k)
print "Number of poi in our dataset:", poi_count
print "List of POIs::", poi_list

for i in poi_list:
  for k,v in enron_data.items():
    if k == i:
      for key, val in v.items():
        if key == 'total_payments' and val == 'NaN':
          poi_nan_count = poi_nan_count + 1
print "Number of POIs having total_payments as NaN is::", poi_nan_count

sal_count = 0
email_count = 0
nan_count = 0
for k, v in enron_data.items():
  match = re.search(r'JAMES',k)
  if match:
    name = re.search(r'PRENTICE', k)
    if name:
      print k
      for key, val in v.items():
        if key == 'total_stock_value':
          print "Total stock value of",k,"is",val
  match2 = re.search(r'WESLEY', k)
  if match2:
    name2 = re.search(r'COLWELL', k)
    if name2:
      print k
      for key, val in v.items():
        if key == 'from_this_person_to_poi':
          print 'Total number of emails from',k,'to poi ::',val
  match3 = re.search(r'JEFFREY',k)
  if match3:
    name3 = re.search(r'SKILLING', k)
    if name3:
      print k
      for key, val in v.items():
        if key == 'exercised_stock_options':
          print "Stock options exercised by %s is %d" % (k,val)
  match = re.search(r'KENNETH',k)
  if match:
    name = re.search(r'LAY', k)
    if name:
      print k
      print v
  match = re.search(r'JEFFREY',k) 
  if match:
    name = re.search(r'SKILLING', k)
    if name:
      print k
      print v
  match = re.search(r'ANDREW',k)
  if match:
    name = re.search(r'FASTOW', k)
    if name:
      print k
      print v
  for key,val in v.items():
    if key == 'total_payments' and val == 'NaN':
      nan_count = nan_count + 1
    if key == 'salary' and val != 'NaN':
      sal_count = sal_count + 1
    if key == 'email_address' and val != 'NaN':
      email_count = email_count + 1
print "Number of people with quantified salary is::",sal_count
print "Number of people with a known email address is::",email_count
print "Number of people with NaN total_payments is::",nan_count
print "Percentage of NaN total_payments is::",nan_count*100/len(enron_data)
