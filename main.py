#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, ttk

#importando Pillow
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("RotaFit")#Título da janela
janela.geometry("600x400")#Tamanho da janela
janela.configure()#Aqui coloca configurações básicas como background.
janela.resizable(0,0)

#Configuração do Grid principal
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

#Página inicial
frameInicial = ttk.Frame(janela)
frameInicial.grid(row=0, column=0, sticky="nsew")

#Página de escolha
frameDeEscolha = ttk.Frame(janela)
frameDeEscolha.grid(row=0, column=0, sticky="nsew")

#Função para passar para a página de escolha de exercicios
def EscolherExercicio():
    frameDeEscolha.tkraise()

#Função para retornar para a página inicial
def VoltarPaginaInicial():
    frameInicial.tkraise()


#Conteúdo da página inicialitulo = 
ttk.Label(frameDeEscolha, text="Escolha/Altere seu exercício!").grid(column=1, row=0, sticky=tk.EW)

frameInicial.tkraise()

janela.mainloop()