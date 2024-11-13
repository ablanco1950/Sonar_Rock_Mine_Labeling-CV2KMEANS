# Sonar_Rock_Mine_Labeling-CV2KMEANS
Program that allows to determine the label of a sonar signal, whether it corresponds to a mine or a rock, based on CV2 KMEANS. It starts from the signal file sonar_data.csv, although it is a labeled file, the labels are only used to check the clustering results. In the test to label the sonar_data.csv file, 201 labels were correctly asigned and 7 failed: success rate of 96.63%

The procedure can also be used to classify signals directly.

Run:

Train_Sonar_Rock_Mine_Labeling_CV2KMEANS.py

References:

https://medium.com/@vamshidharpratap/implementing-k-means-clustering-using-opencv-in-python-bd466b146568

sonar_data.csv downloaded from:
https://github.com/bhargav-borah/Rock-vs-Mine-Detection/blob/main/logistic_regression.ipynb
