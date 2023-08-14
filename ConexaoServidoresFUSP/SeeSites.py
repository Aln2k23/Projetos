import os
import Send

def SeeSites(http):
    cmd = f'curl -I {http}'
    comand = os.popen(cmd)
    statistic = comand.read()

    count = 0
    string_empty = ''
    for letter in statistic:
        if count <= 9:
            string_empty += letter
            count += 1

    print(string_empty)
    string_new = string_empty

    if string_new == 'HTTP/1.1 2':
        print('Servidor está operando corretamente')

    elif string_new == 'HTTP/1.1 3':
        print('Redirecionando')

    elif string_new == 'HTPP/1.1 4':
        print('Servidor cliente está com erro!')
        Send.send('alan.cavalcante@fusp.org.br', 'Servidor cliente está com erro!')

    elif string_new == 'HTTP/1.1 5':
        print('Servidor com erro!')
        Send.send('alan.cavalcante@fusp.org.br','Servidor com erro!')

    else:
        print('Site não encontrado!')
        Send.send('alan.cavalcante@fusp.org.br','Site não encontrado!')