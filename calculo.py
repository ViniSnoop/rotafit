import json
from dicionario import exerciciosDisponiveis

def calculoDeTempo():
    arquivo = open("test.json", "r")
    quantidadeDeExercicios = json.load(arquivo)
    arquivo.close()
    tempo = 0.0
    c = 0
    try:
        for i in exerciciosDisponiveis.values():
            tempo += i["tempo"] * quantidadeDeExercicios[c]
            c +=1

        def converter_segundos(segundos):
            horas = segundos // 3600  # 1 hora = 3600 segundos
            minutos = (segundos % 3600) // 60  # 1 minuto = 60 segundos
            segundos_restantes = segundos % 60  # Resto dos segundos

            return f"{horas}h {minutos}min {segundos_restantes}seg"

        tempoTotal= converter_segundos(tempo)
    except:
        for i in exerciciosDisponiveis.values():
            tempo += i["tempo"] * 0
            c +=1

        def converter_segundos(segundos):
            horas = segundos // 3600  # 1 hora = 3600 segundos
            minutos = (segundos % 3600) // 60  # 1 minuto = 60 segundos
            segundos_restantes = segundos % 60  # Resto dos segundos

            return f"{horas}h {minutos}min {segundos_restantes}seg"

        tempoTotal=converter_segundos(tempo)
    return tempoTotal