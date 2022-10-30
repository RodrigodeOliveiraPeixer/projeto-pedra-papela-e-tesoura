from ctypes.wintypes import PCHAR
import tkinter
from tkinter import *
from tkinter import ttk


#necessário importar pillow para manipular imagens

from PIL import Image, ImageTk

import random

# cores --------------------------------
co0 = "#FFFFFF"  # white 
co1 = "#333333"  # black
co2 = "#fcc058"  # orange 
co3 = "#38576b" # valor
co4 = "#3297a8"  # blue
co5 = "#fff873"  # yellow 
co6 = "#34eb3d"   # green 
co7 = "#e85151"   # red 
fundo = "#3b3b3b"


# Configuração da janelA

janela = Tk()
janela.title('')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Dividindo a jenela

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)

frame_baixo = Frame(janela, width=260, height=180, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)


estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando os frame cima usuário

app_1 = Label(frame_cima, text="Você", height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
app_1.place(x=25, y=70)
app_1_linha = Label(frame_cima, text="", height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
app_1_linha.place(x=0, y=0)
app_1_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_1_pontos.place(x=50, y=20)


app_ = Label(frame_cima, text=":", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_.place(x=125, y=20)

#configurando os frame cima PC

app_2_pontos = Label(frame_cima, text="0", height=1, anchor='center', font=('ivy 30 bold'), bg=co1, fg=co0)
app_2_pontos.place(x=170, y=20)
app_2 = Label(frame_cima, text="PC", height=1, anchor='center', font=('ivy 10 bold'), bg=co1, fg=co0)
app_2.place(x=205, y=70)
app_2_linha = Label(frame_cima, text="", height=10, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
app_2_linha.place(x=255, y=0)

#linha de empate

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('ivy 1 bold'), bg=co0, fg=co0)
app_linha.place(x=0, y=95)


#mostrando o que o PC está jogando

app_PC = Label(frame_baixo, text="", height=1, anchor='center', font=('ivy 10 bold'), bg=co0, fg=co0)
app_PC.place(x=190, y=10)

#---------------------------------------------------------------------//-------------------------------------------------------------------------
#variaveis globais

global voce 
global pc
global jogadas
global pontos_voce
global pontos_pc

pontos_voce = 0
pontos_pc = 0
jogadas = 5




#função iniciar o jogo

def  jogar(i):
    global jogadas
    global pontos_voce
    global pontos_pc

    if jogadas > 0:
        print(jogadas)
        opcoes = ["Pedra", "Papel", "Tesoura"]
        pc = random.choice(opcoes)

        voce = i

        app_PC["text"] = pc
        app_PC["fg"] = co1

        #Em caso de empate
        if voce == "Pedra" and pc == "Pedra":
            print("Empate")
            app_1_linha["bg"] = co0
            app_2_linha["bg"] = co0
            app_linha["bg"] = co5
        
        elif voce == "Papel" and pc == "Papel":
            print("Empate")
            app_1_linha["bg"] = co0
            app_2_linha["bg"] = co0
            app_linha["bg"] = co5
        
        elif voce == "Tesoura" and pc == "Tesoura":
            print("Empate")
            app_1_linha["bg"] = co0
            app_2_linha["bg"] = co0
            app_linha["bg"] = co5


        #caso não seja empate você escolhendo Pedra !!!!

        elif voce == "Pedra" and pc == "Papel":
            print("Vitória do PC!!")
            app_1_linha["bg"] = co7
            app_2_linha["bg"] = co6
            app_linha["bg"] = co0

            pontos_pc += 10

        elif voce == "Pedra" and pc == "Tesoura":
            print("Você ganhou!")
            app_1_linha["bg"] = co6
            app_2_linha["bg"] = co7
            app_linha["bg"] = co0

            pontos_voce += 10

        

        #caso não seja empate você escolhendo Papel !!!!

        elif voce == "Papel" and pc == "Pedra":
            print("Você ganhou!")
            app_1_linha["bg"] = co6
            app_2_linha["bg"] =co7
            app_linha["bg"] = co0

            pontos_voce += 10

        

        elif voce == "Papel" and pc == "Tesoura":
            print("Vitória do PC !!")
            app_1_linha["bg"] = co7
            app_2_linha["bg"] = co6
            app_linha["bg"] = co0

            pontos_pc += 10

        #caso não seja empate você escolhendo Tesoura !!!!    

        elif voce == "Tesoura" and pc == "Pedra":
            print("Vitória do PC !!")
            app_1_linha["bg"] = co7
            app_2_linha["bg"] = co6
            app_linha["bg"] = co0

            pontos_pc += 10

        elif voce == "Tesoura" and pc == "Papel":
            print("Você ganhou!")
            app_1_linha["bg"] = co6
            app_2_linha["bg"] = co7
            app_linha["bg"] = co0

            pontos_voce += 10

        #atualizando a pontuação
        app_1_pontos["text"] = pontos_voce
        app_2_pontos["text"] = pontos_pc

        #atualizando o número de jogadas
        jogadas -= 1






    
    else:
        fim_do_jogo()







#função lógica do jogo


def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    icon_1 = Image.open('images/pedra.png')
    icon_1 = icon_1.resize((50,50), Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo,command=lambda: jogar("Pedra"), width=50, image=icon_1, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief= FLAT)
    b_icon_1.place(x=15, y=60)

    icon_2 = Image.open('images/papel.png')
    icon_2 = icon_2.resize((50,50), Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda: jogar("Papel"), width=50, image=icon_2, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief= FLAT)
    b_icon_2.place(x=95, y=60)

    icon_3 = Image.open('images/tesoura.png')
    icon_3 = icon_3.resize((50,50), Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda: jogar("Tesoura"), width=50, image=icon_3, compound=CENTER, bg=co0, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief= FLAT)
    b_icon_3.place(x=180, y=60)

#terminar o jogo
def fim_do_jogo():
    print("Fim do jogo!")



#---------------------------------------------------------------------//-------------------------------------------------------------------------

#configurando botão iniciar

b_jogar = Button(frame_baixo, command= iniciar_jogo, width=30, text='Jogar', bg=fundo, fg=co0, font=('Ivy 10 bold'), anchor=CENTER, relief= RAISED, overrelief=RIDGE)
b_jogar.place(x=5, y=151)


janela.mainloop()



