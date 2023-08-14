import requests
import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')
def pegar_cotacao(moeda): # Requests.get entra na internet e busca API
    cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    print(cotacoes)
    cotacoes = cotacoes.json() # Traduz um Json para Python

    if moeda == 'dólar':
        return cotacoes['USDBRL']['bid']

    elif moeda == 'euro':
        return cotacoes['EURBRL']['bid']

    elif moeda == 'bitcoin':
        return cotacoes['BTCBRL']['bid']



estrutura = [[sg.Text('Escolha qual moeda deseja ver a cotação atual')],
             [sg.Button('Dólar'),
             sg.Button('Euro'),
             sg.Button('Bitcoin')],
             [sg.Text('Esperando a moeda...', key='-UPDATE_TXT-')]]
janela = sg.Window('Cotação de moeda', estrutura, element_justification='c')


while True:

    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Dólar':
        moeda_pegado = pegar_cotacao('dólar')
        janela['-UPDATE_TXT-'].update('Dólar: '+ moeda_pegado)

    if event == 'Euro':
        moeda_pegado = pegar_cotacao('euro')
        janela['-UPDATE_TXT-'].update('Euro: '+ moeda_pegado)

    if event == 'Bitcoin':
        moeda_pegado = pegar_cotacao('bitcoin')
        janela['-UPDATE_TXT-'].update('Bitcoin: '+ moeda_pegado)

janela.close()