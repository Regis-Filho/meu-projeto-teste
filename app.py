import requests
import subprocess
import os
import sys


def verificar_atualizacao():
    try:
        versao_atual = open('versao.txt').read().strip()
        versao_remota = requests.get('https://raw.githubusercontent.com/Regis-Filho/meu-projeto-teste/refs/heads/main/main/versao.txt').text.strip()
        if versao_atual != versao_remota:
            print('Nova versão disponível!')
            print(f'Versão atual: {versao_atual}')
            print(f'Versão remota: {versao_remota}')
            subprocess.Popen(['atalizador.exe'])  # Inicia o script de atualização
            print('Nova versão disponível!.instalando...')
            print(versao_remota)




    except Exception as e:
        print(f'Erro ao verificar atualização: {e}')
        


verificar_atualizacao()




print('Olá, mundo!')

input('Pressione Enter para sair...')
