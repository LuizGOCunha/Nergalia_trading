from classes import Gramado, Estrada

class Mapa:
    def __init__(self, *villages):
        """A fim de fazer uma lista tridimensional, coloquei uma lista dentro de outra"""
        self.villages = villages
        X = Gramado()
        #X = lambda: copy.deepcopy(x)        
        E = Estrada()
        #E = lambda: copy.deepcopy(e)
        V = self.villages[0]
        v = self.villages[1]
        y9 = [X, X, X, X, X, X, X, X, X, X,]
        y8 = [X, X, V, E, E, X, X, X, X, X,]
        y7 = [X, X, X, X, E, X, X, X, X, X,]
        y6 = [X, X, X, X, E, X, X, X, X, X,]
        y5 = [X, V, E, E, E, E, E, E, v, X,]
        y4 = [X, X, E, X, X, X, X, X, X, X,]
        y3 = [X, X, E, X, X, X, X, X, X, X,]
        y2 = [X, X, E, E, E, E, E, E, X, X,]
        y1 = [X, X, X, X, X, X, X, E, X, X,]
        y0 = [X, X, X, X, X, X, X, E, X, X,]
        self.grid = [y9,y8,y7,y6,y5,y4,y3,y2,y1,y0]
                    
        # listamos e guardamos as vilas presentes no mapa
        

    def passar_do_tempo(self):
        """Uma função para puxar todos os métodos do que deve acontecer quando passar o tempo"""
        for village in self.villages:
            village.produzir()
            village.atualizar_precos()
            
    def coordenada_valida(self, x, y):
        # Checamos se o nosso Y está fora do range da grid (Maior que o maximo ou menor que o minimo)
        try:
            if self.grid[y][x]:
                pass
        except IndexError:
            return False
        # se não for o caso, retornamos true  
        return True

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

