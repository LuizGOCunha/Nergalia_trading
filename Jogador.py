from classes import Estrada

class Jogador:
    def __init__(self, coord_x, coord_y, mapa, **produtos):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.mapa_atual = mapa
        self.executar_coordenada(coord_x, coord_y)
        self.inventario = produtos

    def mostrar_inventario(self):
        for produtos in self.inventario:
            print(produtos)

    def modificar_inventario(self, item, quantidade):
        pass

    def coord_valida(self):
        return 10 > self.coord_y >= 0 and 10 > self.coord_x >= 0

    def retornar_coordenada(self, x, y):
        # if self.mapa_atual.coordenada_valida(x,y):
        y_grid = self.mapa_atual.grid[y]
        coord_completa = y_grid[x]
        return coord_completa

    def executar_coordenada(self, x, y):
        """Função a ser chamada quando o jogador entra na devida coordenada"""
        y_grid = self.mapa_atual.grid[y]
        coord_completa = y_grid[x]
        coord_completa()
        if type(coord_completa) == Estrada:
            self.verificar_caminho()

    def verificar_caminho(self):
        caminho = "Essa estrada tem caminhos para "
        # Tenho noção do problema que pode dar um 'except: pass', mas aqui é só uma verificação, deve ficar ok
        try:
            if type(self.retornar_coordenada(self.coord_x, self.coord_y+1)) == Estrada:
                caminho += "Norte, "
        except IndexError:
            pass
        try:
            if type(self.retornar_coordenada(self.coord_x, self.coord_y-1)) == Estrada:
                caminho += "Sul, "
        except IndexError:
            pass
        try:
            if type(self.retornar_coordenada(self.coord_x+1, self.coord_y)) == Estrada:
                caminho += "Leste, "
        except IndexError:
            pass
        try:
            if type(self.retornar_coordenada(self.coord_x-1, self.coord_y)) == Estrada:
                caminho += "Oeste, "
        except IndexError:
            pass
        caminho = caminho[:-2]
        print(caminho)

    def arredores(self):
        """A intenção aqui é criar um dicionario dos arredores atuais"""
        arredores = {
        "norte":self.mapa_atual(self.coord_x,self.coord_y+1),
        "sul":self.mapa_atual(self.coord_x,self.coord_y-1),
        "leste":self.mapa_atual(self.coord_x+1,self.coord_y),
        "oeste":self.mapa_atual(self.coord_x-1,self.coord_y),
        }
        return arredores

    def mover_norte(self):
        self.coord_y -= 1
        if self.coord_valida():
            self.executar_coordenada(self.coord_x, self.coord_y)
            print("whut")
            self.mapa_atual.passar_do_tempo()
            
        else:
            print("Nenhum lugar ao Norte")
            self.coord_y += 1

    def __str__(self):
        return "JJ"    

    def mover_sul(self):
        self.coord_y += 1
        if self.coord_valida():
            self.executar_coordenada(self.coord_x, self.coord_y)
            self.mapa_atual.passar_do_tempo()
        else:
            print("Nenhum lugar ao Sul")
            self.coord_y -= 1

    def mover_leste(self):
        self.coord_x +=1
        if self.coord_valida():
            self.executar_coordenada(self.coord_x, self.coord_y)
            self.mapa_atual.passar_do_tempo()
        else:
            print("Nenhum lugar ao Leste")
            self.coord_x -= 1

    def mover_oeste(self):
        self.coord_x -= 1
        if self.coord_valida():
            self.executar_coordenada(self.coord_x, self.coord_y)
            self.mapa_atual.passar_do_tempo()
        else:
            print("Nenhum lugar ao Oeste")
            self.coord_x += 1

    def vender(self,vila, quantidade, produto):
        # É necessario padronizar os inventarios para que isso funcione. Talvez transformá-los em dict seja o ideal
        if vila.financas - vila.preco_produto_relativo*quantidade < 0:
            print("Não há moeda suficiente")
        else: 
            vila.financas -= vila.preco_produto_relativo*quantidade
            self.inventario["moedas"] += vila.preco_produto_relativo*quantidade
            vila.produto.quantidade += quantidade
            self.inventario[f"{produto.nome}"].quantidade -= quantidade

    def ver_mapa(self):
        """Aqui é onde printamos na tela a representação do mapa, utilizando o dunder __str__ de nossos objetos"""
        # Aqui quero printar o mapa, mas printar a localização do jogador junto
        # Não sei pq ainda não funciona
        print("**********************")
        for y, y_axis in enumerate(self.mapa_atual.grid):
            string = "*"
            for x, x_axis in enumerate(y_axis):
                # aaaaah, é pq x_axis é um objeto, não uma posição. Depois ajeita isso.
                if self.coord_x == x and self.coord_y == y:
                    string += self.__str__()
                else:
                    string += x_axis[-1].__str__()
            string += "*"
            print(string)
        print("**********************")

    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]
