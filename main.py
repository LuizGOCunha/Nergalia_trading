class jogador:
    def __init__(self, coordenada_x, coordenada_y, mapa):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        self.mapa_atual = mapa
        self.mapa_atual[f'{self.coordenada_x},{self.coordenada_y}']()

    def mover_norte(self):
        self.coordenada_y += 1
        try:
            self.mapa_atual[f'{self.coordenada_x},{self.coordenada_y}']()
        except KeyError:
            print("Nenhum lugar ao norte")
            self.coordenada_y -= 1

    def mover_sul(self):
        self.coordenada_y -= 1
        try:
            self.mapa_atual[f'{self.coordenada_x},{self.coordenada_y}']()
        except KeyError:
            print("Nenhum lugar ao sul")
            self.coordenada_y += 1

    def mover_leste(self):
        self.coordenada_x +=1
        try:
            self.mapa_atual[f'{self.coordenada_x},{self.coordenada_y}']()
        except KeyError:
            print("Nenhum lugar ao leste")
            self.coordenada_x -= 1

    def mover_oeste(self):
        self.coordenada_x -= 1
        try:
            self.mapa_atual[f'{self.coordenada_x},{self.coordenada_y}']()
        except KeyError:
            print("Nenhum lugar ao oeste")
            self.coordenada_x += 1

    def atualizar_mapa(self, mapa):
        self.mapa_atual = mapa


def descrever_gramado():
    print("Está em um plano de grama verde. A humidade reflete das laminas verdejantes.")

def descrever_vila():
    print("você enxerga uma vila tranquila. Um velho veterano acena com a cabeça.")
    print("Você responde? (sim/nao)")
    acao = input('>')
    if acao == 'sim':
        print("O velho sorri")
    elif acao == 'nao':
        print('O velho se vira ao seu café')
    else: 
        print('O velho franze o cenho, e lhe ignora')

def assalto_de_estrada():
    print('Dois homens de face coberta puxam uma navalha e exigem seu dinheiro')
    print('Você obedece? (sim/nao)')
    acao = input('>')
    if acao == 'sim':
        print('Você cede às exigências e entrega seu pouco dinheiro')
    elif acao == 'nao':
        print('Você tenta resistir, mas não é tão durão quanto pensava. Você tem suas entranhas perfuradas.')
        print("Você morreu.")
        exit()
    else: 
        print("Os dois se entreolham, logo percebendo que você não é tão são como parece.")
        print("Eles guardam a navalha e lhe permitem passar.")


mapa = {
    "1,1": descrever_gramado,
    "1,2": descrever_gramado,
    "1,3": descrever_gramado,
    "2,1": descrever_vila,
    "2,2": descrever_gramado,
    "2,3": descrever_gramado,
    "3,1": descrever_gramado,
    "3,2": assalto_de_estrada,
    "3,3": descrever_gramado,
}

jogador1 = jogador(1,1,mapa)
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