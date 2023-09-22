import tkinter as tk
from tkinter import messagebox

def verificar_credenciais():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "a" and senha == "a":
        messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso!")
        janela_login.destroy()
        nova_janela_painel()  
    else:
        messagebox.showerror("Login falhou", "Credenciais inválidas. Tente novamente.")

def nova_janela_painel():
    janela_painel = tk.Tk()
    janela_painel.title("Painel")

    texto_orientacao = tk.Label(janela_painel, text="Funcionando!! ")
    texto_orientacao.pack()



janela_login = tk.Tk()
janela_login.title("Sistema de Login")

label_usuario = tk.Label(janela_login, text="Usuário:")
label_usuario.pack()
entry_usuario = tk.Entry(janela_login, width="20")
entry_usuario.pack()

label_senha = tk.Label(janela_login, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(janela_login, width="20",show="*")  
entry_senha.pack()

# Botão de login
botao_login = tk.Button(janela_login, text="Login", width= "20", command=verificar_credenciais)
botao_login.pack()

# Executa a janela
janela_login.mainloop()
