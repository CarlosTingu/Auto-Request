# -*- coding: utf-8 -*-

import requests
import time 

print('====================================================')
print('=================== AUTO REQUEST ===================')
print('===================   By: Tingu  ===================\n')


header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}

url = input('SITE URL: ')

if url.isnumeric():
    print('URL INVÁLIDA')
    exit()
if url == '':
    print('URL VÁZIA')
    exit()
    
tempo = input('TEMPO POR REQUEST: ')

if tempo.isalpha():
    print('TEMPO INVÁLIDO')
    exit()
if tempo == '':
    print('TEMPO VÁZIO')
    exit()

txt = open('proxys.txt', 'r') 
proxyList = txt.readlines() 
    
i = 0

while i < len(proxyList):
    
    proxyDict = dict({'https':'https://{}'.format(proxyList[i])})
    
    print('')
    
    print('{}° REQUEST - MEU IP: {}'.format(i+1, proxyDict['https']))
    
    try:
        res = requests.get(url, headers=header, proxies=proxyDict)
    except:
        print('ERRO INTERNO')
        exit()
        
    if res != '<Response [200]>':
        print('O SITE RECUSOU')
        i += 1
        continue
    else:
        print('O SITE ACEITOU')
        i += 1
        time.sleep(int(tempo))
        

print('\nPROCESSO CONCLUÍDO COM SUCESSO')  
exit()    
    





