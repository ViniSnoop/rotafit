#importando o json
import json

exerciciosJson = open("exercicios.json", "r")
exerciciosDisponiveis = json.load(exerciciosJson)