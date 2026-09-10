import sqlite3 

def conection(): 
    return sqlite3.connect(".//trabajo2.db")