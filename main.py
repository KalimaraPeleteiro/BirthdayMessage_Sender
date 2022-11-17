from tkinter import *
from tkinter import ttk


# GUI
window = Tk()
window.title("Birthday Message Sender")

# Criação das Tabs
notebook = ttk.Notebook(window)

tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1, text="Novo Contato")
notebook.add(tab2, text="Contatos Registrados")
notebook.add(tab3, text="Informações Pessoais")
notebook.pack()





# Tab3 - Informações Pessoais
Label(tab3, text="Informações de E-mail", font=('Times New Roman', 20, ''), height=2).pack()



window.mainloop()