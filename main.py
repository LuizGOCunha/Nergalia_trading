from functions import descrever_gramado, assalto_de_estrada, descrever_vila
from classes import Mapa, Vila, Jogador, Produto

mapa = Mapa()


jogador1 = Jogador(1,1,mapa)
print("""
W = norte
S = Sul
D = Leste
A = Oeste""")

while True:
    prompt = input('>')
    if prompt == 'w':
        jogador1.mover_norte()
    elif prompt == 's':
        jogador1.mover_sul()
    elif prompt == 'd':
        jogador1.mover_leste()
    elif prompt == 'a':
        jogador1.mover_oeste()
    elif prompt == 'exit':
        exit()
    else:
        print("comando invalido")