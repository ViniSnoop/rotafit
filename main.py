#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, ttk
from janela import janela
from paginaInicial import criarPaginaInicial
from escolherExercicio import criarEscolherExercicio
from visualizarExercicio import criarVisualizarExercicio
from navegação import mostrarFrame

frameInicial = criarPaginaInicial(janela)
frameDeVisu = criarVisualizarExercicio(janela)
frameDeEscolha = criarEscolherExercicio(janela)

janela.frameDeVisu = frameDeVisu
janela.frameDeEscolha = frameDeEscolha

mostrarFrame(frameInicial)

janela.mainloop()