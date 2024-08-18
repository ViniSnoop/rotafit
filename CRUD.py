import csv
import dicionario
import tkinter as tk
from tkinter import filedialog
# Criar o Primeiro CSV

fields = ['Nome', 'grupo', 'tempo', 'id','qtd']
exercicios = dicionario.exerciciosDisponiveis
qtd_Lista = dicionario.qtdExercicios

def save_csv():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                             filetypes=[("CSV files", "*.csv")])

    if file_path:  # Se o usuário não cancelar

        with open(file_path, 'w', newline='') as f:
            w = csv.DictWriter(f, fields)
            w.writeheader()
            for i, k in enumerate(exercicios):
                linha = {field: exercicios[k].get(field) or k for field in fields[:-1]}
                linha['qtd'] = qtd_Lista[i]
                w.writerow(linha)


# Função para abrir a janela de seleção de arquivo e carregar o CSV
def load_csv():
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    file_path = filedialog.askopenfilename(defaultextension=".csv",
                                           filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])

    if file_path:  # Se o usuário não cancelar
        with open(file_path, 'r', newline='') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return data

# Chama a função para abrir a janela e carregar o arquivo


print(load_csv())