#importando o json
import json

# Carregando os Exercícios
exerciciosJson = open("exercicios.json", "r")
exerciciosDisponiveis = json.load(exerciciosJson)

#Carregando a Quantidade de Exercícios iniciais
qtdJson = open("test.json", "r")
qtdExercicios = json.load(qtdJson)