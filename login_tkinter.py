import customtkinter as ctk
from tkinter import messagebox


def verificar_credenciais():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "a" and senha == "a":
        messagebox.showinfo("Login bem-sucedido", "Login realizado com sucesso!")
        nova_janela()  
        
    else:
        messagebox.showerror("Login falhou", "Credenciais inválidas. Tente novamente.")


def nova_janela():
    janela = ctk.CTkToplevel(janela_login)
    janela.title("Nova Janela")
    janela.geometry("400x200")

    texto = ctk.CTkLabel(janela, text="Nova janela")
    texto.pack()


janela_login = ctk.CTk()
janela_login.title("Sistema de Login")
janela_login.geometry("400x200")

texto = ctk.CTkLabel(janela_login, text="Fazer Login")
texto.pack(padx=10,pady=10)

entry_usuario = ctk.CTkEntry(janela_login, placeholder_text="Usuário...", )
entry_usuario.pack(padx=10,pady=10)

entry_senha = ctk.CTkEntry(janela_login, placeholder_text="Senha...", show="*")  
entry_senha.pack(padx=10,pady=10)

checkbox = ctk.CTkCheckBox(janela_login, text="Lembrar Login")
checkbox.pack(padx=10, pady=10)


botao_login = ctk.CTkButton(janela_login, text="Login", command=verificar_credenciais)
botao_login.pack(padx=10,pady=10)

janela_login.mainloop()
