from app.database.db_manager import conectar

def salvar_chapa(dados):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO chapas (descricao, largura, comprimento, espessura, limite_escoamento, cor, peso, valor_kg, custo_total)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao salvar chapa:", e)
        return False

def listar_chapas():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM chapas ORDER BY id DESC")
        resultados = cursor.fetchall()
        conn.close()
        return resultados
    except Exception as e:
        print("Erro ao listar chapas:", e)
        return []

def atualizar_chapa(chapa_id, dados):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE chapas
            SET descricao=?, largura=?, comprimento=?, espessura=?, limite_escoamento=?, cor=?, peso=?, valor_kg=?, custo_total=?
            WHERE id=?
        """, (*dados, chapa_id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao atualizar chapa:", e)
        return False

def excluir_chapa(chapa_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM chapas WHERE id = ?", (chapa_id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao excluir chapa:", e)
        return False

def salvar_solda(dados):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO soldas (descricao, peso, valor_kg, custo_total)
            VALUES (?, ?, ?, ?)
        """, dados)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao salvar solda:", e)
        return False