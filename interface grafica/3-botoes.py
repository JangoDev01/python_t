####
### Imports ###
import tkinter as tk
from datetime import date

### janela principal ###
janela_home = tk.Tk()
janela_home.title("Home")
janela_home.geometry("1000x600")

### Funções e Metodos ###
def mostrar_data():
    hoje = date.today()
    texto_data.set(hoje.strftime("%d/%m/%Y"))

def fechar_janela():
    janela_home.destroy()

### carregamento de itens externos ###
img_btn_close = tk.PhotoImage(file="c:\\Users\\Administrator\\Dev Zone\\Python\\interface grafica\\img\\link_external.png")

### criação e configuração dos widgets ###
texto_data = tk.StringVar()

# labels
label_data = tk.Label(
    janela_home,
    textvariable=texto_data,
    font=("Arial", 33),
    foreground="blue",
    background="lightblue", 
    anchor="center", 
    borderwidth=3
)

# botões
btn_data = tk.Button(
    janela_home,
    text="Mostrar Data",
    command=mostrar_data,
    bg="blue",
    fg="white"
)

btn_fechar = tk.Button(
    janela_home,
    image=img_btn_close,
    command=fechar_janela,
    bg="black"
)

### exibição dos widgets ###
label_data.pack(pady=20)
btn_data.pack(pady=10)
btn_fechar.pack(pady=10,)

### loop main ###
janela_home.mainloop()