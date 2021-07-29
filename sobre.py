from tkinter import *

from tkinter import ttk

fonte1=('Verdana','10','bold')

window = Tk()

window.title("EXCEL TO MySQL - MariaDB")
window.iconbitmap('ssii.ico')
window.geometry('500x200')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab_control.add(tab1, text='')

#rsl = open('result.txt')

lbl11 = Label(tab1, text= 'sobre')
lbl11.grid(column=0, row=2)

"""ix = 0

for linha in rsl:
    print(linha)
    valor = linha.split()
    lbl13x = Label(tab1, text= valor)
    lbl13x.grid(column=1, row=3+ix)
    ix = ix + 1

rsl.close()"""

xy =    ["Desenvolvido por Roberto Sanches Martines",
         "para SS Informática Inteligente",
         "",
         "rbtosanches@gmail.com",
         "rbtosanches@ssinformaticainteligente.com.br",
         "http://www.ssinformaticainteligente.com.br"]

print(xy)

ix = 0

for linha in xy:
    print(linha)
    valor = linha.split()
    lbl13x = Label(tab1, text= valor)
    lbl13x.grid(column=1, row=3+ix)
    ix = ix + 1

"""print("Desenvolvido por Roberto Sanches Martines")
print("para SS Informática Inteligente")
print("rbtosanches@gmail.com")
print("rbtosanches@ssinformaticainteligente.com.br")
print("http://www.ssinformaticainteligente.com.br") """

tab_control.pack(expand=1, fill='both')

window.mainloop()