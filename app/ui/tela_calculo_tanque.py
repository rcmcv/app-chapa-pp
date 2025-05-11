import tkinter as tk
from tkinter import ttk, messagebox
from app.controllers import controller_calculo_tanque

def abrir_tela_calculo_tanque(dados_edicao=None):
    janela = tk.Toplevel()
    janela.title("Cálculo de Chapas - Tanque Redondo")

    largura = 500
    altura = 450
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
    janela.resizable(False, False)

    frame = ttk.LabelFrame(janela, text="Informações do Tanque")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    tipo_tanque = ttk.Combobox(frame, values=["Redondo"], state="readonly")
    tipo_tanque.set("Redondo")
    entrada_cliente = ttk.Entry(frame)
    entrada_diametro = ttk.Entry(frame)
    entrada_altura = ttk.Entry(frame)
    fundo_tipo = ttk.Combobox(frame, values=["Plano", "Cônico"], state="readonly")
    fundo_tipo.set("Plano")
    tampa_tipo = ttk.Combobox(frame, values=["Nenhuma", "Plano", "Cônico"], state="readonly")
    tampa_tipo.set("Nenhuma")

    campos = [
        ("Tipo de Tanque", tipo_tanque),
        ("Cliente", entrada_cliente),
        ("Diâmetro (mm)", entrada_diametro),
        ("Altura (mm)", entrada_altura),
        ("Tipo de Fundo", fundo_tipo),
        ("Tipo de Tampa", tampa_tipo)
    ]

    for i, (label, widget) in enumerate(campos):
        ttk.Label(frame, text=label).grid(row=i, column=0, sticky="w", padx=5, pady=5)
        widget.grid(row=i, column=1, padx=5, pady=5)

    # Preencher campos se estiver em modo edição
    id_edicao = None
    if dados_edicao:
        id_edicao = dados_edicao[0]
        tipo_tanque.set(dados_edicao[1])
        entrada_cliente.insert(0, dados_edicao[2])
        entrada_diametro.insert(0, dados_edicao[3])
        entrada_altura.insert(0, dados_edicao[4])
        fundo_tipo.set(dados_edicao[5])
        tampa_tipo.set(dados_edicao[6])

    def limpar():
        entrada_cliente.delete(0, tk.END)
        entrada_diametro.delete(0, tk.END)
        entrada_altura.delete(0, tk.END)
        fundo_tipo.set("Plano")
        tampa_tipo.set("Nenhuma")
        tipo_tanque.set("Redondo")

    def calcular():
        try:
            d = float(entrada_diametro.get().replace(",", "."))
            h = float(entrada_altura.get().replace(",", "."))
            fundo = fundo_tipo.get()
            tampa = tampa_tipo.get()
            area_total = 123456.78
            chapas = 4
            sobra = 1523.45
            messagebox.showinfo("Cálculo", f"Área total: {area_total:.2f} mm²\n"
                                           f"Chapas: {chapas}\nSobra: {sobra:.2f} mm²")
        except ValueError:
            messagebox.showerror("Erro", "Preencha corretamente os campos numéricos.")

    def salvar():
        try:
            tipo = tipo_tanque.get()
            cliente = entrada_cliente.get().strip()
            d = float(entrada_diametro.get().replace(",", "."))
            h = float(entrada_altura.get().replace(",", "."))
            fundo = fundo_tipo.get()
            tampa = tampa_tipo.get()
            if not cliente:
                messagebox.showwarning("Aviso", "Informe o nome do cliente.")
                return

            area_total = 123456.78
            chapas = 4
            sobra = 1523.45
            usuario_id = 1

            dados = (
                tipo, cliente, d, h, fundo, tampa,
                area_total, chapas, sobra, usuario_id
            )

            if id_edicao:
                sucesso = controller_calculo_tanque.editar_calculo_tanque(id_edicao, dados)
            else:
                sucesso = controller_calculo_tanque.inserir_calculo_tanque(dados)

            if sucesso:
                messagebox.showinfo("Sucesso", "Cálculo salvo com sucesso!")
                janela.destroy()
            else:
                messagebox.showerror("Erro", "Erro ao salvar cálculo.")
        except ValueError:
            messagebox.showerror("Erro", "Preencha corretamente os campos numéricos.")

    botoes = ttk.Frame(janela)
    botoes.pack(pady=10)
    ttk.Button(botoes, text="🧮 Calcular", command=calcular).pack(side="left", padx=10)
    ttk.Button(botoes, text="💾 Salvar", command=salvar).pack(side="left", padx=10)
    ttk.Button(botoes, text="♻️ Limpar", command=limpar).pack(side="left", padx=10)
