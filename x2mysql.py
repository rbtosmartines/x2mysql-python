from tkinter import *

import os

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def verConfig(root):
    os.system("x2mysql1.py")

def mudarConfig(root):
    os.system("x2mysql2.py")

def csv(root):
    os.system("x2mysql_csv.py")

def ods(root):
    os.system("x2mysql_ods.py")

def xls(root):
    os.system("x2mysql_xls.py")

def xlsx(root):
    os.system("x2mysql_xlsx.py")
   
root = Tk()

root.geometry('300x200')

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Ver", command=lambda root=root:verConfig(root))
filemenu.add_command(label="Atualizar", command=lambda root=root:mudarConfig(root))
filemenu.add_separator()
filemenu.add_command(label="Sair", command=root.quit)
menubar.add_cascade(label="Configuração", menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="csv", command=lambda root=root:csv(root))
editmenu.add_command(label="ods", command=lambda root=root:ods(root))
editmenu.add_command(label="xls", command=lambda root=root:xls(root))
editmenu.add_command(label="xlsx", command=lambda root=root:xlsx(root))
menubar.add_cascade(label="Planilha", menu=editmenu)

resultmenu = Menu(menubar, tearoff=0)
resultmenu.add_command(label="Ver", command=donothing)
menubar.add_cascade(label="Resultado", menu=resultmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Index", command=donothing)
helpmenu.add_command(label="Sobre...", command=donothing)
menubar.add_cascade(label="Ajuda", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()