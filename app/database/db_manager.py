import sqlite3

def conectar():
    return sqlite3.connect("app_chapa_pp.db")
