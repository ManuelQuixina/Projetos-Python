# Ola pessoal, eu sou o Manuel Quixina.
# Este é mais um dos meus pequenos projectos em Python.
# Trata-se de um Sistema de Login feito a biblioteca Tkinter.


# O programa é relativamente simples e fácil de compreender.
# Modo de uso:
# Se introduzires o nome de utilizador correcto, no widget do Nome 


from tkinter import *


cores = ["black", "white", "green", "#57d41e", "#4fde0d", "#0f13e8", "yellow", "blue", "red"]
utilizador = "José Cardoso"
senha = "0000"

janela = Tk() 
janela.title("                            Sistema de Login básico") 
janela.geometry("415x255")
janela.config(bg = cores[0]) 
janela.resizable(width = False, height = False)

def mostrar_dados():
    dados_nome = entry_nome.get()
    dados_senha = entry_senha.get()
    print(dados_nome, dados_senha)

    if entry_nome.get() == utilizador:
        label_nome ["text"] = "Utilizador definido"
        label_nome ["bg"] = cores[2]
        label_nome ["fg"] = cores[0]
    else:
        label_nome ["text"] = "Utilizador não definido"
        label_nome ["bg"] = cores[8]
        label_nome ["fg"] = cores[1]
        entry_senha.delete(0, END)
        entry_senha(state = "disable")

    if entry_senha.get() == senha:
        label_senha ["text"] = "Senha Correta"
        label_senha ["bg"] = cores[3]
        label_senha ["fg"] = cores[1]
    else:
        label_senha ["text"] = "Senha Incorreta"
        label_senha ["bg"] = cores[8]
        label_senha ["fg"] = cores[1]

    #entry_nome.delete(0, END)
    #entry_senha.delete(0, END)


label_nome = Label (janela, width = 30, height = 1, text = "Nome do Utilizador:  ", bg = cores[5], fg = cores[1], font = "Calibri 10")
label_nome.pack(pady = 3)
entry_nome = Entry (janela, width = 25, fg = cores[7])
entry_nome.pack(pady = 2)

label_senha = Label (janela, width = 30, height = 1, text = "Digite a senha: ", bg = cores[5], fg = cores[1], font = "Calibri 10")
label_senha.pack(pady = 2)
entry_senha = Entry (janela, width = 25, fg = cores[7])
entry_senha.pack(pady = 2)

botao_entrar = Button (width = 40, height = 1, text = "Entrar: ", bg = cores[5], fg = cores[1], command = mostrar_dados)
botao_entrar.pack(pady = 2)

label_entrar = Label (janela, width = 30, height = 1, text = "", bg = cores[0])
label_entrar.pack(pady = 20)


mainloop()