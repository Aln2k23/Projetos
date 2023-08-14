import PySimpleGUI as sg # Interface
import random
import pyodbc
import smtplib
import email.message


def enviar_email(email_destinatario): 
            password = 'flgvyttwsyrnmsbd'  # Senha App gmail gerada automática
            print(email_destinatario)

            senha_autenticacao = ''
            for i in range(6):
                gerador = random.choice('0123456789')
                senha_autenticacao += gerador

            titulo = 'Recuperação de senha - guimera'

            descricao_email = f"""Olá guimerano, esqueceu a senha né.<br>
            Segue abaixo seu código de autenticação de Usuário:
            <h2> {senha_autenticacao} </h2>"""



            msg = email.message.Message()
            msg['Subject'] = titulo # Título
            msg['From'] = 'guimera.sistem@gmail.com' # Remetente
            msg['To'] = f'{email_destinatario}' # destinatário

            msg.add_header('Content-Type', 'text/html') # Configurações site html
            msg.set_payload(descricao_email) # Corpo email/descrição

            s = smtplib.SMTP('smtp.gmail.com: 587') # Servidor e porta de acesso ao Gmail
            s.starttls() # Executação da porta e servidor
            # Login Credentials for sending the mail
            s.login(msg['From'], password) # Login da conta: email, e a senha
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) # Envio da mensagem
            print('Email enviado')
            return senha_autenticacao



# CONEXÃO COM SERVIDOR
dados_conexao = ('Driver={SQL Server};'
                 'Server=DESKTOP-VG7OCP2\SQLALAN;' 
                 'Database=InterfaceGrafica;')

conexao = pyodbc.connect(dados_conexao)
print('Conexão Efetuada!')
cursor = conexao.cursor()



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



def validar_o_email(email_digitado):
    def validar_arroba(): 
        if '@' in email_digitado:
            return True
        return False

    if '.br' in email_digitado: 
        if '.com' in email_digitado:
            existe_ou_nao = validar_arroba()
            return existe_ou_nao

    elif '.com' in email_digitado:
        existe_ou_nao = validar_arroba()
        return existe_ou_nao
        
    else:
        return False



def janela_login():
    sg.theme('Reddit')
    estrutura_janela_login = [
        [sg.Image('avatar100-removebg-preview.png')],
        [sg.Push(),sg.Text('E-mail ou Usuário'), sg.Input(key='-LOGIN_ACESS-'),sg.Push()],
        [sg.Push(),sg.Text('        Senha        '), sg.Input(key='-LOGIN_PASS-',password_char='*'),sg.Push()],
        [sg.Push(),sg.Text('', key='-ERROLOG-'),sg.Push()],
        [sg.Text('         '),sg.Button('Logar'),sg.Text('    '), sg.Button('Não sou registrado'),sg.Button('Esqueci a senha'),sg.Push(),]
    ]
        
    return sg.Window('Tela de login', estrutura_janela_login,size=(500,245) , element_justification='c', finalize=True)



def janela_registro():
    sg.theme('Reddit')
    estrutura_janela_registro = [
        [sg.Push(),sg.Image('avatar100-removebg-preview.png'),sg.Push()],
        [sg.Text('      Nome'),sg.Push(), sg.Input(key='-NOME-',size=(50)),sg.Push()],
        [sg.Text('   Usuário'),sg.Push(), sg.Input(key='-USUARIO-',size=(50)),sg.Push()],
        [sg.Text('     Senha'),sg.Push(), sg.Input(key='-SENHA-',size=(50)),sg.Push()],
        [sg.Text(' Confirmar'),sg.Push(), sg.Input(key='-CONFIRMAR-',size=(50)),sg.Push()],
        [sg.Text('     E-mail'),sg.Push(), sg.Input(key='-EMAIL-',size=(50)),sg.Push()],
        [sg.Push(),sg.Text('',key='-ERRO-'),sg.Push()],
        # BOTÕES
        [sg.Push(),sg.Button('Registrar'),sg.Button('Voltar'),sg.Button('Gerar senha forte'), sg.Push()]
    ]
        
    return sg.Window('Tela de registro', estrutura_janela_registro,size=(550,320) , finalize=True)



def janela_recuperacao():
    sg.theme('Reddit')
    estrutura = [[sg.Text('Digite seu E-mail abaixo')], # 1
                 [sg.Input(key='-EMAIL_RECUPERACAO-')], # 2
                 [sg.Text('',key='-EMAIL_ERROR-')], # 3
                 [sg.Button('Enviar'),sg.Button('Retornar')], # 4
                 ]
    return sg.Window('Recuperação', layout=estrutura,size=(250,117), element_justification='c', finalize=True)

#                 <<< ----===<  Fim da Função  >===---- >>

def janela_nova_senha():
    sg.theme('Reddit')
    layout = [[sg.Push(),sg.T('Nova Senha'),sg.I(key='-NOVA_SENHA-')],
              [sg.Push(),sg.T(' Confirmar '),sg.I(key='-CONFIRMAR_NOVA_SENHA-')],
              [sg.Push(),sg.T('', key='-SENHA_INCORRETAS-'),sg.Push()],
              [sg.Push(),sg.Button('Confirmar'),sg.Push()]]

    return sg.Window('Nova Senha', layout=layout, finalize=True)



def janela_autenticacao():
    sg.theme('Reddit')
    layout = [[sg.T('Digite o código de autenticação')],
              [sg.I(size=(6),key='-USUARIO_CODIGO-')],
              [sg.T('',key='-AUTENTICAR_ERRO-')],
              [sg.Button('Autenticar')]]

    return sg.Window('Autenticação', layout=layout,element_justification='c',finalize=True)


janela_1, janela_2, janela_3, janela_4, janela_5 = janela_login(), None, None, None, None

while True:
    windows, events, values = sg.read_all_windows()
    
    def sem_erro():
        janela_2['-ERRO-'].update('')

    def caracteres_especiais(chave):
        caracteres = '[!@#$%&*]' # Lista de caractere que deve ter
        for i in values[chave]:
            if i in caracteres:
                return True # Tem
        return False # Não tem
    

    def um_numero_obrigatorio(chave):
        numeros = '0123456789' # Lista de número que deve ter
        for i in values[chave]:
            if i in numeros:
                return True # Tem
        return False # Não tem
# ----------------------------------------------------------------------------------


    if windows == janela_1 and events == sg.WIN_CLOSED: 
        break

    elif windows == janela_2 and events == sg.WIN_CLOSED:
        break 

    elif windows == janela_3 and events == sg.WIN_CLOSED:
        break

    elif windows == janela_4 and events == sg.WIN_CLOSED:
        break

    elif windows == janela_5 and events == sg.WIN_CLOSED:
        break


    if windows == janela_1 and events == 'Logar': # Evento Logar
        ver_senha = janela_1['-ERROLOG-']
        print(ver_senha)
        acess = values['-LOGIN_ACESS-']
        password_login = values['-LOGIN_PASS-']

        # Query
        consultar_tabela = f"""
        select user_acess, email_user, password_user from UsuariosCadastrados
        """
        cursor.execute(consultar_tabela) # Executa a consulta
        linhas_sql = cursor.fetchall() # Consulta todas as linhas
        

        for cada_linha in linhas_sql: # Looping em todas as linhas
            if cada_linha[0] == acess or cada_linha[1] == acess: # verificação de conta
                senha_correta = cada_linha[2] == password_login
                if senha_correta == True:
                    sg.popup_ok('Iniciando...')
                    # Fazer uma função que entre 
                else:
                    janela_1['-ERROLOG-'].update('Senha incorreta')         

        janela_1['-ERROLOG-'].update('Usuário ou E-mail não registrados')



    if windows == janela_2 and events == 'Registrar': # Registrar
        # VALIDAR CADASTRO, E COLOCAR NO BANCO DE DADOS
        def dados_validados():
            if len(values['-NOME-']) >= 1:
                sem_erro()

                if values['-USUARIO-']:
                    tamanho_usuario = len(values['-USUARIO-'])
                    if tamanho_usuario >= 3:
                        sem_erro()

                        if  len(values['-SENHA-']) >= 4 and len(values['-SENHA-']) <= 20:
                            sim_nao_number = um_numero_obrigatorio('-SENHA-')
                            if sim_nao_number == True:
                                sim_nao_especial = caracteres_especiais('-SENHA-')
                                if sim_nao_especial == True:
                                    if values['-SENHA-'] == values['-CONFIRMAR-']:
                                        if values['-EMAIL-']:
                                            sem_erro()
                                            resultado_email = validar_o_email(values['-EMAIL-'])
                                            if resultado_email == True:
                                                sem_erro()
                                                return True
                                            else:
                                                janela_2['-ERRO-'].update('E-mail Incorreto')
                                        else:
                                            janela_2['-ERRO-'].update('Você não digitou seu E-mail')
                                    else:
                                        janela_2['-ERRO-'].update('As senhas não coincidem')
                                else:
                                    janela_2['-ERRO-'].update('É necessário pelo menos um carácter especial [!@#$%&*]')
                            else:
                                janela_2['-ERRO-'].update('É necessário pelo menos um número')                   
                        else:
                            janela_2['-ERRO-'].update('Deve ter no minímo 4 caracteres, e no máximo 20 caracteres na Senha')                    
                    else:
                        janela_2['-ERRO-'].update('Deve ter 3 ou mais caracteres no Usuário')
                else:
                    janela_2['-ERRO-'].update('Você não escreveu o Usuário')
            else:
                janela_2['-ERRO-'].update('Você não escreveu seu Nome')
        dados_validos_sim_nao = dados_validados()

        # Inserir dados da pessoas cadastrada dentro do banco de dados
        if dados_validos_sim_nao == True:
            name_user = values['-NOME-']
            user_acess = values['-USUARIO-']
            email_user = values['-EMAIL-']
            password_user = values['-SENHA-']
            # Comando para registrar no banco de dados
            command_register = f""" 
            INSERT INTO UsuariosCadastrados (name_user, user_acess, email_user, password_user)
            VALUES ('{name_user}', '{user_acess}', '{email_user}','{password_user}')
            """
            # Execução do Comando
            cursor.execute(command_register)
            cursor.commit()
            sg.popup_timed('Usuário Registrado')
            janela_2.hide()
            janela_1.un_hide()



    if windows == janela_1 and events == 'Não sou registrado': # Abrir janela de registro
        janela_2 = janela_registro()
        janela_1.hide()

           

    if windows == janela_1 and events == 'Esqueci a senha':
        janela_3 = janela_recuperacao()
        janela_1.hide()



    if windows == janela_3 and events == 'Enviar':
        email_digitado = values['-EMAIL_RECUPERACAO-']
        
        comand_consult = f"""
        select email_user from UsuariosCadastrados
        where '{email_digitado}' = email_user
        """
        cursor.execute(comand_consult) # Executa a consulta
        busca = cursor.fetchall() # Consulta todas as linhas
        
        tamanho = len(busca)
        if tamanho == 1:
            senha_autenticacao = enviar_email(email_digitado)
            sg.popup_timed('Código enviado para o E-mail.')
            janela_4 = janela_autenticacao()
            janela_3.hide()
        
        
            
        else:
            janela_3['-EMAIL_ERROR-'].update('Este email não está registrado')
             
        # 1 - Verificar se o e-mail existe no banco de dados, SE não for key='Este email não existe'
        # 2 - Criar popuptimer 'Código de autenticação enviado email'
        # 3 - 



    if windows == janela_4 and events == 'Autenticar':
        Usuario_codigo_autentic = values['-USUARIO_CODIGO-']
        if Usuario_codigo_autentic == senha_autenticacao:
            janela_5 = janela_nova_senha()
            janela_4.hide()
        else:
            janela_4['-AUTENTICAR_ERRO-'].update('Código está incorreto')



    if windows == janela_2 and events == 'Voltar': # Voltar a tela de login
        janela_2.hide()
        janela_1.un_hide()



    if windows == janela_5 and events == 'Confirmar':
        nova_senha = values['-NOVA_SENHA-']
        confir_senha = values['-CONFIRMAR_NOVA_SENHA-']
    
        print(nova_senha, confir_senha)
        query_password_antiga = f"""
        select email_user, password_user from UsuariosCadastrados
        where '{email_digitado}' = email_user
        """
        cursor.execute(query_password_antiga)
        line_corret = cursor.fetchall()
        email_colum = line_corret[0][0]
        passw_colum =line_corret[0][1]
        tamanho_senhas = len(nova_senha)
        if tamanho_senhas >= 4 and tamanho_senhas <= 20:
            sim_nao_number2 = um_numero_obrigatorio('-NOVA_SENHA-')
            if sim_nao_number2 == True:
                sim_nao_especial2 = caracteres_especiais('-NOVA_SENHA-')
                if sim_nao_especial2 == True:
                    if nova_senha == confir_senha:
                        if passw_colum != nova_senha:
                            query_update_passw = f"""
                            update UsuariosCadastrados
                            set password_user = '{nova_senha}'
                            where password_user = '{passw_colum}'
                            """
                            cursor.execute(query_update_passw)
                            cursor.commit()
                            sg.popup_timed('Recuperação bem sucedida!')
                            janela_5.hide()
                            janela_1.un_hide()
                        else:
                            janela_5['-SENHA_INCORRETAS-'].update('Não pode ser a mesma senha anterior')
                    else:
                        janela_5['-SENHA_INCORRETAS-'].update('As senhas não coincidem')
                else:
                    janela_5['-SENHA_INCORRETAS-'].update('É necessário pelo menos um carácter especial [!@#$%&*]')
            else:
                janela_5['-SENHA_INCORRETAS-'].update('É necessário pelo menos um número') 
        else:
            janela_5['-SENHA_INCORRETAS-'].update('Deve ter no minímo 4 caracteres, e no máximo 20 caracteres na Senha')


    if windows == janela_3 and events == 'Retornar':
        janela_3.hide()
        janela_1.un_hide()
        


    if windows == janela_2 and events == 'Gerar senha forte': # Gera uma senha automática forte
        senha_gerada = senha_automatica()
        janela_2['-SENHA-'].update(senha_gerada)
        janela_2['-CONFIRMAR-'].update(senha_gerada)