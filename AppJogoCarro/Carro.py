class Carros: # Classe Carros

    # Atributos, caracteristas de um carro
    def __init__(self, marca, modelo, cor, combustivel,ligado=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ligado = ligado
        self.velocidade = 0

        # Velocidade dos carros escolhidos
        def velocidade_das_marcas(marca):
            if marca == 'Volkswagen':
                velocidadeMaxima = 180
                return velocidadeMaxima

            elif marca == 'Ferrari':
                velocidadeMaxima = 299
                return velocidadeMaxima

            elif marca == 'Chevrolet':
                velocidadeMaxima = 167
                return velocidadeMaxima

            elif marca == 'Fiat':
                velocidadeMaxima = 160
                return velocidadeMaxima

            elif marca == 'Lamborghini':
                velocidadeMaxima = 279
                return velocidadeMaxima

            elif marca == 'Mercedes':
                velocidadeMaxima = 275
                return velocidadeMaxima

            elif marca == 'Hyudai':
                velocidadeMaxima = 200
                return velocidadeMaxima

            elif marca == 'Toyota':
                velocidadeMaxima = 200
                return velocidadeMaxima

            elif marca == 'Honda':
                velocidadeMaxima = 197
                return velocidadeMaxima

            elif marca == 'Ford':
                velocidadeMaxima = 176
                return velocidadeMaxima

            elif marca == 'Citroen':
                velocidadeMaxima = 177
                return velocidadeMaxima

            elif marca == 'Renault':
                velocidadeMaxima = 176
                return velocidadeMaxima

            elif marca == 'Peojeut':
                velocidadeMaxima = 177
                return velocidadeMaxima

            elif marca == 'Volvo':
                velocidadeMaxima = 250
                return velocidadeMaxima


        self.velocidadeMaxima = velocidade_das_marcas(marca)


    def ligar(self):
        if self.ligado:
            print('O carro já está ligado.')
        else:
            print('Dando Partida...')
            for tempo in range(1,100000000):
                tempo = tempo
            print('Carro ligado')
            self.ligado = True   


    def desligar(self):
        if self.ligado:
            if self.velocidade == 0:
                print('Carro desligado')
                self.ligado = False
            else:
                print('Por motivos de segurança, só é possivel desligar o carro com ele parado!')
        else:
            print('Carro já está desligado')


    def acelerar(self):
        if self.ligado == True:
            if self.velocidade < self.velocidadeMaxima -1:
                self.velocidade += 0.25
                print(f'{self.velocidade} km/h')
            else:
                print(f'{self.velocidade} km/h')
        else:
            print('Ligue o carro para poder acelerar')
    

    def frear(self, values_break=False):
        if self.velocidade > 0:
            if values_break:
                self.velocidade -= values_break
            else:
                self.velocidade -= 1
            print(f'{self.velocidade} km/h')
        else:
            print('Carro está parado')


    def exibirInformacoes(self):
        print(f'Marca -> {self.marca}')
        print(f'Modelo -> {self.modelo}')
        print(f'Cor -> {self.cor}')
        print(f'Combústivel -> {self.combustivel}')
        print(f'Velocidade Máxima -> {self.velocidadeMaxima}')