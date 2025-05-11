from db_manager import conectar

def ajustar_tabela_calculos():
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("ALTER TABLE calculos_tanques ADD COLUMN fundo_d_menor REAL")
    except:
        print("Coluna fundo_d_menor já existe.")
    try:
        cursor.execute("ALTER TABLE calculos_tanques ADD COLUMN fundo_altura_cone REAL")
    except:
        print("Coluna fundo_altura_cone já existe.")
    try:
        cursor.execute("ALTER TABLE calculos_tanques ADD COLUMN tampa_d_menor REAL")
    except:
        print("Coluna tampa_d_menor já existe.")
    try:
        cursor.execute("ALTER TABLE calculos_tanques ADD COLUMN tampa_altura_cone REAL")
    except:
        print("Coluna tampa_altura_cone já existe.")

    conn.commit()
    conn.close()
    print("Ajuste concluído.")

if __name__ == "__main__":
    ajustar_tabela_calculos()
