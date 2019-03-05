import sqlite3

class Database:

    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS reminder(id INTEGER PRIMARY KEY,title text ,description text,time INTEGER, status INTEGER )")
        self.conn.commit()

    def insert(self,title,description,time,status):
        self.cur.execute("INSERT into reminder VALUES (NULL,?,?,?,?)",(title,description,time,status))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM reminder")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",description="",time="",status=""):
        self.cur.execute("SELECT * FROM reminder where title=? OR description=? OR time=? OR status=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM reminder where id =?",(id,))
        self.conn.commit()

    def update(self,id,description,title,year,status):
        self.cur.execute("UPDATE reminder SET title=?,description=?,time=?,status=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()