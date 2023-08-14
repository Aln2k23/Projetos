import random


# === <<< << << << Função Gerador de String >> >> >> >>> === >> >> >> >>>

def senha_automatica():

    """
    Está função serve para gerar caracteres automático, dentre eles: caracter especial, números
    inteiros, e letras maiúsculas e minúsculas.
    Retorna a string com valores obtidos do gerador de "string".
    """
    string = ''
    for x in range(10):
        gerador = random.choice("6A.-avnaa5@B$.aaAFfIOaapfwte#aVfAZFaftiApllApoSazawJtyuu/9*-C\
c9PIL1.D-0#$/Oçlajafaa1urd*+=+#=@@$aA8a#g[Ee-FAN/F.pHGfBF*NB#G71*gGAFAWAFAFa]f@afaH[X7]/@9\
$AD$9h$2$F-I/zazaffgxacaGSGa@ig$\Jx[jbAFÇh.Kk5-1$[p@/5L0r*-l3F*GLKÇruruF3-1M.$@#5m/n$O.gçl\
#agjapo9#/44o$\ArF[1/.a0XaZ4afapAgdhka$5j@!![PpQqR9!6!5r/S@-*!sT$@t*Uu%AAFA*@4[8-V%/A.v[W]\
#wWlafkBFDADFAA!!po!afjaGA[*K$ÇA-QFZ\A!FG!OxYy![-7-Zz.~çkjknvf!aZFBTRTtfl#h$ja1y1a!F!D!AAR.")
        string += gerador 
        continue
    return string

#                 <<< ----===<  Fim da Função  >===---- >>>


# === <<< << << << Verifica a String Digitada >> >> >> >>> === >> >> >> >>>

def verificacao_de_string(pergunta, primeira_cond, segundo_cond, mensagem_de_erro):
    """
    pergunta: Você digita o texto que deseja, para perguntar pro usuário.
    primeira_cond: Primeira condição do que você deseja.
    segunda_cond: Segunda condição do que você deseja.
    mensagem_de_erro: Texto que você quer que o usuário leia após um erro genérico.
    """
    while True:
        try:
            resposta_do_argumento = input(pergunta) # Resposta do usuário
            tamanho_string = len(resposta_do_argumento) # Tamanho da string digitada
            num_or_str = resposta_do_argumento.isdigit() # Verifica se existe número

            # Verifica se é número ou letra.
            if num_or_str == True:
                num_or_str = 'número(s)'
            else:
                num_or_str = 'letra(s)'

            
            resposta_do_argumento = resposta_do_argumento.upper() # Transforma string em maiúsculo.
            if tamanho_string == 1:
                if primeira_cond == resposta_do_argumento:
                    return primeira_cond # Retorna o valor da primeira condição

                elif segundo_cond == resposta_do_argumento:
                    return segundo_cond # Retorna o valor da segunda condição

                else:
                    print(f'Você digitou: "{resposta_do_argumento}".')
                    continue
            else:
                print(f'Você digitou {tamanho_string} {num_or_str}')
                continue
        except:
            print(mensagem_de_erro) # Mensagem de erro genérico
            continue

#                 <<< ----===<  Fim da Função  >===---- >>>


# === <<< << << << Função de Caracteres Necessários >> >> >> >>> === >> >> >> >>>

def caractres_repetidos_especial(senha):
    """
    Verifica todos caracteres necessários que deve ter na senha
    """
    def repetidos_tamanho():
        tamanho = len(senha) # Tamanho da senha
        for caracter in senha:
            resultado = caracter * tamanho # Multiplica o caractere pela string para ver se tem repetido
            if resultado == senha:
                return True # Caracteres repetidos mais de 10 vezes
            return False # Senha OK !!!


    def repetidos_4_digitos():
        for i in senha:
            res = i * 4
            if res in senha: # Multiplica o caractere pela string e verifica quantos são iguais
                return True # Caracteres repetidos mais de 4 vezes
        return False # Senha OK !!!


    def caracteres_especiais():
        caracteres = '!@#$%¨&*()_-=+/.,;:?ç^~]}[{' # Lista de caractere que deve ter
        for i in senha:
            if i in caracteres:
                return True # Tem
        return False # Não tem
    

    def um_numero_obrigatorio():
        numeros = '0123456789' # Lista de número que deve ter
        for i in senha:
            if i in numeros:
                return True # Tem
        return False # Não tem

    # Controles de acesso para verificar atuações
    repetidos_4 = repetidos_4_digitos()
    repetidos_tam = repetidos_tamanho()
    carac_especial = caracteres_especiais()
    num_obrigatorio = um_numero_obrigatorio()
    if carac_especial == True:
        if num_obrigatorio == True:
            if repetidos_tam == False:
                if repetidos_4 == False:
                    print('Sua senha foi válidada com SUCESSO')
                    return True
                else:
                    print('Sua senha tem 4 caracteres ou mais repetidos.')
                    return False
            else:
                print('Sua senha tem todos caracteres repetidos.')
                return False
        else:
            print('É obrigatório pelo menos um número.')
            return False
    else:
        print('É obrigatório pelo menos um caracter especial.')
        return False

#                 <<< ----===<  Fim da Função  >===---- >>>


# === <<< << << << Função Registrar Usuário >> >> >> >>> === >> >> >> >>>

def registro_de_usuario():
    numero = 2 # Contador, quando chegar em tal número, ele duplica outra contagem "chances de senha"
    chances_de_senha = 0 # Acumulador de chances 
    
    senha_gerada = '' # Senha aleatória que o usuário decide
    while True: # Loop Infinito
        usuario_digitou = input('\nUsuário: ')
        tamanho_usuario = len(usuario_digitou)
        if tamanho_usuario == 0:
            print('Digite seu Usuário para prosseguir.')
            continue
        #   -----------   -----------   -----------   -----------   -----------   -----------

        if chances_de_senha == numero: # Se passar de 2 tentativas, irá pedir pra criar uma senha automática
            decisao_do_gerador_senhas = verificacao_de_string('Digite [S] para criar \
uma senha aleatória, ou [N] para voltar: ', 'S', 'N', 'Houve algum erro inesperado. Tente de novo!!!') 

            if decisao_do_gerador_senhas == 'S': # Se for 'S', ele gera uma senha aleatória
                senha_gerada += senha_automatica() # Senha gerada
                return usuario_digitou, senha_gerada # Return do usuário e a senha
            else:
                numero += 2 # Contador para duplicar o contador de chances
        #   -----------   -----------   -----------   -----------   -----------   -----------

        if len(senha_gerada) == 0: # Tamanho, se for FALSE, ele continue o programa, se VERDADEIRA
            # Ele retorna o valor da senha gerado aleatória

            senha_digitou = input('Senha: ')

            tamanho_senha = len(senha_digitou) # Tamanho string da senha
            if usuario_digitou != senha_digitou: # Não pode ter a senha com o mesmo nome de usuário
                

                if tamanho_senha > 20:
                    print('Número máximo de caracter atingido')
                    chances_de_senha += 1
                    continue # Volta pro loop, no começo da função

                elif tamanho_senha > 8 and tamanho_senha <= 20:
                    senha_validada = caractres_repetidos_especial(senha_digitou)

                    if senha_validada == True:
                        return usuario_digitou, senha_digitou # Se a senha for válidada, retorna pra função

                    elif senha_validada == False: # Se não for, irá quer fazer outra senha
                        chances_de_senha += 1
                        continue 

                elif tamanho_senha > 5 and tamanho_senha <= 8:
                    senha_validada = caractres_repetidos_especial(senha_digitou)
                    if senha_validada == True:
                        return usuario_digitou, senha_digitou
                    elif senha_validada == False:
                        chances_de_senha += 1
                        continue


                elif tamanho_senha <= 5:
                    print('Tamanho da senha FRACO, tente outra senha.') # Não passou
                    chances_de_senha += 1 # Acumulador de chances
                    continue
                

            else:
                print('Não pode ter a SENHA igual a do USUÁRIO')
                chances_de_senha += 1 # Acumulador de chances
                continue

#                 <<< ----===<  Fim da Função  >===---- >>>

# === <<< << << << Função Validação de CPF >> >> >> >>> === >> >> >> >>>


def validacao_cpf():
    while True:    
        cpf = input('Digite o CPF: ').replace('.', '').replace(' ','').replace('-','') # Para usuário digitar o CPF
        tamanho_cpf = len(cpf) # Dar o tamanho de caracteres para ser usado depois
        se_for_numero = cpf.isdigit() # Volta valor Booleano, se tem string dentro da variavel cpf

        if se_for_numero == True:
            if tamanho_cpf == 11:
                numero_da_multiplicacao = 10 # Contagem regressiva começando do 10, do primeiro dígito
                soma = 0
                nove_digitos = cpf[:9]
                for digito in nove_digitos:
                    soma += int(digito) * numero_da_multiplicacao
                    numero_da_multiplicacao -= 1 # Contador
                resultado = (soma * 10)  % 11
                primeiro_digito = resultado if resultado <= 9 else 0 # Se for menor ou igual a 9, ser o proprio
                # resultado, se for maior que 9, o valor será "0"

                numero_da_multiplicacao2 = 11 # Contagem regressiva começando do 11, do segundo dígito
                soma2 = 0
                dez_digitos = cpf[:10]
                for digito2 in dez_digitos:
                    soma2 += int(digito2) * numero_da_multiplicacao2
                    numero_da_multiplicacao2 -= 1 # Contador
                resultado2 = (soma2 * 10) % 11
                segundo_digito = resultado2 if resultado2 <= 9 else 0  # Se for menor ou igual a 9, ser o proprio
                # resultado, se for maior que 9, o valor será "0"

                if primeiro_digito == int(cpf[9]) and segundo_digito == int(cpf[10]):
                    cpf_novo = '' # Cpf novo, para imprimir na tela o cpf completo

                    # Loop de contagem, para cada (tantas letras), criar um carácter no cpf_novo
                    contagem = 0
                    for letra in cpf:
                        cpf_novo += letra
                        contagem += 1
                        if contagem == 3:
                            cpf_novo += '.'
                        elif contagem == 6:
                            cpf_novo += '.'
                        elif contagem == 9:
                            cpf_novo += '-'
                    print('CPF CADASTRADO') # Após o CPF ser validado, encerra o Programa
                    return True, cpf_novo
                else:
                    print('CPF INVÁLIDO') # Se o CPF for inválido, encerra o Programa
                    return False
    # Caso o usuário digite algum valor inválido
            else:
                print(f'Você digitou {tamanho_cpf} números de CPF!!!\nTente de novo.')
                continue
        else:
            print(f'Tente de novo, você digitou {cpf}.')

#                 <<< ----===<  Fim da Função  >===---- >>>


# === <<< << << << Função Validação de Email >> >> >> >>> === >> >> >> >>>

def validar_o_email(email_digitado):
    def validar_arroba(): 
        if '@' in email_digitado:
            if 'gmail' in email_digitado:
                return True
            elif 'outlook' in email_digitado:
                return True
            elif 'hotmail' in email_digitado: 
                return True
            elif 'yahoo' in email_digitado:
                return True
            elif 'icloud' in email_digitado:
                return True
            elif 'gmx' in email_digitado:
                return True
            elif 'hey' in email_digitado:
                return True
            elif 'zoho' in email_digitado:
                return True
            elif 'proton' in email_digitado:
                return True
            elif 'aol' in email_digitado:
                return True
            else:
                print('Nenhum desses Mail foi correspondido, Observa uns mais famosos:')
                print('outlook.com\ngmail.com\nyahoo.com\nhotmail.com\nicloud.com')
                return False
        else:
            print('Falta o "@" no seu e-mail')
            return False

# ------------------------------------------------------

    if '.br' in email_digitado: 
        if '.com' in email_digitado:
            existe_ou_nao = validar_arroba()
            return existe_ou_nao

    elif '.com' in email_digitado:
        existe_ou_nao = validar_arroba()
        return existe_ou_nao
        
    else:
        print('E-mail incompleto')
        return False

#                 <<< ----===<  Fim da Função  >===---- >>>


# === <<< << << << Função Validação de Email >> >> >> >>> === >> >> >> >>>

def validacao_telefone(telefone):
    numeros_validos = '0123456789'
    contagem_acerto = 0
    contagem_erro = 0
    tamanho_telefone = len(telefone)
    telefone_vazio = ''

    if tamanho_telefone == 11:
        for num_val in numeros_validos:
            for num_telefone in telefone:

                if num_val == num_telefone:
                    contagem_acerto += 1
                else:
                    contagem_erro += 1
        
        if contagem_erro != 99 or contagem_acerto != 11:
            print(f'Valor incorreto, você digitou "{telefone}"')
            return False
        else:
            print('Telefone Correto')
            return True
    else:
        print('Tamanho inválido, você não digitou 11 dígitos de telefone')
        return False

#                 <<< ----===<  Fim da Função  >===---- >>>


# === <<< << << << Função de Loop de Nome >> >> >> >>> === >> >> >> >>>

def nome_loop(pergunta):
    while True: # Enquanto não digitar o nome, ficará no looping
        string = input(pergunta)
        tamanho_nome = len(string)
        if tamanho_nome >= 1:
            return string
        else:
            print('Digita o seu nome para prosseguir.')

#                 <<< ----===<  Fim da Função  >===---- >>>


# Estrutura inicial do Programa
print('*===---===---=== Registrar ===---===---===')
erros = 0 # Contagem de erros. Para recomeçar os dados
editar_dados = 0 # Controle de dados, caso for editar os dados


nome = nome_loop('Nome: ')
usuario, senha = registro_de_usuario()


while True: # Controle de erros. ------------------------->>>>
    if erros >= 3: # Se tiver 3 erros ou mais, ele repetirar o Usuário e Senha
        nome = nome_loop('Nome: ')
        usuario, senha = registro_de_usuario()



    if editar_dados >= 1: #Editar dados. ---------------------------->>>>
        nome = nome_loop('Nome: ')
        usuario, senha = registro_de_usuario()



    print()
    telefone_digitado = input('Telefone (com DDD): ')
    if telefone_digitado:
        resultado_telefone = validacao_telefone(telefone_digitado)
        if resultado_telefone == False:
            telefone_digitado = ''

    print()
    resultado_cpf, cpf_novo = validacao_cpf()
    if resultado_cpf == False:
        erros += 1


    print()
    while True:
        email_digitado = input('E-mail: ')
        resultado_email = validar_o_email(email_digitado)
        if resultado_email == True:
            break




    if resultado_cpf == True and resultado_email == True:
        print(f'\nUsuário: {usuario}\nSenha: {senha}\nCPF: {cpf_novo}\nE-mail: {email_digitado}\nTelefone: {telefone_digitado}')
        confirmar_registro = verificacao_de_string('Confirmar seus dados? [S/N]: ', 'S', 'N', 'Você digitou errado,\
 digita "S" para SIM. digita "N" para NÃO\n')

        if confirmar_registro == 'S': # Salva os dados na lista
            pessoa_cadastrada ={'Nome':nome,
                    'Usuário':usuario,
                    'Senha':senha,
                    'CPF':cpf_novo,
                    'E-mail':email_digitado,
                    'Telefone':telefone_digitado}
            contas_cadastradas = []
            contas_cadastradas.append(pessoa_cadastrada.copy())
            break

        elif confirmar_registro == 'N': # Editar os dados
            editar_dados += 1
            continue 





# Contas cadastradas 
print('==================== CADASTRADO ========================')
print()
for pessoa in contas_cadastradas:
    for busca, dados in pessoa.items():
        print(f'\033[1m{busca} :\033[0m {dados}\n')
print('========================================================')
print()