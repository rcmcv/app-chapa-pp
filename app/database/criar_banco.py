from app.database.db_manager import conectar

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            senha TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()
