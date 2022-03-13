from functions import descrever_gramado, descrever_estrada, descrever_vila

class Mapa:
    def __init__(self, *villages):
        """A fim de fazer uma lista tridimensional, coloquei uma lista dentro de outra"""
        X = descrever_gramado
        E = descrever_estrada
        V = descrever_vila
        y9 = [X, X, X, X, X, X, X, X, X, X,]
        y8 = [X, X, X, X, X, X, X, X, X, X,]
        y7 = [X, X, X, X, X, X, X, X, X, X,]
        y6 = [X, X, X, X, X, X, X, X, X, X,]
        y5 = [X, V, E, E, E, E, E, E, V, X,]
        y4 = [X, X, X, X, X, X, X, X, X, X,]
        y3 = [X, X, X, X, X, X, X, X, X, X,]
        y2 = [X, X, X, X, X, X, X, X, X, X,]
        y1 = [X, X, X, X, X, X, X, X, X, X,]
        y0 = [X, X, X, X, X, X, X, X, X, X,]
        self.grid = [y0,y1,y2,y3,y4,y5,y6,y7,y8,y9]
        """listamos e guardamos as vilas presentes no mapa"""
        self.villages = []
        for village in villages:
            self.villages.append(village)

    def passar_do_tempo(self):
        """Uma função para puxar todos os métodos do que deve acontecer quando passar o tempo"""
        for village in self.villages:
            village.produzir()
            village.atualizar_precos()
        
    def executar_coordenada(self,x,y):
        """Função a ser chamada quando o jogador entra na devida coordenada"""
        y_grid = self.grid[y]
        coord_completa = y_grid[x]
        if type(coord_completa) == tuple:
            for funcoes in coord_completa:
                funcoes()
        else:
            coord_completa()


class Vila:
    def __init__(self, nome_da_vila, produto_produzido, inventario):
        self.nome = nome_da_vila
        self.produto = produto_produzido
        self.inventario = inventario
        self.preco_produto_relativo = self.produto.preco_base/(self.inventario/100)
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
    

class Produto:
    def __init__(self, nome_do_produto, preco_base):
        self.nome = nome_do_produto
        self.preco_base = preco_base
        self.preco_relativo = preco_base


class Jogador:
    def __init__(self, coordenada_x, coordenada_y, mapa):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.mapa_atual = mapa
        self.mapa_atual.executar_coordenada(coordenada_x, coordenada_y)

    def mover_norte(self):
        self.coordenada_y += 1
        try:
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
        except IndexError:
            print("Nenhum lugar ao norte")
            self.coordenada_y -= 1
            self.mapa_atual.passar_do_tempo

    def mover_sul(self):
        self.coordenada_y -= 1
        try:
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
        except IndexError:
            print("Nenhum lugar ao sul")
            self.coordenada_y += 1
            self.mapa_atual.passar_do_tempo

    def mover_leste(self):
        self.coordenada_x +=1
        try:
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
        except IndexError:
            print("Nenhum lugar ao leste")
            self.coordenada_x -= 1
            self.mapa_atual.passar_do_tempo

    def mover_oeste(self):
        self.coordenada_x -= 1
        try:
            self.mapa_atual.executar_coordenada(self.coordenada_x, self.coordenada_y)
        except IndexError:
            print("Nenhum lugar ao oeste")
            self.coordenada_x += 1
            self.mapa_atual.passar_do_tempo

   # def atualizar_mapa(self, mapa):
   #     self.mapa_atual = mapa



    