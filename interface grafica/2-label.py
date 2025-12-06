####
import tkinter as tk

"""
    o modulo ttk tem mais suporte pra modelos personalizados dos widget
    o modulo PhotoImage permite manipular uma imagem dentro de uma label
"""
from tkinter import ttk, PhotoImage

### janela
janela = tk.Tk()
janela.title("Home - labels")
janela.geometry("800x400")
janela.config(bg="blue")

### Criar Labels

######### Labels simples #########
label = tk.Label(janela, text="Labels simples")
## empacotar o label na janela
label.pack()

######### Labels simples com o ttk #########
label_2 = ttk.Label(
    janela,
    text="Label simples usando com o ttk",
    font=("Helvetica", 18),
    foreground="purple", # cor do texto
    background="lightgreen", # cor de fundo da label
    anchor="center", # centralizar o conteudo no centro da label
    borderwidth=3, # expressura da borda
    relief="groove" # relevo ou linha fina em volta da label
)

label_3 = ttk.Label(
    janela,
    text="Segunda label simples usando o ttk",
    font=("Arial", 33),
    foreground="blue", # cor do texto
    background="lightblue", # cor de fundo da label
    anchor="center", # centralizar o conteudo no centro da label
    borderwidth=3, # expressura da borda
    relief="groove" # relevo ou linha fina em volta da label
)

"""
    posicionando o label
    ipadx -> deslocamento da janela entre a borda do eixo x
    ipady -> deslocamento da janela entre a borda do eixo y
"""
label_2.pack(pady=20, ipadx=10, ipady=30)
label_3.pack(ipadx=10, ipady=60)

######### Label contendo imagem #########
def centr_img(event):
    # 
    largura_janela = janela.winfo.width()
    altura_janela = janela.winfo.height()
    largura_img = img.width()
    altura_img = img.height()

    #
    posicao_x = (largura_janela - largura_img) // 2
    posicao_y = (altura_janela - altura_img) // 2

    label_img.place(x=posicao_x, y=posicao_y)

img = PhotoImage(file="c:\\Users\\Administrator\\Dev Zone\\Python\\interface grafica\\img\\code_alt.png")

label_img = ttk.Label(
    janela,
    text="Exibindo imagem",
    font=("Arial", 12),
    background='black',
    image=img
)

"""
    <Configure> -> parametro para executar uma configuração
"""
janela.bind("<Configure>", centr_img)

label_img.pack(pady=20)

### main loop
janela.mainloop()