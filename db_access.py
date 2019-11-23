import sqlite3

def find():
    conn = sqlite3.connect('tweetbot.sqlite3')
    c = conn.cursor()

    create_table = '''CREATE TABLE  IF NOT EXISTS  LAST_UPDATE(
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         LAST_UPDATE_ID INTEGER);'''
    c.execute(create_table)
    conn.commit()

    rows = c.execute('SELECT LAST_UPDATE_ID FROM LAST_UPDATE')
    row = c.fetchmany(1)

    c.close()
    conn.close()

    if len(row) == 1:
        return row[0]


def update(last_id):
    conn = sqlite3.connect('tweetbot.sqlite3')
    c = conn.cursor()

    rows = c.execute('SELECT * FROM LAST_UPDATE')
    row = c.fetchmany(1)

    if len(row) == 0:
        insert_sql = 'INSERT INTO LAST_UPDATE(ID, LAST_UPDATE_ID) VALUES (?, ?)'
        ids = (1, last_id)
        c.execute(insert_sql, ids)
        conn.commit()

        c.close()
        conn.close()

    else:
        update_sql = 'UPDATE LAST_UPDATE SET LAST_UPDATE_ID = ? WHERE ID = ?'
        ids = (last_id, 1)
        c.execute(update_sql, ids)
        conn.commit()

        c.close()
        conn.close()
