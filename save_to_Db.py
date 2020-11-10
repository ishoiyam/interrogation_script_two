import mysql.connector as mdb


def connect_to_db():
    global conn
    conn = mdb.connect(host="localhost", user="root", password="toor", database="youtube_tutorial")



def insert_one(fn, ln, email, home_addr, origin):
    cursor = conn.cursor()
    sql = """ insert into profiles (first_name, last_name, email, home_addr, origin) values (%s, %s, %s, %s, %s)  """
    data = (fn, ln, email, home_addr, origin)
    cursor.execute(sql, data)
    conn.commit()

def get_data():
    sql = """ select * from profiles  """
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()

    for r in result:
        print(r)
