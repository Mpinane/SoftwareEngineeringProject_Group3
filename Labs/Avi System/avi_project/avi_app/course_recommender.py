import pandas as pd
import numpy as np
from sklearn import tree

#enrol=[['COMS1018A', 'COMS2002A'],[80,100]]
def recommend_course(enrol,code):
    X=pd.read_csv('preprocessed_data/training_features_'+code+'.csv').values
    Y=pd.read_csv('preprocessed_data/training_class_'+code+'.csv').values[0]
    courses=enrol[0]
    marks=enrol[1]
    df=pd.read_csv('preprocessed_data/courses_undergraduate.csv')
    all_courses=df['COURSE_CODE']
    all_courses=np.array(all_courses)
    symbols=[-1]*len(all_courses)
    
    # Convert all the marks to symbols
    for i in range(len(marks)):
        if 0<=marks[i] and marks[i]<=49:
            marks[i]=4 # F
        if 50<=marks[i] and marks[i]<=59:
            marks[i]=3 # D
        if 60<=marks[i] and marks[i]<=69:
            marks[i]=2 # C
        if 70<=marks[i] and marks[i]<=74:
            marks[i]=1 # B
        if 75<=marks[i] and marks[i]<=100:
            marks[i]=0 # A
    
    for i in range(len(all_courses)):
        for j in range(len(courses)):
            if all_courses[i]==courses[j]:
                symbols[i]=marks[j]
    
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X, Y)
    symbols=[np.array(symbols)]
    predicted_output=clf.predict(symbols)
    
    if predicted_output[0]==0:
        return 'A'
    elif predicted_output[0]==1:
        return 'B'
    elif predicted_output[0]==2:
        return 'C'
    elif predicted_output[0]==3:
        return 'D'
    elif predicted_output[0]==4:
        return 'F'

df_honour=pd.read_csv('preprocessed_data/HONOURS.csv')
honours_codes=df_honour['COURSE_CODE']
honours_codes=np.array(honours_codes)
predicted_symbols=[]
predicted_courses=[]

def predict():
    for i in range(len(honours_codes)):
        
        returned=recommend_course(enrol,honours_codes[i])
        if returned=='A' or returned=='B' or returned=='C':
            predicted_courses.append(honours_codes[i])
            predicted_symbols.append(returned)
    return [predicted_courses,predicted_symbols]
        
print(predict())