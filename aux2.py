from io import UnsupportedOperation
import tkinter as tk
from tkinter import filedialog

class Tela:
    def __init__(self, master):
        self.nossaTela = master
        self.criaWidgets()

    def criaWidgets(self):

        self.lbl1 = tk.Label(self.nossaTela, text="servidor:", font=('Arial',12))
        self.entradaServidor = tk.Entry(self.nossaTela,font=('Arial',12))

        self.lbl2 = tk.Label(self.nossaTela, text="porta:", font=('Arial',12))
        self.entradaPorta = tk.Entry(self.nossaTela,font=('Arial',12))

        self.lbl3 = tk.Label(self.nossaTela, text="usuário:", font=('Arial',12))
        self.entradaUsuario = tk.Entry(self.nossaTela,font=('Arial',12))

        self.lbl4 = tk.Label(self.nossaTela, text="senha:", font=('Arial',12))
        self.entradaSenha = tk.Entry(self.nossaTela, show="*", font=('Arial',12))

        self.lbl5 = tk.Label(self.nossaTela, text="db:", font=('Arial',12))
        self.entradaDB = tk.Entry(self.nossaTela,font=('Arial',12))

        self.cadastra = tk.Button(self.nossaTela, text="Cadastrar", command=self.salvar)

        self.lbl1.grid(column = 0)
        self.entradaServidor.grid(row = 0,column = 1, padx=20)
        self.lbl2.grid(row=1,column=0)
        self.entradaPorta.grid(row = 1,column = 1, padx=20)
        self.lbl3.grid(row=2,column=0)
        self.entradaUsuario.grid(row = 2,column = 1, padx=20)
        self.lbl4.grid(row=3,column=0)
        self.entradaSenha.grid(row = 3,column = 1, padx=20)
        self.lbl5.grid(row=4,column=0)
        self.entradaDB.grid(row = 4,column = 1, padx=20)

        self.cadastra.grid(row = 5,column=0,columnspan=2,pady=20)

    def salvar(self):
        servidor = 'db_host = "'     + self.entradaServidor.get() + '"'
        porta    = 'db_port = "'     + self.entradaPorta.get()    + '"'
        usuario  = 'db_user = "'     + self.entradaUsuario.get()  + '"'
        senha    = 'db_password = "' + self.entradaSenha.get()    + '"'
        db       = 'db_database = "' + self.entradaDB.get()       + '"'

        erro = "0"

        if (servidor == "") or (porta == "") or (usuario == "") or (senha == "") or (db == ""):
            erro = "1"

        if (erro == "0"):
            dados = open('config.py',"w")

            dados.write('{}\n{}\n{}\n{}\n{}\n'.format(servidor,porta,usuario,senha,db))

            dados.close()
        else:
            print("Erro")

janelaRaiz = tk.Tk()
janelaRaiz.title("EXCEL TO MySQL - MariaDB")
janelaRaiz.iconbitmap('ssii.ico')
janelaRaiz.geometry('350x200')
Tela(janelaRaiz)
janelaRaiz.mainloop()