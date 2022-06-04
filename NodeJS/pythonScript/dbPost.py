import sqlite3
import sys
import json

def delete(id):
    conn = sqlite3.connect("test.db")
    with conn:
        cursor = conn.cursor()
        sql = 'DELETE FROM customer WHERE id=?'
        cursor.execute(sql,(id,))
        conn.commit()

def show():
    conn = sqlite3.connect("test.db")
    with conn:
        result = []
        #   generating a cursor from connection
        cursor = conn.cursor()
        cursor.execute('select * from customer')
        # Data fetch and printing out
        rows = cursor.fetchall()
        for row in rows:
            result.append(row)
            #print(row)
        return_value = json.dumps(result)
        print(return_value)

def insert(name, category, state):
    #   SQLite DB connection
    conn = sqlite3.connect("test.db")
    with conn:
        #   generating a cursor from connection
        cursor = conn.cursor()
        data = (
            ('One', 1, 'Seoul'),
            ('Two', 2, 'Suwon'),
            ('Three', 3, 'Daegu')
        )
        sql = "insert into customer(name,category,region) values (?,?,?)"
        #cursor.executemany(sql, data)    
        cursor.execute(sql,(name,category,state))
        conn.commit()        

def main(arg):
    name, category, state = arg[:]
    insert(name,category,state)
    show()

if __name__ == '__main__':
    main(sys.argv[1:])