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


CreaterDataCauHinh()