import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers import controller_materiais

def abrir_tela_materiais():
    janela = tk.Toplevel()
    janela.title("Cadastro de Materiais")

    largura_janela = 1100
    altura_janela = 600
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    janela.resizable(False, False)

    id_chapa_edicao = [None]

    frame_chapa = ttk.LabelFrame(janela, text="Cadastro de Chapa")
    frame_chapa.pack(fill="x", padx=10, pady=10)

    campos_chapa = [
        ("Descrição", 0), ("Largura (mm)", 1), ("Comprimento (mm)", 2),
        ("Espessura (mm)", 3), ("Limite Escoamento (MPa)", 4),
        ("Cor", 5), ("Peso (kg)", 6), ("Valor (R$/kg)", 7), ("Custo Total", 8)
    ]

    entradas_chapa = {}
    for label, row in campos_chapa:
        ttk.Label(frame_chapa, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
        entrada = ttk.Entry(frame_chapa)
        entrada.grid(row=row, column=1, padx=5, pady=2)
        entradas_chapa[label] = entrada

    def calcular_custo_chapa(event=None):
        try:
            peso = entradas_chapa["Peso (kg)"].get().replace(",", ".")
            valor = entradas_chapa["Valor (R$/kg)"].get().replace(",", ".")
            custo_total = float(peso) * float(valor)
            entradas_chapa["Custo Total"].delete(0, tk.END)
            entradas_chapa["Custo Total"].insert(0, f"{custo_total:.2f}")
        except:
            entradas_chapa["Custo Total"].delete(0, tk.END)

    entradas_chapa["Peso (kg)"].bind("<KeyRelease>", calcular_custo_chapa)
    entradas_chapa["Valor (R$/kg)"].bind("<KeyRelease>", calcular_custo_chapa)

    def limpar_chapa():
        for entrada in entradas_chapa.values():
            entrada.delete(0, tk.END)
        id_chapa_edicao[0] = None
        entradas_chapa["Descrição"].focus()

    def salvar_chapa():
        try:
            peso = float(entradas_chapa["Peso (kg)"].get().replace(",", "."))
            valor = float(entradas_chapa["Valor (R$/kg)"].get().replace(",", "."))
            custo_total = peso * valor

            dados = (
                entradas_chapa["Descrição"].get(),
                float(entradas_chapa["Largura (mm)"].get().replace(",", ".")),
                float(entradas_chapa["Comprimento (mm)"].get().replace(",", ".")),
                float(entradas_chapa["Espessura (mm)"].get().replace(",", ".")),
                float(entradas_chapa["Limite Escoamento (MPa)"].get().replace(",", ".")),
                entradas_chapa["Cor"].get(),
                peso,
                valor,
                custo_total
            )

            if id_chapa_edicao[0]:
                sucesso = controller_materiais.atualizar_chapa(id_chapa_edicao[0], dados)
                msg = "atualizada" if sucesso else "Erro ao atualizar"
            else:
                sucesso = controller_materiais.salvar_chapa(dados)
                msg = "salva" if sucesso else "Erro ao salvar"

            if sucesso:
                messagebox.showinfo("Sucesso", f"Chapa {msg} com sucesso!")
                limpar_chapa()
                carregar_chapas()
            else:
                messagebox.showerror("Erro", f"Falha ao tentar {msg} a chapa.")
        except Exception as e:
            messagebox.showerror("Erro", f"Verifique os dados preenchidos.\n{e}")

    ttk.Button(frame_chapa, text="Salvar Chapa", command=salvar_chapa).grid(row=9, column=0, pady=10)
    ttk.Button(frame_chapa, text="Limpar", command=limpar_chapa).grid(row=9, column=1, pady=10)

    # --- LISTAGEM ---
    frame_lista = ttk.LabelFrame(janela, text="Chapas Cadastradas")
    frame_lista.pack(fill="both", expand=True, padx=10, pady=10)

    colunas = (
        "id", "descricao", "largura", "comprimento", "espessura",
        "limite", "cor", "peso", "valor", "custo"
    )

    tabela = ttk.Treeview(frame_lista, columns=colunas, show="headings")
    tabela.heading("id", text="ID")
    tabela.heading("descricao", text="Descrição")
    tabela.heading("largura", text="Largura\n(mm)")
    tabela.heading("comprimento", text="Comprimento\n(mm)")
    tabela.heading("espessura", text="Espessura\n(mm)")
    tabela.heading("limite", text="Limite\n(MPa)")
    tabela.heading("cor", text="Cor")
    tabela.heading("peso", text="Peso\n(kg)")
    tabela.heading("valor", text="R$/kg")
    tabela.heading("custo", text="Custo\nTotal")

    tabela.column("id", width=50)
    tabela.column("descricao", width=150)
    tabela.column("largura", width=90)
    tabela.column("comprimento", width=110)
    tabela.column("espessura", width=100)
    tabela.column("limite", width=90)
    tabela.column("cor", width=80)
    tabela.column("peso", width=80)
    tabela.column("valor", width=80)
    tabela.column("custo", width=90)

    tabela.pack(fill="both", expand=True)

    def carregar_chapas():
        for item in tabela.get_children():
            tabela.delete(item)
        lista = controller_materiais.listar_chapas()
        for linha in lista:
            tabela.insert("", "end", values=(
                linha[0], linha[1], linha[2], linha[3], linha[4],
                linha[5], linha[6], linha[7], linha[8], linha[9]
            ))

    def preencher_formulario():
        item = tabela.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma chapa para editar.")
            return
        valores = tabela.item(item, "values")
        id_chapa_edicao[0] = valores[0]
        entradas_chapa["Descrição"].delete(0, tk.END)
        entradas_chapa["Descrição"].insert(0, valores[1])
        entradas_chapa["Largura (mm)"].delete(0, tk.END)
        entradas_chapa["Largura (mm)"].insert(0, valores[2])
        entradas_chapa["Comprimento (mm)"].delete(0, tk.END)
        entradas_chapa["Comprimento (mm)"].insert(0, valores[3])
        entradas_chapa["Espessura (mm)"].delete(0, tk.END)
        entradas_chapa["Espessura (mm)"].insert(0, valores[4])
        entradas_chapa["Limite Escoamento (MPa)"].delete(0, tk.END)
        entradas_chapa["Limite Escoamento (MPa)"].insert(0, valores[5])
        entradas_chapa["Cor"].delete(0, tk.END)
        entradas_chapa["Cor"].insert(0, valores[6])
        entradas_chapa["Peso (kg)"].delete(0, tk.END)
        entradas_chapa["Peso (kg)"].insert(0, valores[7])
        entradas_chapa["Valor (R$/kg)"].delete(0, tk.END)
        entradas_chapa["Valor (R$/kg)"].insert(0, valores[8])
        entradas_chapa["Custo Total"].delete(0, tk.END)
        entradas_chapa["Custo Total"].insert(0, valores[9])

    def excluir_chapa():
        item = tabela.focus()
        if not item:
            messagebox.showwarning("Aviso", "Selecione uma chapa para excluir.")
            return
        valores = tabela.item(item, "values")
        chapa_id = valores[0]
        confirmacao = messagebox.askyesno("Confirmar", f"Deseja excluir a chapa ID {chapa_id}?")
        if confirmacao:
            if controller_materiais.excluir_chapa(chapa_id):
                messagebox.showinfo("Sucesso", "Chapa excluída com sucesso!")
                carregar_chapas()
            else:
                messagebox.showerror("Erro", "Erro ao excluir chapa.")

    frame_botoes = ttk.Frame(janela)
    frame_botoes.pack(pady=10, anchor="center")
    ttk.Button(frame_botoes, text="✏️ Editar Selecionada", command=preencher_formulario).pack(side="left", padx=10)
    ttk.Button(frame_botoes, text="🗑️ Excluir Selecionada", command=excluir_chapa).pack(side="left", padx=10)

    carregar_chapas()
    ttk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=10)
