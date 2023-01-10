from random import randint
from time import sleep

ranking = list()
resultado = {"Jogador1": 0, "Jogador2": 0, "Jogador3": 0, "Jogador4": 0}

for key in resultado.keys():
    resultado[key] = randint(1, 6)
# Rola os dados / Gera um número aleatório de 1 a 6 e preenche nas posições do dicionário

for i, key in enumerate(resultado.keys()):
    print(f'O dado que o {i+1}° Jogador tirou foi: {resultado[key]}')
    ranking.append(resultado[key])
    sleep(0.5)
# Mostra os dados rolados na tela / Adicionado as rolagens na lista 'ranking'

print('=+'*30)

ranking.sort(reverse=True)

for c in range(0, len(ranking)):

    for key in resultado.keys():

        if ranking.count(ranking[c]) == 1 and ranking[c] == resultado[key]:
            print(f'O {c + 1}° colocado é {key} com {resultado[key]}')
            sleep(0.5)
            # Verifica se não houve dados repetidos e se o valor do dado na ordem de ranking é igual ao valor tirado pelo jogador 
            # Alinha o resultado do dado salvo em ranking com o jogador que tirou o dado

        if ranking.count(ranking[c]) > 1 and ranking[c] == resultado[key]:
            print(f'O {c + 1}° colocado é {key} com {resultado[key]}')
            sleep(0.5)
            del resultado[key]
            break
            # Verifica se houve dados repetidos e se o valor dado na ordem de ranking é igual ao valor tirado pelo jogador
            # Alinha o resultado do dado salvo em ranking com a primeira ocorrência do jogador que tirou o dado
