import sqlite3

def get_data():
    conn = sqlite3.connect('insurance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * from insurance;")
    result = cursor.fetchall()
    output = {"data": [list(i) for i in result]}
    return (output)


def add_data(data=[]):
    conn = sqlite3.connect('insurance.db')
    cursor = conn.cursor()

    var_string = ', '.join('?' * len(data))
    query_string = 'INSERT INTO insurance VALUES (%s);' % var_string
    cursor.execute(query_string, data)
    conn.commit()
    cursor.close()
    if conn:
        conn.close()
        print('SQLite Connection closed')
    return "Inserted into the database"