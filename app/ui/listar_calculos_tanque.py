import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers import controller_calculo_tanque
from app.ui.tela_calculo_tanque import abrir_tela_calculo_tanque

def abrir_listagem_calculos():
    janela = tk.Toplevel()
    janela.title("Cálculos de Tanques Realizados")

    largura = 1200
    altura = 500
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
    janela.resizable(False, False)

    frame = ttk.Frame(janela)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    colunas = ("id", "tipo_tanque", "cliente", "diametro", "altura",
               "fundo", "tampa", "chapas", "usuario", "data")
    tabela = ttk.Treeview(frame, columns=colunas, show="headings")

    tabela.heading("id", text="ID")
    tabela.heading("tipo_tanque", text="Tipo de Tanque")
    tabela.heading("cliente", text="Cliente")
    tabela.heading("diametro", text="Ø (mm)")
    tabela.heading("altura", text="Altura (mm)")
    tabela.heading("fundo", text="Fundo")
    tabela.heading("tampa", text="Tampa")
    tabela.heading("chapas", text="Qtd Chapas")
    tabela.heading("usuario", text="Usuário")
    tabela.heading("data", text="Data")

    for col in colunas:
        tabela.column(col, width=100)
    tabela.pack(fill="both", expand=True)

    def carregar_calculos():
        for item in tabela.get_children():
            tabela.delete(item)
        lista = controller_calculo_tanque.listar_calculos_tanques()
        for linha in lista:
            tabela.insert("", "end", values=(
                linha[0], linha[1], linha[2], linha[3], linha[4],
                linha[5], linha[6], linha[8] if linha[8] else "",
                linha[10], linha[11][:10]
            ))

    def excluir():
        item = tabela.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um cálculo para excluir.")
            return
        valores = tabela.item(item, "values")
        if messagebox.askyesno("Confirmar", f"Deseja excluir o cálculo ID {valores[0]}?"):
            if controller_calculo_tanque.excluir_calculo_tanque(valores[0]):
                messagebox.showinfo("Sucesso", "Cálculo excluído com sucesso.")
                carregar_calculos()
            else:
                messagebox.showerror("Erro", "Erro ao excluir cálculo.")

    def editar():
        item = tabela.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione um cálculo para editar.")
            return
        valores = tabela.item(item, "values")
        calculo_id = valores[0]
        dados = controller_calculo_tanque.buscar_calculo_por_id(calculo_id)
        if not dados:
            messagebox.showerror("Erro", "Cálculo não encontrado.")
            return
        abrir_tela_calculo_tanque(dados)

    botoes = ttk.Frame(janela)
    botoes.pack(pady=10)
    ttk.Button(botoes, text="✏️ Editar Selecionado", command=editar).pack(side="left", padx=10)
    ttk.Button(botoes, text="🗑️ Excluir Selecionado", command=excluir).pack(side="left", padx=10)

    carregar_calculos()
