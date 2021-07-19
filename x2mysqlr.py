from tkinter import *

from tkinter import ttk

fonte1=('Verdana','10','bold')

window = Tk()

window.title("Welcome to LikeGeeks app")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='')

rsl = open('result.txt')

lbl11 = Label(tab1, text= 'resultado')
lbl11.grid(column=0, row=2)

ix = 0

for linha in rsl:
    print(linha)
    valor = linha.split()
    lbl13x = Label(tab1, text= valor)
    lbl13x.grid(column=1, row=3+ix)
    ix = ix + 1

rsl.close()

tab_control.pack(expand=1, fill='both')

window.mainloop()