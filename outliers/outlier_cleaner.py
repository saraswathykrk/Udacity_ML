#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    def func(s):
      #print s[-1]
      return s[-1]

    cleaned_data = []

    ### your code goes here
    percent = (1-0.1)*len(ages)
    count = 0
    temp_list = []
    print percent
    for ind in range(0,len(ages)):
      tup = ()
      error = (net_worths[ind] - predictions[ind])**2
      #print ages[ind], net_worths[ind], error
      tup = (ages[ind][0], net_worths[ind][0], error[0])
      #print tup
      temp_list.append(tup)
    #print sorted(temp_list,key = func)     
    for i in sorted(temp_list,key = func):
      if count < percent:
        cleaned_data.append(i)
        count += 1 
    #print cleaned_data
    return cleaned_data

