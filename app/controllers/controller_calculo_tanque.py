from app.database.db_manager import conectar

# Inserir novo cálculo de tanque
def inserir_calculo_tanque(dados):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO calculos_tanques (
                tipo_tanque, cliente, diametro_mm, altura_mm,
                fundo_tipo, tampa_tipo, area_total_mm2,
                chapas_utilizadas, sobra_mm2, usuario_id,
                fundo_d_menor, fundo_altura_cone, tampa_d_menor, tampa_altura_cone
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, dados)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao inserir cálculo:", e)
        return False

# Listar todos os cálculos realizados
def listar_calculos_tanques():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calculos_tanques ORDER BY data_calculo DESC")
        resultados = cursor.fetchall()
        conn.close()
        return resultados
    except Exception as e:
        print("Erro ao listar cálculos:", e)
        return []

# Atualizar um cálculo existente
def editar_calculo_tanque(calculo_id, dados):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE calculos_tanques SET
                tipo_tanque = ?, cliente = ?, diametro_mm = ?, altura_mm = ?,
                fundo_tipo = ?, tampa_tipo = ?, area_total_mm2 = ?,
                chapas_utilizadas = ?, sobra_mm2 = ?, usuario_id = ?,
                fundo_d_menor = ?, fundo_altura_cone = ?, tampa_d_menor = ?, tampa_altura_cone = ?
            WHERE id = ?
        """, (*dados, calculo_id))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao editar cálculo:", e)
        return False

# Excluir cálculo por ID
def excluir_calculo_tanque(calculo_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM calculos_tanques WHERE id = ?", (calculo_id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Erro ao excluir cálculo:", e)
        return False

# Buscar um cálculo por ID (usado para preencher formulário em modo edição)
def buscar_calculo_por_id(calculo_id):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM calculos_tanques WHERE id = ?", (calculo_id,))
        resultado = cursor.fetchone()
        conn.close()
        return resultado
    except Exception as e:
        print("Erro ao buscar cálculo:", e)
        return None
