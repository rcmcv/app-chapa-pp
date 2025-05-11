import tkinter as tk
from tkinter import Menu
from app.ui import tela_materiais
from app.ui.tela_calculo_tanque import abrir_tela_calculo_tanque
from app.ui.listar_calculos_tanque import abrir_listagem_calculos


def abrir_tela_principal():
    root = tk.Tk()
    root.title("App Chapa PP - Principal")

    # Define o tamanho da janela
    largura_janela = 800
    altura_janela = 500

    # Obtém tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula posição x e y
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)

    # Aplica tamanho e posição centralizada
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    root.resizable(False, False)

    # Menu superior
    menubar = Menu(root)

    menu_cadastros = Menu(menubar, tearoff=0)
    menu_cadastros.add_command(label="Materiais", command=tela_materiais.abrir_tela_materiais)
    menubar.add_cascade(label="Cadastros", menu=menu_cadastros)

    # Menu Cálculos
    menu_calculos = tk.Menu(menubar, tearoff=0)
    menu_calculos.add_command(label="Tanque Redondo", command=abrir_tela_calculo_tanque)
    menu_calculos.add_command(label="Histórico de Cálculos", command=abrir_listagem_calculos)
    menubar.add_cascade(label="Cálculos", menu=menu_calculos)


    menu_sair = Menu(menubar, tearoff=0)
    menu_sair.add_command(label="Sair", command=root.destroy)
    menubar.add_cascade(label="Sistema", menu=menu_sair)

    root.config(menu=menubar)
    root.mainloop()
