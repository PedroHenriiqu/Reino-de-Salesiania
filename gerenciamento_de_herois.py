from no import No
import time

class Gerenciar_herois:
    def __init__(self):
        self.inicio = None

    # Função onde adiciona um novo Herói.
    def adicionar_heroi(self, novo_heroi):
        novo_no = No(novo_heroi) # Chama a classo 'No', passando o novo Herói, retornando um 'No' com aquele herói.
        if self.inicio is None: # Caso self.inicio for 'None', ele atribui o 'novo_no' a ele.
            self.inicio = novo_no
        else:
            atual = self.inicio
            while atual.proximo: # Caso self.inicio não for 'None', ele atribui o Herói 'novo_no', ao proximo No. 
                atual = atual.proximo
            atual.proximo = novo_no
        print(f"- Herói '{novo_heroi['Nome']}' cadastrado.")
        time.sleep(2)

    # Função onde Lista os Heróis do sistema.
    def listar_herois(self):
        atual = self.inicio
        if not atual: # Caso o self.inicio, for 'None'/ vazio ele retoena a informação a seguir.
            print("- Lamento, mas não encontrei nenhum herói cadastrado.")
            time.sleep(2)
            return 1
        herois_por_nivel = []
        while atual:
            herois_por_nivel.append(atual.heroi) # Coloca todos os Heróis na nova lista.
            atual = atual.proximo
        # Organiza os Heróis da lista por 'Nivel', onde o Herói com maior nivel fica em primeiro.
        herois_por_nivel.sort(key=lambda h: h['Nivel'], reverse=True)
        print("-- Nossos Heróis (Ordenados por Nível):")
        # Um 'For' printando cada Herói da lista, onde foi organizada por Nivel. 
        for heroi in herois_por_nivel:
            print(f"Nome: {heroi['Nome']}, Classe: {heroi['Classe']}, HP: {heroi['HP']}, ATK: {heroi['ATK']}, Nível: {heroi['Nivel']}.")
        time.sleep(2)

    # Função onde Evolui um Herói especifico.
    def evoluir_heroi(self, nome):
        atual = self.inicio
        while atual: # Procura o Herói pelo 'Nome'
            if atual.heroi['Nome'] == nome:
                heroi = atual.heroi
                heroi['Nivel'] += 1 # Almentando o Nivel do Herói.
                # OBS: os Casos 'HP' ou 'ATK' do Herói for muito baixo, quando for fazer a operação a seguir ele retorna um
                # numero quebrado(float), porém na documentação está pedindo um numero inteiro, estão acaba ficando o mesmo valor anterior.
                heroi['HP'] = int(heroi['HP'] * 1.10)# Almentando o HP do Herói.
                heroi['ATK'] = int(heroi['ATK'] * 1.05)# Almentando o ATK do Herói.
                print(f"Herói '{heroi['Nome']}' subiu de nível! Agora ele está no nível {heroi['Nivel']}.\n Novo HP: {heroi['HP']} | Novo ATK: {heroi['ATK']}")
                time.sleep(2)
                return
            atual = atual.proximo
        # Caso não encontre o Herói retorna a informação a seguir.
        print("Herói não encontrado!")
        time.sleep(2)

    # Função onde remove o Herói do sistema.
    def remover_heroi(self, nome):
        atual = self.inicio
        anterior = None
        while atual: # Busca Pelo Herói.
            if atual.heroi['Nome'] == nome:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                print(f"Herói '{nome}' foi removido dos registros.")
                time.sleep(2)
                return
            anterior = atual
            atual = atual.proximo
        # Caso não encontre o Herói retorna a informação a seguir.
        print("Este herói não está nos registros!")
        time.sleep(2)
    
    # Função de Batalhas hahaha
    # Dois Heróis batalham um contra o outro, quem tiver mais ATK vence.
    def batalha_de_herois(self, heroi_1, heroi_2):
        print(f"\n-- A batalha vai começar....\n\033[1m-- O Duelo entre {heroi_1["Nome"]} x {heroi_2["Nome"]}.\033[0m\n-- Vocês estão pretarados para esse Duelo? 😶‍🌫️\n")
        time.sleep(2)
        if heroi_1["ATK"] > heroi_2["ATK"]:
            print(f"---------- Vitória ----------")
            print(f"- O Herói é..... {heroi_1["Nome"]}, com um ataque 'ATK' de {heroi_1["ATK"]}.")
        elif heroi_1["ATK"] < heroi_2["ATK"]:
            print(f"---------- Vitória ----------")
            print(f"- O Herói é..... {heroi_2["Nome"]}, com um ataque 'ATK' de {heroi_2["ATK"]}.")
        else:
            print(f"---------- Empate ----------")
            print(f"- Os Heróis {heroi_1["Nome"]} e {heroi_2["Nome"]}, tem o mesmo ATK {heroi_1["ATK"]}/{heroi_2["ATK"]}.")
        time.sleep(7)

    # Função que Busca o Herói antes da Batalha, assim tem a certeza que o Herói existe.
    def buscar_herois(self, nome):
        atual = self.inicio
        while atual:
            if atual.heroi["Nome"] == nome:# Se o Herói existi ele retorna as informações dele para a batalha.
                print(f"O Primeiro Herói '{nome}' foi selecionado.")
                return atual.heroi
            atual = atual.proximo
        # Caso não encontre o Herói retorna a informação a seguir.
        print("Este herói não está nos registros!")