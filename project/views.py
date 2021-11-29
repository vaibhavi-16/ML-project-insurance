from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression
#import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
import joblib

def index(request):
    return render(request,'index.html')
##-------------------------------------------------------------------------

##------------------------------------------------------------------------------

def insurance(request):
    return render(request, 'insurance.html')
##------------------------------------------------------------------------------

def result_insurance(request):
    gr = joblib.load("insurance.sav")
    lis = []
    lis.append(request.GET['n1'])
    lis.append(request.GET['n2'])
    lis.append(request.GET['n3'])
    lis.append(request.GET['n4'])
    lis.append(request.GET['n5'])
    lis.append(request.GET['n6'])

    result1 = gr.predict(np.array([lis]).reshape(1,-1))
    result1 = round(result1[0])

    insurance = "The predicted Insurance of premium policy is Rs."+str(result1)

    return render(request, 'result_insurance.html', {"result6": insurance})

##------------------------------------------------------------------------------

def require(request):
    return render(request, 'require.html')
##------------------------------------------------------------------------------
##------------------------------------------------------------------------------

def cement(request):
    return render(request, 'cement.html')
##------------------------------------------------------------------------------

def result_cement(request):
    gr = joblib.load("concrete.sav")
    lis = []
    lis.append(request.GET['n1'])
    lis.append(request.GET['n2'])
    lis.append(request.GET['n3'])
    lis.append(request.GET['n4'])
    lis.append(request.GET['n5'])
    lis.append(request.GET['n6'])
    lis.append(request.GET['n7'])
    lis.append(request.GET['n8'])

    result1 = gr.predict(np.array([lis]).reshape(1,-1))
    result1 = round(result1[0])

    cement = "The average compressive strength of the concrete is "+str(result1)+" MPa"

    return render(request, 'result_cement.html', {"result7": cement})
