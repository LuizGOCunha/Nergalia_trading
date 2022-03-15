from functools import total_ordering
import math
from operator import index
from functions import descrever_gramado, descrever_estrada, descrever_vila
from colorama import Fore, Style

class Mapa:
    def __init__(self, *villages):
        """A fim de fazer uma lista tridimensional, coloquei uma lista dentro de outra"""
        X = Gramado()
        E = Estrada()
        arroz_vila1 = Produto("arroz", 0.5, 100)
        V = Vila("Vila1", arroz_vila1)
        y9 = [X, X, X, X, X, X, X, X, X, X,]
        y8 = [X, X, V, E, E, X, X, X, X, X,]
        y7 = [X, X, X, X, E, X, X, X, X, X,]
        y6 = [X, X, X, X, E, X, X, X, X, X,]
        y5 = [X, V, E, E, E, E, E, E, V, X,]
        y4 = [X, X, E, X, X, X, X, X, X, X,]
        y3 = [X, X, E, X, X, X, X, X, X, X,]
        y2 = [X, X, E, E, E, E, E, E, X, X,]
        y1 = [X, X, X, X, X, X, X, E, X, X,]
        y0 = [X, X, X, X, X, X, X, E, X, X,]
        self.grid = [y9,y8,y7,y6,y5,y4,y3,y2,y1,y0]
        """listamos e guardamos as vilas presentes no mapa"""
        self.villages = []
        for village in villages:
            self.villages.append(village)

    def passar_do_tempo(self):
        """Uma função para puxar todos os métodos do que deve acontecer quando passar o tempo"""
        for village in self.villages:
            village.produzir()
            village.atualizar_precos()
        
    def executar_coordenada(self, x, y):
        """Função a ser chamada quando o jogador entra na devida coordenada"""
        y_grid = self.grid[y]
        coord_completa = y_grid[x]
        if type(coord_completa) == tuple or type(coord_completa) == list:
            for funcoes in coord_completa:
                funcoes()
        else:
            coord_completa()

    def acrescentar_objeto(self, x, y, objeto):
        self.grid[y][x] = (self.grid[y][x], objeto)

    def resetar_terreno(self, x, y):
        self.grid[y][x] = self.grid[y][x][0]

    def remover_ultimo_objeto(self, x, y):
        self.grid[y][x] = self.grid[y][x][:-1]

    def __call__(self):
        """Aqui é onde printamos na tela a representação do mapa, utilizando o dunder __str__ de nossos objetos"""
        print("**********************")
        for y_axis in self.grid:
            string = "*"
            for coordenate in y_axis:
                string += coordenate[-1].__str__()
            string += "*"
            print(string)
        print("**********************")

        

class Vila:
    def __init__(self, nome_da_vila, produto_produzido):
        self.nome = nome_da_vila
        self.produto = produto_produzido
        self.preco_produto_relativo = self.produto.preco_base/(self.produto.quantidade/100)
        self.financas = 50

    def produzir(self, praga=False, enchente=False):
        """metodo a ser chamado para aumentar o inventario da vila com o tempo (ou não)"""
        if praga:
            self.inventario -= 1
        elif enchente: 
            pass
        else: 
            self.inventario += 1

    def atualizar_precos(self):
        """Aqui atualizamos o preço do produto da vila com base em oferta e demanda
            Futuramente também deve se atualizar o preço dos produtos que a vila pede"""
        self.preco_produto_relativo = self.produto.preco_base/(self.inventario/100)
        
    def interagir_com_a_vila(self):
        """Aqui será o prompt de interação com a vila (comprar, vender, etc)"""
        pass

    def __call__(self):
        """dunder utilizado para que o objeto vila possa ser chamado pelo executar_coordenada"""
        self.interagir_com_a_vila()

    def __str__(self):
        return Fore.YELLOW + Style.BRIGHT + "VV" + Style.RESET_ALL

    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]
    

class Produto:
    def __init__(self, nome_do_produto, preco_base, quantidade):
        self.nome = nome_do_produto
        self.preco_base = preco_base
        self.preco_relativo = preco_base
        self.quantidade = quantidade

    def modificar_quantidade(self, modificador):
        self.quantidade += modificador

    def __str__(self):
        return f"Um carregamento de {self.nome}. {self.quantidade} quilos."

    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]

@total_ordering
class Penias: 
    def __init__(self, valor):
        self.valor = round(valor, 2)

    def __str__(self):
        penias = math.floor(self.valor)
        copones = int((self.valor - penias)*10)
        return f"Em sua bolsa de moedas você tem {penias} penias e {copones} copones"
    
    def __eq__(self, outro):
        return self.valor == outro.valor

    def __lt__ (self, outro):
        return self.valor < outro.valor


class Gramado:
    def __init__(self):
        pass

    def __call__(self):
        print("Está em um plano de grama verde. A humidade reflete das laminas verdejantes.")

    def __str__(self):
        return Fore.GREEN + Style.BRIGHT + "gg" + Style.RESET_ALL

    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]


class Estrada:
    def __init__(self):
        pass

    def __call__(self):
        print('Seus pés caminham em uma estrada segura')

    def __str__(self):
        return Fore.WHITE + Style.BRIGHT + "EE" + Style.RESET_ALL
    
    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]


class Jogador:
    def __init__(self, coordenada_x, coordenada_y, mapa, *produtos):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.mapa_atual = mapa
        self.mapa_atual.executar_coordenada(coordenada_x, coordenada_y)
        self.inventario = produtos

    def mostrar_inventario(self):
        for produtos in self.inventario:
            print(produtos)

    def modificar_inventario(self, item, quantidade):
        pass

    def coord_valida(self):
        return 10 > self.coordenada_y >= 0 and 10 > self.coordenada_x >= 0

    def mover_norte(self):
        self.coordenada_y += 1
        if self.coord_valida():
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
            self.mapa_atual.passar_do_tempo
        else:
            print("Nenhum lugar ao Norte")
            self.coordenada_y -= 1

    def __str__(self):
        return "JJ"
            
        

    def mover_sul(self):
        self.coordenada_y -= 1
        if self.coord_valida():
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
            self.mapa_atual.passar_do_tempo
        else:
            print("Nenhum lugar ao Sul")
            self.coordenada_y += 1

    def mover_leste(self):
        self.coordenada_x +=1
        if self.coord_valida():
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
            self.mapa_atual.passar_do_tempo
        else:
            print("Nenhum lugar ao Leste")
            self.coordenada_x -= 1

    def mover_oeste(self):
        self.coordenada_x -= 1
        if self.coord_valida():
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
            self.mapa_atual.passar_do_tempo
        else:
            print("Nenhum lugar ao Oeste")
            self.coordenada_x += 1

    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]

   # def atualizar_mapa(self, mapa):
   #     self.mapa_atual = mapa



    