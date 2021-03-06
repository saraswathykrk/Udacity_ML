#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split #cross_validation
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

#print features_train

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]


### your code goes here
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
fimp = clf.feature_importances_

for i in range(0,len(fimp)):
  if fimp[i] > 0.2:
    print i, fimp[i]
    index = i

name = vectorizer.get_feature_names()
for i in range(0,len(name)):
  if i == index:
    print name[i]


pred = clf.predict(features_test)

#print features_train
#for i in features_train:
#  if clf.feature_importances_[i] > 0.2:
#    print clf.feature_importances_[i]

print len(features_train)

from sklearn.metrics import accuracy_score
print accuracy_score(labels_test,pred)


