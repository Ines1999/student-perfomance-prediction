import pandas as pd
from joblib import dump, load
import numpy as np
from sklearn.metrics import accuracy_score

##############################
classificationResultsPrediction = dict()
accuracyPrediction = dict()
sorted_accuracyPrediction = dict()


##############################

def dataframeEncoding(df):
    df['Mjob'] = df['Mjob'].map({'at_home': 0, 'services': 1, 'teacher': 2, 'health': 3, 'other': 4})
    df['reason'] = df['reason'].map({'course': 0, 'home': 1, 'reputation': 2, 'other': 3})
    df['guardian'] = df['guardian'].map({'mother': 0, 'father': 1, 'other': 2})
    df['schoolsup'] = df['schoolsup'].map({'no': 0, 'yes': 1})
    df['paid'] = df['paid'].map({'no': 0, 'yes': 1})


######### Prediction  ###################
def predictionSVM():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    svm = load('../Modeling/Models/svm.pkl')
    s = svm.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['svm'] = result
    return s


def predictionKNN():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    global noms
    noms = df['lastName'].tolist()
    global prenoms
    prenoms = df['firstName'].tolist()
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    knn = load('../Modeling/Models/knn.pkl')
    s = knn.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['knn'] = result
    return s


def predictionNaiveBayes():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    nb = load('../Modeling/Models/naive_bayes.pkl')
    s = nb.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['naiveBayes'] = result
    return s


def predictionRandomForest():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    forest = load('../Modeling/Models/random_forest.pkl')
    s = forest.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['randomForest'] = result
    return s


def predictionGradientBoosting():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    gradient = load('../Modeling/Models/gradient_boosting.pkl')
    s = gradient.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['gradientBoosting'] = result
    return s


def predictionDecisionTree():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    decision = load('../Modeling/Models/decision_tree.pkl')
    s = decision.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['decisionTree'] = result
    return s


def predictionLogisticRegression():
    df = pd.read_csv('test.csv')
    dataframeEncoding(df)
    df['pass'] = np.where(df['G3'] < 10, 0, 1)
    X = df.drop(["G3", "pass", "lastName", "firstName"], axis=1)
    Y = df['pass']
    logistic_regression = load('../Modeling/Models/logistic_reg.pkl')
    s = logistic_regression.predict(X)
    result = accuracy_score(Y, s)
    accuracyPrediction['logisticRegression'] = result
    return s


def predictionResults():
    classificationResultsPrediction['svm'] = predictionSVM()
    classificationResultsPrediction['knn'] = predictionKNN()
    classificationResultsPrediction['logisticRegression'] = predictionLogisticRegression()
    classificationResultsPrediction['naiveBayes'] = predictionNaiveBayes()
    classificationResultsPrediction['randomForest'] = predictionRandomForest()
    classificationResultsPrediction['decisionTree'] = predictionDecisionTree()
    classificationResultsPrediction['gradientBoosting'] = predictionGradientBoosting()


def sortingAccurcy():
    sortedList = sorted(accuracyPrediction.items(), key=lambda x: x[1], reverse=True)
    print('-------------------')
    print(sortedList)
    global s_accuracyPrediction
    s_accuracyPrediction = dict(sortedList)
