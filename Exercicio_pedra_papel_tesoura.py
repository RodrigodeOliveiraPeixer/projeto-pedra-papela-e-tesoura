import tkinter
from tkinter import *
from tkinter import ttk

# cores --------------------------------
co0 = "#FFFFFF"  # white 
co1 = "#333333"  # black
co2 = "#fcc058"  # orange 
co3 = "#38576b" # valor
co4 = "#3297a8"  # blue
co5 = "#fff873"  # yellow 
co6 = "#34eb3d"   # green / verde
co7 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"


# Configuração da janela

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

app_linha = Label(frame_cima, text="", width=255, anchor='center', font=('ivy 1 bold'), bg=co5, fg=co0)
app_linha.place(x=0, y=95)



janela.mainloop()



