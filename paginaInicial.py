#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, ttk

from navegação import mostrarFrame

#Página inicial
def criarPaginaInicial(janela):
    frameInicial = ttk.Frame(janela)
    frameInicial.grid(row=0, column=0, sticky="nsew")

    ttk.Label(frameInicial, text="ROTAFIT").grid(row=0, column=0, sticky="nsew")
    
    #Botões
    ttk.Button(frameInicial, text="Visualizar exercícios", command=lambda: mostrarFrame(janela.frameDeVisu)).grid(row=1, column=0, sticky="nsew")
    ttk.Button(frameInicial, text="Escolher exercícios", command=lambda: mostrarFrame(janela.frameDeEscolha)).grid(row=1, column=1, sticky="nsew")

    return frameInicial