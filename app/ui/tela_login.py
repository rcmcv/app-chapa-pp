import tkinter as tk
from tkinter import messagebox
from app.ui import tela_principal

def iniciar_tela_login():
    root = tk.Tk()
    root.title("App Chapa PP - Login")

     # Define o tamanho da janela
    largura_janela = 300
    altura_janela = 200

    # Obtém tamanho da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcula posição x e y
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)

    # Aplica tamanho e posição centralizada
    root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")
    root.resizable(False, False)

    tk.Label(root, text="Usuário").pack(pady=5)
    entrada_usuario = tk.Entry(root)
    entrada_usuario.pack()

    tk.Label(root, text="Senha").pack(pady=5)
    entrada_senha = tk.Entry(root, show="*")
    entrada_senha.pack()

    def login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if usuario == "admin" and senha == "123":
            messagebox.showinfo("Login", "Login realizado com sucesso!")
            root.destroy()
            tela_principal.abrir_tela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    tk.Button(root, text="Entrar", command=login).pack(pady=10)
    root.mainloop()
