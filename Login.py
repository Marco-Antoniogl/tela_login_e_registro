from tkinter import Tk, Label, Entry, Button, Frame
from tkinter.constants import FLAT, SOLID
from tkinter import ttk
import tkinter as tk
import sqlite3

#Cores
co0 = "#feffff" #branco
co1 = "#00008B" #Darkblue
co4 = "#484D50" #Cinza
co5 = "#191970" #MidnightBlue
#Cores em # https://www.homehost.com.br/blog/tutoriais/tabela-de-cores-html/

#Autenticação de login


def criar_tabela():
    conn = sqlite3.connect("Banco.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cadastro (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        login TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )
""")
    
    conn.commit()
    conn.close()


def fazer_login():
    login = login_entry.get()
    senha = senha_entry.get()

    conn = sqlite3.connect("Banco.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT senha FROM cadastro WHERE login = '{}'".format(login))
        login = cursor.fetchone()

    except sqlite3.Error as e:
        print("Erro ao executar consulta SQL:", e)

    if login == "" and senha == "":
        botao_label.config(text="Login realizado com sucesso!", fg="green")
    else:
        botao_label.config(text="Nome de usuário ou senha inválido!", fg="red")

    conn.close()

#Confg da Janela
janela = Tk()
janela.title("login")
janela.geometry("700x600")
janela.configure(background=co5)
janela.resizable(width=False, height=False)

style = ttk.Style(janela)
style.theme_use("clam")

#Frame

principal = Frame(janela, width=500, height=550, bg=co1, relief=FLAT)
principal.pack(padx=160, pady=120)

#Login

login_label = Label(principal, text="E-mail ou Telefone",  font=("Arial", 12), bg=co1, fg=co0, justify="left" )
login_label.pack(padx= 125, pady=20)

login_entry = Entry(principal,width=30, justify="left", relief=SOLID)
login_entry.pack(pady=0)

#Senha
senha_label = Label(principal, text="Senha",  font=("Arial", 12), bg=co1, fg=co0, justify="left" )
senha_label.pack(pady=20)

senha_entry = Entry(principal,width=30, justify="left", relief=SOLID)
senha_entry.pack(pady=0)

#Botão de login

botao_entry = Button(principal,width=10, justify="left", relief=SOLID, text="Entrar", command=fazer_login)
botao_entry.pack(pady=50)

botao_label = Label(principal, text="", bg=co1,fg=co1)
botao_label.pack()

criar_tabela()

janela.mainloop()