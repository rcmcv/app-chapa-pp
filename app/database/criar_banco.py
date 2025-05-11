from app.database.db_manager import conectar

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            senha TEXT NOT NULL
        );
    """)

    # Tabela de chapas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chapas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            largura REAL,
            comprimento REAL,
            espessura REAL,
            limite_escoamento REAL,
            cor TEXT,
            peso REAL,
            valor_kg REAL,
            custo_total REAL
        );
    """)

    # Tabela de soldas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS soldas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            peso REAL,
            valor_kg REAL,
            custo_total REAL
        );
    """)

        # Tabela de cálculos de tanques
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calculos_tanques (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo_tanque TEXT NOT NULL,
            cliente TEXT NOT NULL,
            diametro_mm REAL NOT NULL,
            altura_mm REAL NOT NULL,
            fundo_tipo TEXT NOT NULL,
            tampa_tipo TEXT NOT NULL,
            area_total_mm2 REAL,
            chapas_utilizadas INTEGER,
            sobra_mm2 REAL,
            usuario_id INTEGER NOT NULL,
            data_calculo TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    conn.close()
