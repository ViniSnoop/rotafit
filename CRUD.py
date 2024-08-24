import csv
import dicionario
import tkinter as tk
from tkinter import filedialog
# Criar o Primeiro CSV

fields = ['Nome', 'grupo', 'tempo', 'id','qtd']
exercicios = dicionario.exerciciosDisponiveis
qtd_Lista = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def create_csv():
    exercicios_dict = {}
    for nome, detalhes in exercicios.items():
        exercicios_dict[nome] = {
            'Nome': nome,
            'grupo': detalhes.get('grupo'),
            'tempo': detalhes.get('tempo'),
            'id': detalhes.get('id'),
            'qtd': detalhes.get('qtd')
        }
    return exercicios_dict

# Função para abrir a janela de seleção de arquivo e carregar o CSV (R = Read)
def read_csv():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename(defaultextension=".csv",
                                           filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])

    if file_path:  # Se o usuário não cancelar
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return data

# Atualiza o treino (U = Update)

def update_csv(treinos):
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])

    if file_path:  # Se o usuário não cancelar

        with open(file_path, 'w', newline='') as f:
            fields = treinos[0].keys()  # Pegando as chaves como campos
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(treinos)

