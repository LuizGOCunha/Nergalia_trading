from functions import descrever_gramado, assalto_de_estrada, descrever_vila
from classes import Mapa, Penias, Vila, Jogador, Produto

mapa = Mapa()
arroz_jogador = Produto("arroz", 0.5, 50)
peixe_jogador = Produto("peixe", 1, 20)
moedas_jogador = Penias(15.50)

jogador1 = Jogador(0 ,0 ,mapa ,moedas_jogador ,arroz_jogador, peixe_jogador)

print("""
W = norte
S = Sul
D = Leste
A = Oeste""")

key_bindings = {
    'w': jogador1.mover_norte,
    's': jogador1.mover_sul,
    'd': jogador1.mover_leste,
    'a': jogador1.mover_oeste,
    'inv': jogador1.mostrar_inventario,
    'exit': exit
}

while True:
    prompt = input('>')
    try:
        key_bindings[prompt]()
    except KeyError:
        print("Comando inexistente")













    #if prompt == 'w':
    #    jogador1.mover_norte()
    #elif prompt == 's':
    #    jogador1.mover_sul()
    #elif prompt == 'd':
    #    jogador1.mover_leste()
    #elif prompt == 'a':
    #    jogador1.mover_oeste()
    #elif prompt == 'exit':
    #    exit()
    #elif prompt == 'inv':
    #    jogador1.mostrar_inventario()
    #else:
    #    print("comando invalido")

