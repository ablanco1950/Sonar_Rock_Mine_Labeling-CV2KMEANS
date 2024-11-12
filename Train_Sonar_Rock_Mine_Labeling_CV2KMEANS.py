
#importing the libraries

import numpy as np
import pandas as pd
     
#Importing the data set and exploring the data

dataset = pd.read_csv('sonar_data.csv', header = None)
     

#print(dataset.head())

#print(dataset.shape)
     
#(208, 61)

#print(dataset.describe())

#print(dataset.iloc[:, 60].value_counts())

#print(dataset.groupby(60).mean())

X = dataset.iloc[:, :-1].values
#print(X.shape)
y = dataset.iloc[:, -1].values

#print(y)

import cv2

# https://medium.com/@vamshidharpratap/implementing-k-means-clustering-using-opencv-in-python-bd466b146568

#Define the stopping criteria and number of clusters
# stop after 10 iterations or when EPS(change in cluster centers) is less than 0.2
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.2)


k = 2 # number of clusters, one for mine other for rock


#print(X.shape)

# USE HISTOGRAM OF SIGNAL
counts, X = np.histogram(X, np.array(range(0, X.shape[0])))

#print(X.shape)
#https://stackoverflow.com/questions/40567816/cv2-kmeans-error-with-parameters-python
#retval, labels, centers = cv2.kmeans(np.float32(X), k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
retval, labels, centers = cv2.kmeans(np.float32(X), k, None, criteria, 10, cv2.KMEANS_PP_CENTERS)

#print(labels)


MR=""
ContHits=0
ContFailures=0

for i in range(len(labels)):
   
    label=labels[i]
    if  label[0]== 0:
        MR="R"
    else:    
        MR="M"
    if y[i]== MR:
        ContHits=ContHits+1
    else:
        ContFailures=ContFailures+1
        
    print("Signal " + str(i)+ " Predicted Class = "+ str(MR) + " True class = " + str(y[i]))


print(" Hits " + str(ContHits))
print(" Failures " + str(ContFailures))




