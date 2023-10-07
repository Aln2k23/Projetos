import PySimpleGUI as sg
import os
import time


def window_alert():
        sg.theme('LightGray1')
        layout_alert = [ [sg.Push(),sg.T('Você está prestes a instalar o Pacote Office com chave de ativação'),sg.Push()],
                        [sg.Push(),sg.B('Iniciar instalação'), sg.B('Cancelar'),sg.Push()] ]
        return sg.Window('Assistente de instalação', layout_alert, finalize=True)



def window_verification():
    sg.theme('LightGray1')
    layout_verification = [ [sg.Push(),sg.T('Escolha o Pacote Office que será instalado'),sg.Push()],
                            [sg.Push(),sg.R('Office 2016','group', ), sg.Push(),sg.R('Office 2019', 'group'),sg.Push()],
                            [sg.Push(),sg.T('Licença'), sg.Push()],
                            [sg.I(size=40)],
                            [sg.Push(),sg.B('Prosseguir'), sg.B('Fechar a instalação'),sg.Push()] ] 
    return sg.Window('Verificação das pastas', layout_verification, finalize=True)



PATH2016 = r'C:\OfficeAtivation\ODT2016'
PATH2019 = r'C:\OfficeAtivation\ODT2019'
PATH_SCRIPT = r'C:\Program Files\Microsoft Office\Office16'
control = False




window1, window2 = window_alert(), None
while True:
    windows, event, value = sg.read_all_windows()
    

    if window2 and event == 'Fechar a instalação' or event == sg.WIN_CLOSED or window1 and event == 'Cancelar':
        sg.popup('Assistente cancelado!')
        break

   
    if windows == window1 and event == 'Iniciar instalação':
        window2 = window_verification()
        window1.hide()
         
    
    if windows == window2 and event == 'Prosseguir':
        office2016 = value[0]
        office2019 = value[1]
        license_digit = value[2]
        dir_exist2016 = os.path.isdir(PATH2016) 
        dir_exist2019 = os.path.isdir(PATH2019) 


        if dir_exist2016 == True and dir_exist2019:
            if office2016 == True or office2019 == True:
                if len(license_digit) == 29:
                    if office2016 == True:
                        try:
                            window2.hide()
                            sg.popup_timed('INSTALANDO... Não desligue o computador')
                            os.chdir(PATH2016)
                            os.system('Start setup.exe')
                            control = True
                           
                            break
                        except:
                            print('Error no office16 install')
                    if office2019 == True:
                        try:
                            window2.hide()
                            sg.popup_timed('INSTALANDO... Não desligue o computador')
                            os.chdir(PATH2019)
                            os.system('Setup /download configuration.xml')
                            os.system('Setup /configure configuration.xml')
                            control = True
                            
                            break
                        except:
                            print('Error no office19 install')
                    
                else:
                    sg.popup('Licença incorreta!')
            else:
                sg.popup('Selecione qual sistema será instalado.')
        else:
            sg.popup('Pasta ODT não localizada! Finalizando o sistema')


seconds_run = 0
while control:
    print(seconds_run)
    comand = os.popen('winget list --name Microsoft Office')
    statistic = comand.read()
    os.chdir(PATH_SCRIPT)
    
    try:
        if "Você concorda com todos os termos dos contratos de origem?" in statistic:
            os.popen('Y')
            time.sleep(2)
    except:
        sg.popup('ERROR msstore')


    if 'Microsoft Office Professional Plus 2016' in statistic or 'Office16.PROPLUS' in statistic and office2016 == True:
        try:
            os.chdir(PATH_SCRIPT)    
            time.sleep(20)
            os.system(r"""for /f %x in ('dir /b ..\root\Licenses16\proplusvl_kms*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%x" """)
            time.sleep(3)
            os.system('cscript ospp.vbs /setprt:1688')
            time.sleep(3)
            os.system('cscript ospp.vbs /unpkey:6MWKP >nul')
            time.sleep(3)
            os.system(f'cscript ospp.vbs /inpkey:{license_digit}')
            time.sleep(3)
            os.system('cscript ospp.vbs /sethst:e8.us.to')
            time.sleep(3)
            os.system('cscript ospp.vbs /act')

            sg.popup('Ativado com sucesso!!!')
            break
        except:
            sg.popup('ERROR no 2016')



    if 'Microsoft Office Professional Plus 2019 - pt-br' in statistic or 'ProPlus2019Volume - pt-br' in statistic and office2019 == True:
        try:
            os.chdir(PATH_SCRIPT)
            time.sleep(20)
            time.sleep(3)
            os.system(r"""for /f %x in ('dir /b ..\root\Licenses16\ProPlus2019VL*.xrm-ms') do cscript ospp.vbs /inslic:"..\root\Licenses16\%x" """)
            time.sleep(3)
            os.system('cscript ospp.vbs /setprt:1688')
            time.sleep(3)
            os.system('cscript ospp.vbs /unpkey:6MWKP >nul')
            time.sleep(3)
            os.system(f'cscript ospp.vbs /inpkey:{license_digit}')
            time.sleep(3)
            os.system('cscript ospp.vbs /sethst:e8.us.to')
            time.sleep(3)
            os.system('cscript ospp.vbs /act')

            sg.popup('Ativado com sucesso!!!')
            break
        except:
            sg.popup('ERROR no 2019')
    seconds_run += 1
