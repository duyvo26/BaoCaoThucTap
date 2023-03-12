# LogisticRegression
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from importlib.resources import path
import math
import os
import csv
from matplotlib import pyplot as plt
import numpy as np
from numpy import array, random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scipy import stats
import pylab as pl
import shutil
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import ExtraTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import base64
from datetime import datetime
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
import pickle
from mOC_iSVM.static.ChucNang import get_random_string, AddModelSql

path_stock = os.path.dirname(os.path.abspath("hello"))+os.sep


def check_miss_data(X):
    df = pd.DataFrame(X)
    # try:
    #     return ('?' in df.values) | (np.nan in df.values)
    # except:
    ListData = list(df.values)
    for i in ListData:
        for a in i:
            # print(a)
            if "?" == a or np.nan == a:
                return True
    return False


def ImputeMissValue(X):
    X = pd.DataFrame(X)
    X = X.replace("?", np.nan)
    impute_nan = SimpleImputer(missing_values=np.nan)
    X = impute_nan.fit_transform(X)

    return X


def EncodeLable(y):
    encode = LabelEncoder()
    y = encode.fit_transform(y)
    return y


def read_data(file_name):
    df = pd.read_csv(file_name)
    X = df.drop("class", axis=1)
    y = df["class"]
    so_dac_trung = X.shape[1]
    so_mau = X.shape[0]
    so_lop = len(np.unique(y))
    print("Tap du lieu co", so_mau, "mau")
    print("Tap du lieu co", so_dac_trung, "dat trung")
    print("Tap du lieu co", so_lop, "lop")
    return X, y


def Train_batch(batch, path_stock):
    arr = []
    with open(path_stock+"/data.csv") as f:
        arr = f.readlines()
        arr = np.array(arr)
        random.shuffle(arr)
        arr = np.array_split(arr, batch)
    if os.path.exists(path_stock+"/tmp"):
        shutil.rmtree(path_stock+"/tmp")
    os.makedirs(path_stock+"/tmp")
    for i in range(0, len(arr)):
        with open(
                path_stock+f"/tmp/{i+1}.csv", "w") as f:
            f.writelines(arr[i])
    return batch
  # chia thành 10
# n = 20
# bước nhảy k=
# k = 3


def Select_Model(idUser, dataIn, test_size_, path_open, path_save, n=20, k=3, ChooseModel="AdaBoostClassifier"):
    if (ChooseModel != all):
        print("DataIn", dataIn)
        if ChooseModel == "GaussianNB":
            Model = GaussianNB()
        elif ChooseModel == "DecisionTreeClassifier":
            Model = DecisionTreeClassifier(criterion=dataIn)
        elif ChooseModel == "KNeighborsClassifier":
            Model = KNeighborsClassifier(n_neighbors=int(dataIn))
        elif ChooseModel == "BernoulliNB":
            Model = BernoulliNB()
        elif ChooseModel == "ExtraTreeClassifier":
            Model = ExtraTreeClassifier(criterion=dataIn)
        elif ChooseModel == "BaggingClassifier":
            Model = BaggingClassifier(n_estimators=int(dataIn))
        elif ChooseModel == "AdaBoostClassifier":
            Model = AdaBoostClassifier()
        elif ChooseModel == "MLPClassifier":
            Model = MLPClassifier()
        elif ChooseModel == "LinearDiscriminantAnalysis":
            Model = LinearDiscriminantAnalysis()
        else:
            ChooseModel = "RandomForestClassifier"
            dataIn = dataIn.split(',')
            Model = RandomForestClassifier(
                n_estimators=int(dataIn[0]), criterion=str(dataIn[1]))

    X, y = read_data(path_open)
    print("Có Dữ Liệu Lỗi", check_miss_data(X))
    x = ImputeMissValue(X)
    y = EncodeLable(y)
    print(X, y)

    print("Test size\t", str(test_size_))

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=test_size_, shuffle=True)

    begin = 0
    end = int(len(x_train) / n)

    list_accuracy_score, list_f1_score, list_recall_score, list_precision_score = [], [], [], []
    list_accuracy_score_bieuDo, list_precision_score_bieuDO, list_recall_score_bieuDO, list_f1_score_bieuDO = [], [], [], []

    TrainXY = []

    for index in range(n):
        print("begin", begin, "end", end)
        trainx = x_train[begin:end]
        trainy = y_train[begin:end]
        
        TrainXY.append([trainx, trainy])
        
        
        print('****-------------------------------------------------------------*****')

        print("batch", index)
        if index > 0 and index - k >= 0:
            print("len X real", len(trainx))
            
            for i in range(index-k, index):
                print('add batch', i)
                # trainx = pd.concat([trainx, TrainXY[i][0]])
                # trainy = pd.concat([trainy, TrainXY[i][1]])
                trainx = np.concatenate((trainx, TrainXY[i][0]))
                trainy = np.concatenate((trainy, TrainXY[i][1]))
                # trainx += TrainXY[i][0]
                # trainy += TrainXY[i][1]
                print('*********')
                print("len X add", len(trainx))
                print('*********')
            print('*********')
        if index > 0 and index - k < 0:
            print('*********')
            # print(TrainXY[index])
            print('*********')
            print("len X real", len(trainx))
            print('*********')
            for i in range(0, index):
                print('add batch', i)
                trainx = np.concatenate((trainx, TrainXY[i][0]))
                trainy = np.concatenate((trainy, TrainXY[i][1]))
                # trainx += TrainXY[i][0]
                # trainy += TrainXY[i][1]
                print('*********')
                print("len X add", len(trainx))
                print('*********')
            print('*********')

        print("len X SUM", len(trainx))

        
        print("LEN X", len(trainx))
        Model.fit(trainx, trainy)
        print("train model batch", index, n)

        print('****-------------------------------------------------------------*****')

        if (index == n-1):
            # save the model to disk
            now = datetime.now()
            dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
            try:
                os.makedirs(path_save+'/DowModels/')
            except:
                print("")
                
                

            filename = get_random_string(8)+'.sav'  
            path = path_save+'/DowModels/'+ filename
            
            
            pickle.dump(Model, open(path, 'wb'))
            AddModelSql(idUser, ChooseModel,
                                 filename, path, str(dt_string))
            
            
            
        y_pred = Model.predict(x_test)
        list_label_real, out_label = y_pred, y_test
        acc = balanced_accuracy_score(list_label_real, out_label)
        list_accuracy_score.append(f"{index} {acc}")
        list_accuracy_score_bieuDo.append(acc)
        # Precision
        acc = precision_score(
            list_label_real, out_label, average="macro")
        list_precision_score.append(f"{index} {acc}")
        list_precision_score_bieuDO.append(acc)
        # recall_score
        acc = recall_score(list_label_real, out_label, average='weighted')
        list_recall_score.append(f"{index} {acc}")
        list_recall_score_bieuDO.append(acc)
        # f1_score
        acc = f1_score(list_label_real, out_label, average='weighted')
        list_f1_score.append(f"{index} {acc}")
        list_f1_score_bieuDO.append(acc)

        begin += int(len(x_train) / n)
        end += int(len(x_train) / n)

    # shutil.rmtree(path_save_parent)
    # shutil.rmtree(path_save+'/bieudo')
    # return arr_nu, arr_gamma, arr, x_ve
    return list_accuracy_score_bieuDo, list_precision_score_bieuDO, list_recall_score_bieuDO, list_f1_score_bieuDO

