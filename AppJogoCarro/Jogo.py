from Carro import Carros as car
import os

while True:
    print('Bem vindo ao jogo do Alan')
    print('---Escolha os seu carro---')
    choice_car = input('1 - Volkswagen\n2 - Ferrari\n3 - Chevrolet\n4 - Fiat\n>>> ')
    size_string_choice_car = len(choice_car)

    if size_string_choice_car > 1:
        print(f'\033[0;31mVocê digitou mais de um caracter.\033[m Você digitou: "{choice_car}"')
        for tempo in range(1,20000000): # Tempo de mensagem de erro
                tempo = tempo
        os.system('cls') or None # Limpar terminal
        continue
    elif size_string_choice_car < 1:
        print(f'\033[0;31mVocê digitou menos ou nada caracter.\033[m Você digitou: "{choice_car}"')
        for tempo in range(1,20000000): # Tempo de mensagem de erro
                tempo = tempo
        os.system('cls') or None # Limpar terminal
        continue


    try:
        choice_car = int(choice_car)
    except:
        print(f'\033[0;31mVocê não digitou um número!\033m Você digitou {choice_car}')
        for tempo in range(1,20000000): # Tempo de mensagem de erro
                tempo = tempo
        os.system('cls') or None # Limpar terminal
        continue
    
    if choice_car != 1 and choice_car != 2 and choice_car != 3 and choice_car != 4:
        print('\033[0;31mDigite o número correspondente ao carro!\033[m')
        for tempo in range(1,20000000): # Tempo de mensagem de erro
                tempo = tempo
        os.system('cls') or None # Limpar terminal
        continue

    break



def chosen_car(choice_car):
    if choice_car == 1:
        return 'Volkswagen'
    elif choice_car == 2:
        return 'Ferrari'
    elif choice_car == 3:
        return 'Chevrolet'
    elif choice_car == 4:
        return 'Fiat'
    
    

carro_1 = car(chosen_car(choice_car),'genérico','genérico','Gasolina') # Carro criado
print('\n\033[1mCOMANDOS\033[m')
print('Ligar o carro: digite "ligar"')
print('Desligar o carro: digite "desligar"')
print('Acelerar: "Enter"')
print('Frear o carro: Digite "f" e pressione enter. Quantos "f" você colocar, sera o resultado do freio mais eficiente')
print('Exibir informações do carro: digite "exibir"\n')
while True:
    eventos = input()

    if eventos == 'ligar':
        car.ligar(carro_1)
    
    if eventos == 'desligar':
        car.desligar(carro_1)

    if len(eventos) == 0:
        car.acelerar(carro_1)

    if 'f' in eventos:
        values_break = eventos.count('f')
        car.frear(carro_1, values_break)

    if eventos == 'exibir':
        car.exibirInformacoes(carro_1)