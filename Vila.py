from colorama import Fore, Style

class Vila:
    def __init__(self, nome_da_vila, penias, produto_produzido):
        self.nome = nome_da_vila
        self.produto = produto_produzido
        self.preco_produto_relativo = self.produto.preco_base/(self.produto.quantidade/100)
        self.financas = penias

    # Esse método provavelmente deveria pertencer ao produto, lembrar de modificar apropriadamente
    def produzir(self, praga=False, enchente=False):
        """metodo a ser chamado para aumentar o inventario da vila com o tempo (ou não)"""
        if praga:
            self.produto.quantidade -= 1
        elif enchente: 
            pass
        else: 
            self.produto.quantidade += 3
        # Aqui calculamos a porcentagem perdida por invalidade (apodrecimento)
        self.produto.quantidade -= self.produto.quantidade*(self.produto.invalidade_rate/100)
        print(self.nome, self.financas, self.preco_produto_relativo, self.produto)

    def atualizar_precos(self):
        """Aqui atualizamos o preço do produto da vila com base em oferta e demanda
            Futuramente também deve se atualizar o preço dos produtos que a vila pede"""
        self.preco_produto_relativo = self.produto.preco_base/(self.produto.quantidade/100)
        print(self.nome, self.financas, self.preco_produto_relativo, self.produto)
        
    def interagir_com_a_vila(self):
        """Aqui será o prompt de interação com a vila (comprar, vender, etc)"""
        print(f"Você passa por uma vila amigável de nome {self.nome}")
        print(self.produto, self.financas, self.preco_produto_relativo)

    def __call__(self):
        """dunder utilizado para que o objeto vila possa ser chamado pelo executar_coordenada"""
        self.interagir_com_a_vila()

    def __str__(self):
        return Fore.YELLOW + Style.BRIGHT + "VV" + Style.RESET_ALL

    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]
    
