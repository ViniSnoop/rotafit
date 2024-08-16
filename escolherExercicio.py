#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, ttk

#importando modulos
from navegação import mostrarFrame

def criarEscolherExercicio(janela):
    frameDeEscolha = ttk.Frame(janela)
    frameDeEscolha.grid(row=0, column=0, sticky="nsew")

    return frameDeEscolha