from gerenciamento_de_herois import Gerenciar_herois
import time

gerenciar = Gerenciar_herois()
valores_entreda = ['Nome', 'Classe', 'HP', 'ATK', 'Nivel']

print("\033[1m-------------------------------------------------------------\033[0m")
print("\033[1m|--- Olá seres humanos, Bem vindo ao Reino de Salesiania 🏰 |\n|--- Vamos lá! O que desejas??                              |\033[0m")
print("\033[1m-------------------------------------------------------------\033[0m")
while True:
    print("\033[1m------------------------------------------------------\033[0m")
    print("\033[1m|### Menu:                                           |\033[0m")
    print("|-- Digite '1' para Listar nossos Heróis do Reino.   |\n|-- Digite '2' para Adicionar um novo Herói ao Reino.|\n|-- Digite '3' para Evoluir um Herói.                |\n|-- Digite '4' para Deletar um Herói.                |\n|-- Digite '5' para Batalha de Heróis.               |\n|-- Digite '6' para sair do sistema.                 |")
    print("\033[1m------------------------------------------------------\033[0m")
    info = input('- Sua escolha é? ')
    #Operações do sistema a seguir:
    # Opção de Lista os Heróis cadastrados no Sistema.
    if info == '1':
        gerenciar.listar_herois()
    # Opção de Inserir um novo Herói no Sistema.
    elif info == '2':
        print("\n- Para Adicionar um novo Herói, precisamos das informações a seguir:")
        novo_heroi = {}
        for variavel in valores_entreda: # Um For, Pegando todas as Informações necessarias para cadastrar um novo Herói.
            while True:
                info =  input(f"{variavel}: ")
                if variavel not in 'Nome, Classe':
                    try:
                        info = int(info)
                        break
                    except:
                        print(f"\n- O Valor inserido '{info}' precisa ser um valor inteiro. EX: 50.\n- Digite o valor correto novamente...")
                        time.sleep(2)
                else:
                    break
            novo_heroi[variavel] = info
        gerenciar.adicionar_heroi(novo_heroi) # Metodo onde chamo a função que ira inserir um novo herói, passando as informações necessarias.
    #Opção de Evoluir um Herói do Sistema.
    elif info == '3':
        nome = input("\n- Qual o nome do Herói que deseja evoluir o nivel? ")
        gerenciar.evoluir_heroi(nome) # Chamando o Metodo para Evoluir um Herói, onde eu Passo o 'Nome' do herói como chave para achá-lo no Sistema.
    #Opção para Deletar um Herói do Sistema.
    elif info == '4':
        nome = input("Qual o nome do Herói que deseja deletar do sistema? ")
        gerenciar.remover_heroi(nome)# Chamando o Metodo para Remover um Herói do sistema, onde eu Passo o 'Nome' do herói como chave para achá-lo no Sistema.
    # Opção para Batalha de Heróis.
    elif info == '5':
        info = gerenciar.listar_herois() # Lista os Heróis.
        if info == 1:
            print("- Cadastre mais Heróis para batalhar.")
        else:
            print("\n- Vamos de Batalha de Heróis??\n")
            while True: # Selecionar os Heróis.
                nome = input("- Qual o nome do primeiro Herói? ")
                heroi_1 = gerenciar.buscar_herois(nome)
                if heroi_1 == None:
                    print(f"Herói '{nome}' não Localizado.\n- Escolha um Herói existente.")
                else:
                    break
            while True:
                nome = input("\n- Qual o nome do segundo Herói? ")
                heroi_2 = gerenciar.buscar_herois(nome)
                if heroi_2 == None:
                    print(f"- Herói '{nome}' não Localizado. Escolha um Herói existente.")
                    continue
                elif heroi_1["Nome"] == heroi_2["Nome"]:
                    print("\n- Os mesmos Heróis não pode ser enfrentarem...\n Escolha outro Herói para batalha.\n Portanto foi um Empate.")
                    time.sleep(2)
                    continue
                gerenciar.batalha_de_herois(heroi_1, heroi_2)# Metodo onde acontece a batalha, passando os dois herois para batalha.
                break
    # Opção para sair do Sistema.
    elif info == '6':
        print("\n-- Obrigado por conhecer e colaborar com o Reino de Salesiania 🏰.\n-- Espero que tenha gostado!!!\n-- Até a Proxima...😁")
        break
    # Caso a opção não for correspondente as anteriores, ele volta ao 'Menu.'
    else:
        print(f"-- Ops.\n-- Não encontrei a sua escolha '{info}' no meu sistema...\n-- Olhe novamente o nosso menu e escolha sua opção desejada.😉")
        time.sleep(8.5)
    print("- Retornado ao Menu.")
    time.sleep(1.5)