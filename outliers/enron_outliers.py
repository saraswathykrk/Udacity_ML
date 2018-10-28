#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot as plt
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)

#print data_dict

boo1 = False
for k,v in data_dict.items():
  boo1 = False
  for key,val in v.items():
    #if key == 'salary' and val > 20000000:
    #  print k,key,val
    if key == 'salary' and val > 1000000 and val != 'NaN':
      boo1 = True
    if key == 'bonus' and val >= 5000000 and val != 'NaN' and boo1:
      print k, key, val
### your code below
for point in data:
  salary = point[0]
  bonus = point[1]
  #if salary > 20000000:
  #  print salary, bonus
  plt.scatter( salary, bonus )

plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()
