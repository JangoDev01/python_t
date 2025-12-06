####
import tkinter as tk

# Janela principal
janela = tk.Tk()

icon = 'c:\\Users\\Administrator\\Dev Zone\\Python\\interface grafica\\icons\\code_alt.ico'

janela.title("Home")
janela.iconbitmap(icon)
## aparece em tela cheia
janela.state('zoomed')
###
janela.config(bg="lightblue")
### redimencionamento da janela
janela.geometry("500x400+200+100")

## tamanho maximo
# janela.minsize(300,200)
## tamanho minimo
# janela.maxsize(800,600)


"""
    função contendo as configurações de uma segunda janela...
    que será aberta num evento de click capturado na tela principal...
"""
def abrir_janela2():
    janela_2 = tk.Toplevel()
    janela_2.title("Home")
    janela_2.iconbitmap(icon)

    ## impedindo o redimencionamento
    janela_2.resizable(False, False)

    janela_2.config(bg="#20EE70")
    janela_2.attributes('-alpha', 0.9)

    largura_janela2 = 300
    altura_janela2 = 200

    ## obter as dimensões da tela do monitor
    largura_tela = janela_2.winfo_screenwidth()
    altura_tela = janela_2.winfo_screenheight()

    ## calcular as coordenadas para centralizar a janela 2
    x = (largura_tela - largura_janela2) // 2
    y = (altura_tela - altura_janela2) // 2

    ## geometria da janela
    janela_2.geometry(f'{largura_janela2}x{altura_janela2}+{x}+{y}')

"""
    se um evento de click do botão esquerdo do mouse for capturado a janela 2 será aberta...
    bind() -> faz uma união...
    <Button-1> -> botão esquerdo do mouse
"""
janela.bind("<Button-1>", lambda event: abrir_janela2())

# main loop
janela.mainloop()