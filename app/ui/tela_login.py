import tkinter as tk
from tkinter import messagebox

def iniciar_tela_login():
    root = tk.Tk()
    root.title("App Chapa PP - Login")
    largura_janela = 300
    altura_janela = 200

    # Obter largura e altura da tela
    largura_tela = root.winfo_screenwidth()
    altura_tela = root.winfo_screenheight()

    # Calcular posição x, y para centralizar
    x = (largura_tela // 2) - (largura_janela // 2)
    y = (altura_tela // 2) - (altura_janela // 2)

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
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")

    tk.Button(root, text="Entrar", command=login).pack(pady=10)
    root.mainloop()
