from tkinter import Frame
from janela import janela

#Esconde o frame anterior
def esconderFrames():
    for widget in janela.winfo_children():
        widget.grid_forget()

#Define o frame atual
def mostrarFrame(frame):
    esconderFrames()
    frame.grid(row=0, column=0, sticky="nsew")
    frame.lift()