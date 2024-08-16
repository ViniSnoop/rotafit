#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import Tk, ttk

janela = tk.Tk()
janela.title("RotaFit")#Título da janela
janela.geometry("600x400")#Tamanho da janela
janela.configure()#Aqui coloca configurações básicas como background.
janela.resizable(0,0)

#Configuração do Grid principal
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

