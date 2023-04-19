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

def CheckTaoThuMuc(path):
    import os
    try:
        os.mkdir(path)
    except:
        print("")

        
def get_random_string(length):
    import random
    import string
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def GetFirstLabel(value):
    # Lay mot phan cua chuoi truoc ky tu space
    position = value.find(" ")
    return value[0:position]


def GetPosition(value):
    # Lay mot phan cua chuoi truoc ky tu space
    position = value.find(" ")
    return position


def SplitLabel(ftrain, path_stock):
    path = path_stock+'tmp/tmp50/data/'
    # Tao folder dua tren ten file train
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    # Doc du lieu tu file train va gan vao mang
    lines = ftrain.readlines()
    # Tao mot mang trong chua danh sach cac label
    list_label = []
    # Tach label cua dong dau tien trong file train va gan vao danh sach label
    list_label.append(GetFirstLabel(lines[0]))
    # Vong lap for den gan cac label con lai cua file train vao danh sach label
    for i in lines[1:len(lines)]:
        # Tach label cua dong thu i
        text = GetFirstLabel(i)
        # Kiem tra ton tai trong danh sach label
        if text not in list_label:
            # Neu chua co se them label do vao danh sach label
            list_label.append(text)
    # Tao mot dictionary chua cac lop dua theo label cua tung lop
    list_class = dict()
    # Gan cho moi label la mot mang trong trong dictionary
    for i in list_label:
        list_class[i] = []
    # Vong lap for chay tung dong trong mang du lieu train
    for i in lines:
        # Tach nhan cua dong thu i
        text = GetFirstLabel(i)
        # Gan dong thu i vao dictionary theo nhan tuong ung
        list_class[text].append(i)
    # Ghi tung key:value cua dictionary ra file
    for i in list_class:
        with open(path+"/"+str(i)+".train", "w") as fw:
            fw.writelines(list_class[i])


def func(value):
    return ''.join(value.splitlines())


def Cut_file(numberClass, path_file, batch):
    # print("HAM cut file")
    dulieu = []
    mang = []
    f = open(path_file, "r")
    mang = f.readlines()
    dem = 0
    for line in mang:
        # print(line)
        if (dem > 0):
            tach = line.split(',')
            dataline = ''
            tmp = 0
            for i in range(0, len(tach)):
             # # # # # # # # # # #    CLASS NUMBER # # # # # # # # # # # # # # # # #
                if (int(i) == int(numberClass)):
                    dataline = func(f'{tach[i]}{dataline}')
                else:
                    # Khong co id #############
                    dataline += func(f' {i}:{tach[i]}')
            dulieu.append(dataline+'\n')
            #####################################
        dem = dem+1
    # print(dulieu)
    arr = np.array(dulieu)
    arraydt = []
    random.shuffle(arr)
    partone = []
    parttwo = []
    index = 1
    for i in arr:
        arraydt.append(i)
        Ssize = round(len(arr)*(batch/10))
        if (Ssize % 2 == 1):
            Ssize += 1
        if index <= (Ssize):
            partone.append(i)
        else:
            parttwo.append(i)
        index += 1
    return partone, parttwo, arraydt


def Cut_fileCSV(numberClass, path_file, batch):
    print("HAM cut file")
    dulieu = []
    mang = []
    f = open(path_file, "r")
    mang = f.readlines()
    dem = 0
    for line in mang:
        # print(line)
        if (dem > 0):
            tach = line.split(',')
            dataline = ''
            tmp = 0
            for i in range(0, len(tach)):
             # # # # # # # # # # #    CLASS NUMBER # # # # # # # # # # # # # # # # #
                if (int(i) == int(numberClass)):
                    dataline = func(f'{tach[i]}{dataline}')
                else:
                    # Khong co id #############
                    dataline += func(f' {i}:{tach[i]}')
            dulieu.append(dataline+'\n')
            #####################################
        dem = dem+1
    # print(dulieu)
    arr = np.array(dulieu)
    arraydt = []
    random.shuffle(arr)
    partone = []
    parttwo = []
    index = 1
    for i in arr:
        arraydt.append(i)
        Ssize = round(len(arr)*(batch/10))
        if (Ssize % 2 == 1):
            Ssize += 1
        if index <= (Ssize):
            partone.append(i)
        else:
            parttwo.append(i)
        index += 1
    return partone, parttwo, arraydt


def SplitLabel_For_batch(ftrain, path_file):
    path = path_file+'/data/'
    # Tao folder dua tren ten file train
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)
    # Doc du lieu tu file train va gan vao mang
    lines = ftrain.readlines()
    # Tao mot mang trong chua danh sach cac label
    list_label = []
    # Tach label cua dong dau tien trong file train va gan vao danh sach label
    list_label.append(GetFirstLabel(lines[0]))
    # Vong lap for den gan cac label con lai cua file train vao danh sach label
    for i in lines[1:len(lines)]:
        # Tach label cua dong thu i
        text = GetFirstLabel(i)
        # Kiem tra ton tai trong danh sach label
        if text not in list_label:
            # Neu chua co se them label do vao danh sach label
            list_label.append(text)
    # Tao mot dictionary chua cac lop dua theo label cua tung lop
    list_class = dict()
    # Gan cho moi label la mot mang trong trong dictionary
    for i in list_label:
        list_class[i] = []
    # Vong lap for chay tung dong trong mang du lieu train
    for i in lines:
        # Tach nhan cua dong thu i
        text = GetFirstLabel(i)
        # Gan dong thu i vao dictionary theo nhan tuong ung
        list_class[text].append(i)
    # Ghi tung key:value cua dictionary ra file
    for i in list_class:
        with open(path+"/"+str(i)+".train", "w") as fw:
            fw.writelines(list_class[i])
        # Batch_to_model(path+str(i)+".train",path_file)


def connect_2_file(path_file_model, path_file_train, path_file_sum):
    f = open(path_file_model)
    file_one = f.readlines()
    file_one.pop(0)
    file_one.pop(0)
    file_one.pop(0)
    file_one.pop(0)
    file_one.pop(0)
    file_one.pop(0)
    file_one.pop(0)
    if (os.path.exists(path_file_train) == True):
        f = open(path_file_train)
        file_two = f.readlines()
    else:
        file_two = []
    arr = file_two+(file_one)
    f = open(path_file_sum, "w")
    f.write("")
    f = open(path_file_sum, "a")
    for i in range(0, len(arr)):
        f.write(arr[i])


def find_best_nugamma(phanTram, file_open, path_stock, nu_start, nu_end, nu_step, gamma_start, gamma_end, gamma_step):
    try:
        os.makedirs(path_stock)
    except:
        print("")

    replace_file(file_open)
    f = open(file_open)
    mang = f.readlines()
    path_stock += os.sep
    if (os.path.exists(path_stock+'/train') == False):
        os.mkdir(path_stock+'/train')
    if (os.path.exists(path_stock+f'/tmp/tmp50') == False):
        os.makedirs(path_stock+f"/tmp/tmp50")
    if (os.path.exists(path_stock+f'/svm_data') == False):
        os.mkdir(path_stock+f"/svm_data")
    namefile_open = "/data"
    print("Tao file save .train")
    f_save_train = open(
        path_stock+f"/train/{namefile_open}.train", "w")
    f_save_train.write("")
    print("Tao file save .test")
    f_save_test = open(path_stock+f"/train/{namefile_open}.test", "w")
    f_save_test.write("")
    print("url\t"+path_stock+f"/train/{namefile_open}")
    index = 1
    print("Chia file .train ra lam 2")
    print("Tong file data,", len(mang))
    max = int(len(mang) * phanTram)
    lentest, lentrain = 0, 0
    # max = int(len(mang) / 2)
    for j in mang:
        f_save_test = open(path_stock+f"/train/{namefile_open}.test", "a")
        f_save_train = open(
            path_stock+f"/train/{namefile_open}.train", "a")
        if (index < max):
            # print([f'{j}\n {index}'])
            f_save_test.writelines(j)
            lentest += 1
        else:
            f_save_train.writelines(j)
            lentrain += 1
        index += 1
    print("Len file train", lentrain)
    print("Len file test", lentest)
    list_nu = np.arange(nu_start, nu_end, nu_step, float)
    print("NU", nu_start, nu_end, nu_step)
    list_gamma = np.arange(gamma_start, gamma_end, gamma_step, float)
    print("Gamma", gamma_start, gamma_end, gamma_step)
    # print(list_nu)
    # print(list_gamma)
    now = datetime.now()
    # convert to string
    str_date = now.strftime("%Y-%m-%d_%H-%M-%S")
    list_nu_gamma = []
    list_ba = []
    best_nu = 0
    best_gamma = 0
    max_acc = 0
    checkNumber = 0
    maxFor = len(list_nu) * len(list_gamma)
    MaxData = 0
    GiayRun = 0
    import time
    ArrNuGa = []
    for nu in list_nu:
        for gamma in list_gamma:
            begin = time.time()
            checkNumber += 1
            # for file_name in list_file:
            # get time now
            now = datetime.now()
            current_time = now.strftime("%H%M%S")
            with open(path_stock+os.sep+"train/data.train") as ftrain:
                SplitLabel(ftrain, path_stock)
            path_tmp50 = path_stock+"tmp/tmp50/data/"
            path_data = os.listdir(path_tmp50)
            path_model = path_stock+"tmp/tmp50/model/"
            if os.path.exists(path_model):
                shutil.rmtree(path_model)
            os.makedirs(path_model)
            for i in path_data:
                y, x = svm.svm_read_problem(path_tmp50+i)
                # print("CHeck",y)
                prob = svm.svm_problem(y, x)
                param = svm.svm_parameter(
                    "-s 2 -q -n "+str(float(nu))+" -g "+str(float(gamma)))
                m = svm.svm_train(prob, param)
                svm.svm_save_model(
                    path_model+os.path.splitext(os.path.basename(i))[0]+".model", m)
            # test
            line_ftest = []
            with open(path_stock+'train/data.test') as ftest:
                line_ftest = ftest.readlines()
            list_label_real = []
            for i in line_ftest:
                text = i[0:GetPosition(i)]
                list_label_real.append(text)
            # chay thu lai cai ei
            yt, xt = svm.svm_read_problem(path_stock+'train/data.test')
            list_model = os.listdir(path_stock+"tmp/tmp50/model")
            list_label = []
            list_p_val = []
            for i in list_model:
                m = svm.svm_load_model(path_stock+"tmp/tmp50/model/"+i)
                p_label, p_acc, p_val = svm.svm_predict(yt, xt, m)
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
            f = open(path_stock+f"svm_data/svm_{str_date}.csv", "a")
            f.write(f"{acc} {nu} {gamma}\n")
            if acc > max_acc or acc == 1:
                max_acc = acc
                best_nu = nu
                best_gamma = gamma
                MaxData = [max_acc, best_nu, best_gamma]
                ArrNuGa.append(MaxData)
                print(f">>>{acc}  {nu}  {gamma}")
            end = time.time()
            # if GiayRun == 0:
            GiayRun = end - begin
            # print("time",  end - begin)
            print(
                "---------------------------------------------------------------------------")
            print("Con lai\t", maxFor - checkNumber)
            Giay = int((maxFor - checkNumber)*GiayRun)
            print("So GIAY\t", Giay)
            Phut = int(Giay / 60)
            print("So PHUT\t", Phut)
            Gio = int(Phut / 60)
            print("SO GIO\t", Gio)
            Ngay = int(Gio / 24)
            print("SO NGAY\t", Ngay)
            print(f"SO MAX\t {MaxData}")
            print(f"On {acc} {nu} {gamma}")
            print(
                "---------------------------------------------------------------------------")
    with open(path_stock+"tmp/best_nu_gamma.csv", 'w') as file:
        file.write(f'{best_nu} {best_gamma}')
    shutil.rmtree(path_stock+"tmp/tmp50", ignore_errors=True)
    shutil.rmtree(path_stock+"tmp/history_nu_gamma", ignore_errors=True)
    return MaxData[1], MaxData[2], MaxData[0], ArrNuGa


def replace_file(file_open):
    f = open(file_open)
    ar = f.readlines()
    mang1 = []
    for i in ar:
        ir = i.replace('"', '')
        ir = ir.replace('\n', '')
        mang1.append(ir)
    f = open(file_open, 'w')
    f.write('')
    f = open(file_open, 'a')
    mang = []
    for i in mang1:
        if (i != ''):
            f.write(f'{i}\n')
            mang.append(f'{i}\n')


def FindFirstFileTrain(arr, filetrainFind):
    for i in arr:
        for a in i:
            if a.split('/')[len(a.split('/')) - 1] == filetrainFind.split('/')[len(filetrainFind.split('/')) - 1]:
                if (os.path.exists(a) == True):
                    print("Tim thay file", a)
                    return a


def GetAccInBath(file_test, path_stock):
    # test
    line_ftest = []
    with open(file_test) as ftest:
        line_ftest = ftest.readlines()
    list_label_real = []
    for i in line_ftest:
        text = i[0:GetPosition(i)]
        list_label_real.append(text)

    yt, xt = svm.svm_read_problem(file_test)
    list_model = os.listdir(path_stock+"tmp/models")
    list_label = []
    list_p_val = []
    ArrModel = []
    for index in range(0, len(list_model)):
        listmodel = os.listdir(path_stock+f"tmp/models/model_batch_{index+1}")
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
        pathModel = path_stock+f"tmp/models/model_batch_{index+1}"
        ArrModel.append([pathModel, acc])
    return ArrModel


def ChuanDoanISVM(path_stock, path_models, txtIN):
    path_test = path_stock+"data.test"
    # # shutil.rmtree(path_test)
    # # os.makedirs(path_test)
    f = open(path_test, 'w')
    load = "1000 "+str(txtIN)
    f.write(load)
    f.close()
    print("LOAAA", load)
    yt, xt = svm.svm_read_problem(path_test)  # test cũng vậy nè
    print("++++++++++++++", xt)
    list_model = os.listdir(path_models)
    list_label = []
    list_p_val = []
    for i in list_model:
        m = svm.svm_load_model(
            path_models+os.sep+i)
        p_label, p_acc, p_val = svm.svm_predict(yt, xt, m)
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
    # print(out_label[0])
    return out_label[0]


def ChuanDoanCoDien(path_models, txtIN):
    import pickle
    loaded_model = pickle.load(open(path_models, 'rb'))
    outClass = loaded_model.predict([txtIN])
    outPhanTram = loaded_model.score([txtIN], outClass)
    return outClass, outPhanTram


def SaveModelSql():
    import sqlite3
    conn = sqlite3.connect('Model.db')
    conn.execute('''CREATE TABLE Model
         (ID INTEGER PRIMARY KEY,
         NAME           TEXT    NOT NULL,
         idUser            TEXT     NOT NULL,
         path            TEXT     NOT NULL,
         nameModel            TEXT     NOT NULL,
         Time            TEXT     NOT NULL
         );''')


def SaveCauHinhSql():
    import sqlite3
    conn = sqlite3.connect('Model.db')
    conn.execute('''CREATE TABLE CauHinh
         (ID INTEGER,
         Name    TEXT    NOT NULL,
         Data    TEXT    NOT NULL
         );''')


def CreaterDataCauHinh():
    import sqlite3
    SaveCauHinhSql()
    conn = sqlite3.connect('Model.db')

    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('0', 'fileAnh', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('1', 'fileModel', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('10', 'fileModelSVM', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('2', 'LengNameClass', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('3', 'LengNameThamSo', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('4', 'ListNameClass', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('5', 'ListNameThamSO', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('6', 'color', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('7', 'font', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('8', 'TieuDeDoan', '')")
    conn.execute(
        "INSERT INTO CauHinh (ID, Name, Data) VALUES ('9', 'Fsize', '')")
    conn.commit()
    conn.close()


def UpdateDataCauHinh(id, newData):
    import sqlite3
    conn = sqlite3.connect('Model.db')
    conn.execute(
        f"UPDATE CauHinh SET Data = '{newData}' WHERE ID = {id}")
    conn.commit()
    conn.close()


def GetDataCauHinh():
    import sqlite3
    conn = sqlite3.connect('Model.db')
    cursor = conn.cursor()  # create a cursor object
    cursor.execute(f"SELECT * FROM CauHinh ")
    output = cursor.fetchall()  # call fetchall() on the cursor object
    conn.commit()
    conn.close()
    return output




def AddModelSql(idUser, select, name, path, time):
    import sqlite3
    try:
        conn = sqlite3.connect('Model.db')
        conn.execute(
            f"INSERT INTO Model (NAME, nameModel, idUser, path ,Time) VALUES ('{name}','{select}', '{idUser}','{path}', '{time}' )")
    except:
        SaveModelSql()
        conn = sqlite3.connect('Model.db')
        conn.execute(
            f"INSERT INTO Model (NAME, nameModel, idUser, path ,Time) VALUES ('{name}','{select}', '{idUser}','{path}', '{time}' )")
    conn.commit()
    conn.close()


def ShowModel(idUser):
    import sqlite3
    conn = sqlite3.connect('Model.db')
    cursor_obj = conn.cursor()

    cursor_obj.execute(
        f"SELECT * FROM Model where idUser == '{idUser}' ORDER BY ID DESC")
    output = cursor_obj.fetchall()
    # for row in output:
    #     print(row)
    conn.commit()
    conn.close()
    return output
