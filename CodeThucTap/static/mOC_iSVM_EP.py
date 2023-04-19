from genericpath import exists
from importlib.resources import path
import math
from operator import index
import os
from re import A
from matplotlib import pyplot as plt
import numpy as np
from numpy import random
import time
import datetime
import shutil
from datetime import datetime
from pandas import cut
from pyparsing import line
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from CodeThucTap.static import svmutil as svm

import ChucNang




def GetMaxArr(arr, EP):
    # arr = [['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_1', 0.7484101935469293], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_2', 0.9124422346010951], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_3', 0.9484696268588207], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_4', 0.9716159507791386], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_5', 0.9757866904337492],
    #        ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_6', 0.9824343434343434], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_7', 0.9911616161616161], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_8', 0.9911616161616161], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_9', 0.9911616161616161], ['D:\\GIT\\Python\\WebmOC_iSVM\\LuanVanThucTap2023\\mOC_iSVM/static//media/\\tmp/models/model_batch_10', 0.9939393939393939]]
    arrACC = []
    # print(arr)
    for a in arr:
        if a[1] >= EP:
            arrACC.append(a)
            arr.remove(a)

    return arrACC


def FindFirstFileTrain(arr, filetrainFind):
    for i in arr:
        for a in i:
            if a.split('/')[len(a.split('/')) - 1] == filetrainFind.split('/')[len(filetrainFind.split('/')) - 1]:
                if (os.path.exists(a) == True):
                    print("Tim thay file", a)
                    return a
            

def mOC_iSVM_EP(idUser, file_train, file_test, path_stock, best_nu=0.050512, best_gamma=0.005, Age=3, batch=10):
    ChucNang.replace_file(file_train)
    ChucNang.replace_file(file_test)
    # batch
    arr = []
    # tron mang #################################
    with open(file_train) as f:
        arr = f.readlines()
        # arr = np.array_split(f.readlines(), batch)
    random.shuffle(arr)
    arr = np.array_split(arr, batch)
    # tron mang #################################
    if os.path.exists(path_stock+"tmp/tmp_batch"):
        shutil.rmtree(path_stock+"tmp/tmp_batch")
    for i in range(0, len(arr)):
        os.makedirs(path_stock+f"/tmp/tmp_batch/train_batch_{i+1}")
        with open(path_stock+f"/tmp/tmp_batch/train_batch_{i+1}/train_batch_{i+1}.train", "w") as f:
            f.writelines(arr[i])
        with open(path_stock+f"/tmp/tmp_batch/train_batch_{i+1}/train_batch_{i+1}.train") as f:
            ChucNang.SplitLabel_For_batch(
                f, path_stock+f"/tmp/tmp_batch/train_batch_{i+1}")
    # lay cac class trong file train
    arrLable = []
    for i in arr:
        for a in i:
            arrLable.append(int(a.split(" ")[0]))
    ###########################################
    arrLable = np.unique(arrLable)
    ###########################################
    print("Danh sach lable", arrLable)
    # train by Age
    path_save_models = path_stock+f"tmp/models"
    if (os.path.exists(path_save_models) == True):
        shutil.rmtree(path_stock+f"tmp/models")
    os.makedirs(path_save_models)
    ###########################################
    arrFileModel = []
    ###########################################
    arrFileTrain = []
    ###########################################
    for i in range(1, batch+1):
        arrTam = []
        for lb in arrLable:
            arrTam.append(path_stock+f"tmp/tmp_batch/train_batch_{i}/data/{lb}.train")
        arrFileTrain.append(arrTam)
        
        
        
    import time
    TimeSave = 0
    TimeEnd = 0
    ThoiGianOn = time.time()
    
    
    for i in range(0, batch):
        
        TimeEnd = TimeSave * batch
        TimeOn = TimeSave * i
        TimeOut = TimeEnd - TimeOn

        GiayLoad = int(time.time() - ThoiGianOn)
        print("############################################################################################")
        print(f"-------------Thoi gian chay {GiayLoad} giay------------- ")
        PhutLoad = int(GiayLoad / 60)
        print(f"-------------Thoi gian chay {PhutLoad} phut------------- ")

        print(
            f"------------- Thoi gian du kien 1 lan chay: {int(TimeOut)} giay------------- ")
        phut = int(int(TimeOut) / 60)
        print(
            f"------------- Thoi gian du kien 1 lan chay: {phut} phut------------- ")
        gio = int(phut / 60)
        print(
            f"------------- Thoi gian du kien 1 lan chay: {gio} gio------------- ")

        Batdau = time.time()

        print(f'------------- Da chay {i}/{batch} -----------------------')
        
        
        
        # get acc model
        ListACC = ChucNang.GetAccInBath(file_test, path_stock)
        ArrMax = GetMaxArr(ListACC, Age)
        
        os.makedirs(path_save_models+f"/model_batch_{i+1}")
        # print("----------------------------------------------------------------")
        # print(f'model_batch_{i}')
        # if (i == 0):
        # print max list arr acc
        print("------------")
        print("ACC max", Age)
        print("List MAx Accc")
        for ssfsa in ArrMax:
            print(ssfsa)
        print("------------")

        
        for j in ArrMax:
            # print("------------------------------")
            listmodel = os.listdir(j[0])
            for a in sorted(listmodel):
                modelLoad, modelCheck = j[0]+"/"+a, a    
                for az in arrLable:
                    if str(modelCheck.replace(".model", "")) == str(az):
                        # if int(modelCheck.replace(".model", "")) == 0:
                        #     print("Ket noi file", str(modelLoad),
                        #         str(arrFileTrain[i][az]))
                        #     print("...")
                        ChucNang.connect_2_file(
                            str(modelLoad), arrFileTrain[i][az], arrFileTrain[i][az])
            # print("------------------------------")
                        
        # lap n lan  label
        try:
            os.makedirs(path_stock+f"tmp/SaveModels")
        except:
            print("")
        for az in arrLable:
            if (os.path.exists(arrFileTrain[i][az]) == True):
                y, x = svm.svm_read_problem(arrFileTrain[i][az])
                prob = svm.svm_problem(y, x)
                param = svm.svm_parameter(
                    "-s 2 -q -n "+str(float(best_nu))+" -g "+str(float(best_gamma)))
                m = svm.svm_train(prob, param)
                svm.svm_save_model(
                    path_save_models+f"/model_batch_{i+1}/{az}.model", m)
                # save model
                if (i == (batch-1)):
                    svm.svm_save_model(
                        path_stock+f"/tmp/SaveModels/train_OUT__{az}.model", m)
            else:
                # find file train isset
                # print("----------------------------------------------")
                # print("Tim file train con thieu", arrFileTrain[i][az])
                PathTrain = FindFirstFileTrain(arrFileTrain, arrFileTrain[i][az])
                # print("----------------------------------------------")

                if (os.path.exists(PathTrain) == True):
                    y, x = svm.svm_read_problem(PathTrain)
                    prob = svm.svm_problem(y, x)
                    param = svm.svm_parameter(
                        "-s 2 -q -n "+str(float(best_nu))+" -g "+str(float(best_gamma)))
                    m = svm.svm_train(prob, param)
                    svm.svm_save_model(
                        path_save_models+f"/model_batch_{i+1}/{az}.model", m)
                    # save model
                    if (i == (batch-1)):
                        svm.svm_save_model(
                            path_stock+f"/tmp/SaveModels/train_OUT__{az}.model", m)
  
        KetThuc = time.time()

        TimeSave = KetThuc - Batdau

        print(
            f"-------------  Thoi gian chay 1 lan hien tai la:{KetThuc - Batdau} ----------------")

    # zip model
    try:
        os.makedirs(path_stock + f"/DowModels")
    except:
        print("")

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
    
    filename = ChucNang.get_random_string(8)
    path = path_stock + f"/DowModels/{filename}"
    shutil.make_archive(path, 'zip', path_stock+f"tmp/SaveModels")
    ChucNang.AddModelSql(idUser, 'EP', filename + '.zip', path, str(dt_string))
    
    
    list_accuracy_score, list_f1_score, list_recall_score, list_precision_score = [], [], [], []
    line_ftest = []
    with open(file_test) as ftest:
        line_ftest = ftest.readlines()
    list_label_real = []
    for i in line_ftest:
        text = i[0:ChucNang.GetPosition(i)]
        list_label_real.append(text)
    list_accuracy_score_bieuDo, list_precision_score_bieuDO, list_recall_score_bieuDO, list_f1_score_bieuDO = [], [], [], []
    yt, xt = svm.svm_read_problem(
        file_test)
    list_model = os.listdir(path_stock+"tmp/models")
    list_label = []
    list_p_val = []
    for index in range(0, len(list_model)):
        listmodel = os.listdir(
            path_stock+f"tmp/models/model_batch_{index+1}")
        # listmodel.sort()
        # print(path_stock+f"tmp/models/model_batch_{index+1}")
        for i in listmodel:
            m = svm.svm_load_model(
                path_stock+"tmp/models/"+list_model[index]+"/"+i)
            p_label, p_acc, p_val = svm.svm_predict(yt, xt, m)
            # print(path_stock+"tmp/models/"+list_model[index]+"/"+i)
            # print(p_acc)
            list_label.append(os.path.splitext(i)[0])
            list_p_val.append(p_val)
        out_label = []
        out_p_val = []
        for i in list_p_val[0]:
            out_p_val.append(i[0])
        for i in list_p_val[0]:
            out_label.append(list_label[0])
        for i in range(0, len(list_p_val)):
            for j in range(0, len(list_p_val[i])):
                if float(list_p_val[i][j][0]) > float(out_p_val[j]):
                    out_p_val[j] = list_p_val[i][j][0]
                    out_label[j] = list_label[i]
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
    return list_accuracy_score_bieuDo, list_precision_score_bieuDO, list_recall_score_bieuDO, list_f1_score_bieuDO

