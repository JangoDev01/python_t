####
"""
    pack -> empacotamento lateral
        -widget alinhados um ao lado do outro vertical ou orizontalmente...
        -um seguido do outro sem nenhum parametro
            btn_red.pack()
            btn_blue.pack()
            -os itens serão organizados na tela orizontalmente e centralizados
        -parametro side="" -> organiza apartir de qual lado
            -right, left, bottom, top -> vem por padrão
        -parametro expend=True -> força um widget a se expandir dependendo
            do espaço em que se encontra...
            -por padrão ele vem com o valor False
        parametro fill="" -> determina se o widget vai efetivamente ocupar o espaço
            desponivel...
            -x -> preencha na orizontal
            -y -> preencha na vertical
            -both -> preencha de ambos os lados
        parametro anchor="" -> ancora ou posicionar um widget em uma direção
            -w -> oeste
            -e -> este
            -n -> norte
            -s -> sul
"""
### Imports ###
import tkinter as tk
from tkinter import ttk, messagebox

### Janela Principal ###
janela_home = tk.Tk()
janela_home.title("Home")
janela_home.geometry("600x400")
janela_home.config(bg="white")

### Funções e Metodos ###
def abrir_janela_login():
    janela_login = tk.Toplevel()
    janela_login.title("login")

    ## impedindo o redimencionamento
    janela_login.resizable(False, False)
    largura_janela_login = 400
    altura_janela_login = 200

    ## obter as dimensões da tela do monitor
    largura_tela = janela_login.winfo_screenwidth()
    altura_tela = janela_login.winfo_screenheight()

    ## calcular as coordenadas para centralizar a janela 2
    x = (largura_tela - largura_janela_login) // 2
    y = (altura_tela - altura_janela_login) // 2
    ## geometria da janela
    janela_login.geometry(f'{largura_janela_login}x{altura_janela_login}+{x}+{y}')

    lbl_login = ttk.Label(janela_login, text="Login", background="lightblue")
    lbl_login.configure(anchor="center")
    lbl_user = ttk.Label(janela_login, text="Usuario:")
    txt_user = ttk.Entry(janela_login)
    lbl_pass = ttk.Label(janela_login, text="Senha:")
    txt_pass = ttk.Entry(janela_login, show="*")
    btn_login = ttk.Button(janela_login, text="Login", command=mostrar_msg)

    lbl_login.pack(fill="both", expand=True)
    lbl_user.pack(anchor="w", padx=10, pady=5)
    txt_user.pack(anchor="w", padx=10, pady=5, fill="x")
    lbl_pass.pack(anchor="w", padx=10, pady=5)
    txt_pass.pack(anchor="w", padx=10, pady=5, fill="x")
    btn_login.pack(anchor="e", padx=10, pady=5)

def mostrar_msg():
    messagebox.showinfo("Alerta", "É Nós seu Cuzão...!")
    janela_home.destroy()

def bg_red():
    lbl_lr = tk.Label(janela_home, text="Red", font=("Arial", 33))
    lbl_lr.pack(pady=10)
    janela_home.config(bg="red")

def bg_blue():
    lbl_lb = tk.Label(janela_home, text="Blue", font=("Arial", 33))
    lbl_lb.pack(pady=10)
    janela_home.config(bg="blue")

def bg_yellow():
    lbl_ly = tk.Label(janela_home, text="Yellow", font=("Arial", 33))
    lbl_ly.pack(pady=10)
    janela_home.config(bg="yellow")

def bg_black():
    lbl_bl = tk.Label(janela_home, text="Black", font=("Arial", 33))
    lbl_bl.pack(pady=10)
    janela_home.config(bg="Black")

### Criação e configuração dos widgets ###
## botões
btn_red = ttk.Button(janela_home, text="Vermelho", width=15, command=bg_red)
btn_blue = ttk.Button(janela_home, text="Azul", width=15, command=bg_blue)
btn_entrar = ttk.Button(janela_home, text="Entrar", width=15, command=abrir_janela_login)
btn_yellow = ttk.Button(janela_home, text="Amarelo", width=15, command=bg_yellow)
btn_black = ttk.Button(janela_home, text="Preto", width=15, command=bg_black)

btn_black.pack(side="top", pady=5, expand=True, fill="x")
btn_red.pack(side="bottom", pady=5, expand=True, fill="x")
btn_entrar.pack(pady=5)
btn_blue.pack(side="left", padx=5,  expand=True, fill="y")
btn_yellow.pack(side="right", padx=5,  expand=True, fill="both")

### 

### main loop ###
janela_home.mainloop()