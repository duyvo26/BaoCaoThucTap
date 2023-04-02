

def get_random_string(length):
    import random
    import string
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


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
