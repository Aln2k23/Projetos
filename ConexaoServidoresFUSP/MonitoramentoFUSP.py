from ConnectionServers import ConnectionServers
from time import sleep
from SeeSites import SeeSites

# Loopback
loopback, ip = ConnectionServers.Ping_Hosts('127.0.0.1')
ConnectionServers.Validate_Datas(loopback, ip)

# Site aberto (status)
SeeSites('https://fusp.org.br/')
SeeSites('https://managerweb.fusp.org.br/#/login')

# Sites IP
fusp, ip = ConnectionServers.Ping_Hosts('fusp.org.br')
ConnectionServers.Validate_Datas(fusp, ip)

managerweb, ip = ConnectionServers.Ping_Hosts('managerweb.fusp.org.br')
ConnectionServers.Validate_Datas(managerweb, ip)


# Servidores

youtube, ip = ConnectionServers.Ping_Hosts('youtube.com')
ConnectionServers.Validate_Datas(youtube, ip)

gmail, ip = ConnectionServers.Ping_Hosts('gmail.com')
ConnectionServers.Validate_Datas(gmail, ip)

servidorteste, ip = ConnectionServers.Ping_Hosts('srvimpressora')
ConnectionServers.Validate_Datas(servidorteste, ip)



print('\nFim do monitoramento, será efetuado novamente daqui a 1 hora.')
sleep(5)
