import time 
from selenium import webdriver
import pyautogui 
import os 
import datetime


#Adquire e formata a data de hoje
def datadehoje():
    hoje = datetime.date.today()
    hoje = list(str(hoje))[5::]
    hoje = ''.join(hoje)
    return hoje

#Separa as strings de dados apara ficar só com o número de infectados e de óbitos
def separar(item):
    item = item.split('\t')
    item[-1] = item[-1].split('\n')[0]

    return item


#Checa se o útimo dado é igual, se nao for o arquivo é atualizado
def attfile(novainfo):
    o = open('data.txt','r+')
    dados = []
    for i in o.readlines():
        dados.append(i)
    if separar(dados[-1])[1:] == novainfo:
        return
    else:
        o.write(f'{datadehoje()}\t{novainfo[0]}\t{novainfo[1]}\n')
        print(f'Atualizado em {time.ctime()}')
    o.close()
    os.system(f'python3 sms.py {novainfo[0]} {novainfo[1]}')

def getcasenumbers():
    o = open('COVID2.html', 'r', encoding = 'utf8')
    casos = []
    file = o.readlines()
    for i in file:
        if 'Brazil' in i:
            indice = file.index(i)
            casos.append(file[indice+1])
            casos.append(file[indice+3])
            break
    o.close()

    dados = []
    for i in casos:
        dados.append(i.split('>')[1])

    dados[0] = dados[0].split('<')[0]
    dados[1] = dados[1].split(' ')[0]
    return dados







URL = 'https://www.worldometers.info/coronavirus/'

pyautogui.FAILSAFE = False

counter = 0

while True:
    counter += 1
    # open page with selenium

#    block = webdriver.ChromeOptions()
#    block.add_extension('adblock.crx')
    driver = webdriver.Chrome()
    try:
        driver.get(URL)
    
    #Sleep to ensure page to load properly
        time.sleep(60)

    # open 'Save as...' to save html and assets
        pyautogui.hotkey('ctrl', 's')
        time.sleep(10)
        pyautogui.typewrite('/home/pi/Scripts/Python/Corona/COVID2')

        time.sleep(5)

        pyautogui.hotkey('enter')

        time.sleep(5)

        pyautogui.hotkey('enter')

#   time to download the page
        time.sleep(300)

        driver.quit()
    except:
        print('Erro de novo')
        driver.quit()

    try:
        os.system('rm -r COVID2_files')

    except:
        print('Sem COVID2_files dessa vez')

    print(f'Iteração de número {counter} terminada em {time.ctime()}\n')

    try:

        attfile(getcasenumbers())

        time.sleep(5)

        os.system('python3 plot.py')
        print('Plotado')

    except:

        print('Exception, pulando iteração')

    time.sleep(3600)
