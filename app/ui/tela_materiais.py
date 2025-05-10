import tkinter as tk
from tkinter import ttk

def abrir_tela_materiais():
    janela = tk.Toplevel()
    janela.title("Cadastro de Materiais")

    # Define o tamanho da janela
    largura_janela = 700
    altura_janela = 500

    # # Obtém tamanho da tela
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula posição x e y
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)

    # Aplica tamanho e posição centralizada
    janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    janela.resizable(False, False)

    # Seção: Cadastro de Chapa
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

    # Seção: Cadastro de Solda
    frame_solda = ttk.LabelFrame(janela, text="Cadastro de Solda")
    frame_solda.pack(fill="x", padx=10, pady=10)

    campos_solda = [
        ("Descrição", 0), ("Peso (kg)", 1),
        ("Valor (R$/kg)", 2), ("Custo Total", 3)
    ]

    entradas_solda = {}
    for label, row in campos_solda:
        ttk.Label(frame_solda, text=label).grid(row=row, column=0, sticky="w", padx=5, pady=2)
        entrada = ttk.Entry(frame_solda)
        entrada.grid(row=row, column=1, padx=5, pady=2)
        entradas_solda[label] = entrada

    # Botão de fechar
    ttk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=10)
