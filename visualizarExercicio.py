#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, ttk

#importando modulos
from navegação import mostrarFrame

def criarVisualizarExercicio(janela):
    frameDeVisu = ttk.Frame(janela)
    frameDeVisu.grid(row=0, column=0, sticky="nsew")

    ttk.Label(frameDeVisu, text="ROTAFIT").grid(row=0, column=0, sticky="nsew")
    ttk.Button(frameDeVisu, text="Voltar para página inicial", command=lambda: janela.mostrarFrame(janela.frameInicial)).grid(row=1, column=0, sticky="nsew")
    
    return frameDeVisu