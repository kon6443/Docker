import sqlite3
import sys
import json

def delete(id):
    id = str(id)
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

def main(arg):
    delete(arg)
    show()

if __name__ == '__main__':
    arg = int(sys.argv[1])
    main(arg)   