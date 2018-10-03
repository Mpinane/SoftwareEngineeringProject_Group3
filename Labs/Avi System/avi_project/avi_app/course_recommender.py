import pandas as pd
import numpy as np
from sklearn import tree

X=pd.read_csv('preprocessed_data/training_features_COMS4037A.csv').values
Y=pd.read_csv('preprocessed_data/training_class_COMS4037A.csv').values[0]

#a=[ 3,  0,  0,  4,  4,  0,  2,  2, -1, -1,  3,  0,  0,  0,  3,  2,  3, 0,  4,  4, -1, -1,  3,  4,  1,  4,  2,  0,  0,  0,  0]
#b=[['D','A','A','F','F','A','C','C','-1','-1','D','A','A','A','D','C','D','A','F','F','-1','-1','D','F','B','F','C','A','A','A','A'],['UNDERGRADUATE']]

predict_input=[X[0]]
print(predict_input)
def recommend_course(X,Y):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    predicted_output=clf.predict(predict_input)
    
    if predicted_output[0]==0:
        return ('A')
    elif predicted_output[0]==1:
        return ('B')
    elif predicted_output[0]==2:
        return ('C')
    elif predicted_output[0]==3:
        return ('D')
    elif predicted_output[0]==4:
        return ('F')
    
print(recommend_course(X,Y))