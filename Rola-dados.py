from random import randint
from time import sleep

ranking = list()
resultado = {"Jogador1": 0, "Jogador2": 0, "Jogador3": 0, "Jogador4": 0}

for key in resultado.keys():
    resultado[key] = randint(1, 6)

for i, key in enumerate(resultado.keys()):
    print(f'O dado que o {i+1}° Jogador tirou foi: {resultado[key]}')
    ranking.append(resultado[key])
    sleep(0.5)

print('=+'*30)

ranking.sort(reverse=True)

for c in range(0, len(ranking)):

    for key in resultado.keys():

        if ranking.count(ranking[c]) == 1 and ranking[c] == resultado[key]:
            print(f'O {c + 1}° colocado é {key} com {resultado[key]}')
            sleep(0.5)

        if ranking.count(ranking[c]) > 1 and ranking[c] == resultado[key]:
            print(f'O {c + 1}° colocado é {key} com {resultado[key]}')
            sleep(0.5)
            del resultado[key]
            break
