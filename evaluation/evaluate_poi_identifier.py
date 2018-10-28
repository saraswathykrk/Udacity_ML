#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)


### your code goes here 
from time import time
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
t0 = time()
clf.fit(features_train, labels_train)
print "Training time :", round(time() - t0,3), "s"
t0 = time()
pred = clf.predict(features_test)
print "Testing time :", round(time() - t0,3), "s"
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred,labels_test)
print "Accuracy is:" , acc

poi_cnt = 0
for i in labels_test:
  if i == 1:
    poi_cnt = poi_cnt + 1
print "Total number of pois in test set::", poi_cnt
print "Total number of people in test set::", len(features_test)

new_pred = [0.0, 0.0 , 0.0 ,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0 , 0.0,0.0, 0.0]
print accuracy_score(labels_test, new_pred)
print new_pred
print pred
print labels_test
print "New accuracy = Total labelled correctly/total num of items:: 25/29 =",float(round(25/29,6))



#printing precision score and recall score
from sklearn.metrics import precision_score, recall_score

print precision_score(labels_test,pred)
print recall_score(pred,labels_test)


