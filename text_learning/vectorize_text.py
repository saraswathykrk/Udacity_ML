#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
            temp_counter += 1
        #if temp_counter < 5200:
            path = os.path.join('..', path[:-1])
            #print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            text = parseOutText(email)
            #print text
            

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            if text.find("sara"):
              new_text = text.replace("sara","")
            else:
              new_text = text
            if new_text.find("shackleton"):
              new_text1 = new_text.replace("shackleton","")
            else:
              new_text1 = new_text
            if new_text1.find("chris"):
              new_text2 = new_text1.replace("chris","")
            else:
              new_text2 = new_text1
            if new_text2.find("sshacklensf"):
              new_text3= new_text2.replace("sshacklensf","")
            else:
              new_text3 = new_text2
            if new_text3.find("germani"):
              new_text4= new_text3.replace("germani","")
            else:
              new_text4 = new_text3
            if new_text4.find("germani"):
              new_text5= new_text4.replace("cgermannsf","")
            else:
              new_text5 = new_text4

            ### append the text to word_data
            word_data.append(new_text5)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
              from_data.append(0)
            else:
              from_data.append(1)

            email.close()

#print from_data
print word_data[152]
print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )





### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english',max_df = 0.7)
X = vectorizer.fit_transform(word_data)
#print X
#print X[34597]
Y = vectorizer.get_feature_names()
print Y[34597]
print Y[34596]
print Y[34598]
print len(vectorizer.get_feature_names())
