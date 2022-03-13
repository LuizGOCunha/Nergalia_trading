
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

def descrever_estrada():
    print('Seus pés caminham em uma estrada segura')

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
