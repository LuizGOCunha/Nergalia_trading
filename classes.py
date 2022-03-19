from functools import total_ordering
import math
from colorama import Fore, Style


class Produto:
    def __init__(self, nome_do_produto, preco_base, quantidade, quilos_perdidos_por_apodrecimento):
        self.nome = nome_do_produto
        self.preco_base = preco_base
        self.preco_relativo = preco_base
        self.quantidade = quantidade
        # Isso é a porcentagem (0-100) de quilos perdidos por invalidade a cada dia
        self.invalidade_rate = quilos_perdidos_por_apodrecimento

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
        string = f"Em sua bolsa de moedas você tem {penias} penias"
        if copones:
            string += f"e {copones} copones"
        return string
    
    def __eq__(self, outro):
        return self.valor == outro.valor

    def __lt__ (self, outro):
        return self.valor < outro.valor

    def __add__(self, outro):
        return Penias(self.valor + outro.valor)


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
        self.primeira_vias_call_flag = False      

    def __call__(self):
        print('Seus pés caminham em uma estrada segura')

    def __str__(self):
        return Fore.WHITE + Style.BRIGHT + "EE" + Style.RESET_ALL
    
    def __getitem__(self,index):
        lista_gambiarra = [self]
        return lista_gambiarra[index]



   # def atualizar_mapa(self, mapa):
   #     self.mapa_atual = mapa



    