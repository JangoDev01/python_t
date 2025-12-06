####

import tkinter as tk

### Instanciando uma janela na memoria da maquina
janela = tk.Tk()

"""
    configurando a janela
    title() -> titulo da janela:
        aparece no topo da janela
    geometry() -> define altura, largura, distancia entre os lados da tela com a janela
"""
janela.title("Primeiro App")
janela.geometry("1000x500+20+20")

### imprimir mensagem na janela
label_msg = tk.Label(janela, text="Olá Mundo!")
## manipulando a geometria de widget com o pack()
label_msg.pack()
##
janela.mainloop()