from functions import descrever_gramado, assalto_de_estrada, descrever_vila
from Mapa import Mapa
from Jogador import Jogador
from Vila import Vila
from classes import Produto, Penias


arroz_vila1 = Produto("arroz", 0.5, 100, 0.1)
peixe_vila2 = Produto("peixe", 2.2, 18, 5)
V = Vila("Vila1", 30, arroz_vila1)
v = Vila("Vila2", 45, peixe_vila2)
mapa = Mapa(V,v)
arroz_jogador = Produto("arroz", 0.5, 50, 0.1)
peixe_jogador = Produto("peixe", 1, 20, 5)
moedas_jogador = Penias(15.50)

jogador1 = Jogador(0 ,0 ,mapa ,moedas = moedas_jogador ,arroz=arroz_jogador, peixe=peixe_jogador)

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
    'exit': exit,
    'mapa': jogador1.ver_mapa,
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

