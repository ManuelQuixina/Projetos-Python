# 18/07/2025
# Ola pessoal mais uma vez. Eu sou o Manuel Cardoso
# Desta vez vim com mais um pequeno projrcto em python.
# Quero dizer que ainda sou um Programador iniciante

# desta vez crie um aplicativo que se chama "Gerador de Senha"
# Ele é bem simples e facil de usar.



from tkinter import *
from tkinter import ttk 
import string
import random
from tkinter import messagebox

#from PIL import ImageTK, Image


# lista de cores

cor1 = "black"
cor2 = "white"
cor3 = "red"

janela = Tk()
janela.title ("Projecto 2")
janela.config(bg = cor2)
janela.geometry("300x400")
janela.resizable(width=False, height=False)

# Dividindo a tela ----------------------------------------------------------------------------------
frame_cima = Frame (janela, width=300, height=50, bg = cor1, padx=0, pady=0, relief="flat")
frame_cima.grid(row = 0, column = 0, sticky=NSEW)

frame_baixo = Frame (janela, width=300, height=350, bg = "grey", padx=0, pady=0, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW)


# logica do app --------------------------------------------------------------------------------------------

def gerar_senha():
    alfa_maior = string.ascii_uppercase
    alfa_menor = string.ascii_lowercase
    numeros = "0123456789"
    simbolos = "()*:;,._-/[]"

    global combinar 

    if estado_1.get() == alfa_maior:
        combinar = alfa_maior
    else:
        pass

    if estado_2.get() == alfa_menor:
        combinar = combinar + alfa_menor
    else:
        pass

    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
        pass

    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
        pass

    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento))
    app_senha ["text"] = senha

def copiar_senha():
    info = senha
    frame_baixo.clipboard_clear()
    frame_baixo.clipboard_append(info)
    messagebox.showinfo("Sucesso", "A senha foi copiada com sucesso")

# Trabalhando no frame cima -------------------------------------------------------------------------
estilo = ttk.Style(janela)
estilo.theme_use("clam")

#img = Image.open("foto 1.PNG")
#img = Image.resize((30, 30), Image.ANTIALIAS)
#img = ImageTK.PhotoImage(img)

#app_logo = Label (frame_cima, height=70, image=img, compound=LEFT, padx=10, relief="flat", anchor="nw", bg = cor2)
#app_logo.place(x=2, y=0)
label_titulo = Label (frame_cima, width=30, height=2, bg = "grey", fg = "black", text = "Gerador de Senhas", font = "Arial 15 bold")
label_titulo.grid(row=0, column=0, sticky=NSEW)

label_linha = Label(frame_cima, width=53, height=0, bg = "Red")
label_linha.grid(row=1, column=0, pady=1)

# Trabalhando no frame baixo --------------------------------------------------------------------------------------------------------------------------------------------------

app_senha = Label (frame_baixo, text = "--------------", width=20, height=2, padx=0, relief="solid", anchor="center", font="Ivy 12 bold", bg = cor2, fg = cor1)
app_senha.grid(row=0, column=0, sticky=NSEW, padx=3, pady=5)

botao_copiar = Button (frame_baixo, width=5, command=copiar_senha, height=2, relief="groove", text="Copiar", bg = cor2, fg = cor1)
botao_copiar.grid(row=0, column=1, padx=2, pady=5, sticky=NSEW)

app_info = Label (frame_baixo, text = "Número total de caracteres na senha: ", height=1, padx=0, relief="flat", anchor="center", font="Arial 10 bold", bg = "grey", fg = cor1)
app_info.grid(row=1, column=0, sticky=NSEW, padx=1, pady=2)

dados = IntVar()
dados.set(0)
spin = Spinbox (frame_baixo, from_=0, to=20, width=5, textvariable=dados, relief="sunken")
spin.grid(row=2, column=0, pady=2)

alfa_maior = string.ascii_uppercase
alfa_menor = string.ascii_lowercase
numeros = "0123456789"
simbolos = "()*:;,._-/[]"

frame_caractere =  Frame(frame_baixo, width=350, height=350, bg="grey", pady = 0, padx=0, relief="flat")
frame_caractere.grid(row=3, column=0, sticky=NSEW)

estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton (frame_caractere, height=1, var = estado_1, onvalue=alfa_maior, offvalue="off", relief="flat", bg = "grey", text="ABC Maiúsculas")
check_1.grid(row=0, column=0, sticky=NW, padx=5, pady=8)

estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton (frame_caractere, height=1, var = estado_2, onvalue=alfa_menor, offvalue="off", relief="flat", bg = "grey", text="ABC Minusculas")
check_2.grid(row=1, column=0, sticky=NW, padx=5, pady=8)


estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton (frame_caractere, height=1, var = estado_3, onvalue=numeros, offvalue="off" , relief="flat", bg = "grey", text="123 Números")
check_3.grid(row=2, column=0, sticky=NW, padx=5, pady=8)

estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton (frame_caractere, height=1, var = estado_4, onvalue=simbolos, offvalue="off" , relief="flat", bg = "grey", text="Símbolos [];,:()")
check_4.grid(row=3, column=0, sticky=NW, padx=5, pady=8)

botao_gerar = Button(frame_caractere, height=1, width=10, command=gerar_senha, bg = "red", fg = "white", relief="groove", text="Gerar Senha")
botao_gerar.grid(row=4, column=1, pady=2)





janela.mainloop()