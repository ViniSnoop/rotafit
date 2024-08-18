#importando tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk

#importando dicionario e json
import dicionario
import json

from calculo import calculoDeTempo
#-- Navegação

#Define o frame atual
def mostrarFrame(frame):
    frameInicial.grid_remove()
    frameDeVisu.grid_remove()
    frameDeEscolha.grid_remove()
    
    frame.grid(row=0, column=0, sticky="nsew")
    
#-- Fim Navegação

#-- Função que obtém os resultados escolhidos pelo usuário em Escolher Exercício
quantidadeDeExercicios = []
def obterNumero():
    c=0
    quantidadeDeExercicios.clear()
    for chave in listaDeChavesDeEscolha:
        quantidadeDeExercicios.append(chave.get())
    
    for chave, valor in dicionario.exerciciosDisponiveis.items():
        ttk.Label(frameDeVisu, text="{} 5x {}".format(chave, quantidadeDeExercicios[c]), font=("Helvetica", 12)).grid(row=valor["id"], column=1, padx=5, pady=5, sticky="nsew")
        c+=1
    
    informacoes = open("test.json", "w")
    json.dump(quantidadeDeExercicios, informacoes)
    informacoes.close()

    tempoTotalLocal = calculoDeTempo()
    labelTempo.config(text="{}".format(tempoTotalLocal))

    mostrarFrame(frameDeVisu)

#-- Fim função

#-- Configuração da JANELA
#Config janela
janela = tk.Tk()
janela.title("RotaFit")#Título da janela
janela.geometry()#Tamanho da janela
janela.resizable(0,0)

#Config Grid principal
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

#-- Fim da configuração de JANELA

#-- FrameInicial

#frame
frameInicial = ttk.Frame(janela)
frameInicial.grid()

#mensagem na tela
ttk.Label(frameInicial, text="ROTAFIT", font=("Helvetica", 18)).grid(row=0, column=0, columnspan=1, padx=20, pady=20, sticky="ew")

#botões
ttk.Button(frameInicial, text="Visualizar exercícios", command=lambda: mostrarFrame(frameDeVisu)).grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
ttk.Button(frameInicial, text="Escolher exercícios", command=lambda: mostrarFrame(frameDeEscolha)).grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

#-- Fim FrameInicial


#-- FrameVisualização

frameDeVisu = ttk.Frame(janela)
frameDeVisu.grid()
frameDeVisu.grid_rowconfigure(15, weight=1)
frameDeVisu.grid_columnconfigure(2, weight=0)

#Título
ttk.Label(frameDeVisu, text="Visualização", font=("Helvetica", 18)).grid(row=0, column=0, sticky="e")

#Lado Esquerdo da página
ttk.Button(frameDeVisu, text="Salvar", command=lambda: mostrarFrame(frameInicial)).grid(row=0, column=1, padx=10, pady=10, sticky="sw")
c=0
try:
    for chave, valor in dicionario.exerciciosDisponiveis.items():
        ttk.Label(frameDeVisu, text="{} 5x {}".format(chave, quantidadeDeExercicios[c]), font=("Helvetica", 12)).grid(row=valor["id"], column=1, padx=5, pady=5, sticky="nsew")
        c+=1
except:
    for chave, valor in dicionario.exerciciosDisponiveis.items():
        ttk.Label(frameDeVisu, text="{} 5x {}".format(chave, 0), font=("Helvetica", 12)).grid(row=valor["id"], column=0, padx=5, pady=5, sticky="nsew")
        c+=1
#Lado Direito da Página
ttk.Label(frameDeVisu, text="TEMPO SUGERIDO:", font=("Helvetica", 18)).grid(row=7, column=2, padx=10, pady=10, sticky="ew")
tempoTotalLocal = calculoDeTempo()
labelTempo = ttk.Label(frameDeVisu, text="{}".format(tempoTotalLocal), font=("Helvetica", 18))
labelTempo.grid(row=8, column=2, padx=10, pady=10, sticky="ew")

ttk.Button(frameDeVisu, text="Voltar para página inicial", command=lambda: mostrarFrame(frameInicial)).grid(row=0, column=2, padx=10, pady=10, sticky="se")

#-- Fim FrameVisualização

#-- FrameEscolha

frameDeEscolha = ttk.Frame(janela)
frameDeEscolha.grid()
frameDeEscolha.grid_rowconfigure(15, weight=1)
frameDeEscolha.grid_columnconfigure(3, weight=1)

ttk.Label(frameDeEscolha, text="Escolhas", font=("Helvetica", 18)).grid(row=0, column=1, sticky="ew")
listaDeChavesDeEscolha = []
for chave, valor in dicionario.exerciciosDisponiveis.items():
    ttk.Label(frameDeEscolha, text="{} 5x".format(chave), font=("Helvetica", 12)).grid(row=valor["id"], column=1, padx=5, pady=5, sticky="nsew")
    chave = IntVar()
    listaDeChavesDeEscolha.append(chave)
    ttk.Spinbox(frameDeEscolha, from_=0, to=10, wrap=True, textvariable=chave).grid(row=valor["id"], column=2, padx=5, pady=5, sticky="nsew")

#Botão de envio
ttk.Button(frameDeEscolha, text="Adicionar exercícios", command=lambda: obterNumero()).grid(row=15, column=1, padx=20, pady=1, sticky="sw")

#Botão de retorno
ttk.Button(frameDeEscolha, text="Voltar para página inicial", command=lambda: mostrarFrame(frameInicial)).grid(row=15, column=2, padx=20, pady=1, sticky="se")
#-- Fim FrameEscolha

mostrarFrame(frameInicial)

janela.mainloop()