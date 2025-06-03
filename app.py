import requests
import subprocess
import os
import sys


def verificar_atualizacao():
    try:
        versao_atual = open('versao.txt').read().strip()
        versao_remota = requests.get('https://raw.githubusercontent.com/Regis-Filho/MEU-PROJETO-TESTE/main/versao.txt').text.strip()
        if versao_atual != versao_remota:
            print('Nova versão disponível!.instalando...')
            subprocess.Popen(['atualizador.exe'])
            sys.exit()



    except Exception as e:
        print(f'Erro ao verificar atualização: {e}')
        


verificar_atualizacao()




print('Olá, mundo!')

input('Pressione Enter para sair...')
