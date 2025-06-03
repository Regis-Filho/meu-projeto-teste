import requests
import zipfile
import os
import time
import subprocess

url_zip = "https://github.com/Regis-Filho/meu-projeto-teste/raw/refs/heads/main/main/app.zip"

def atualizar():
    print("Baixando nova versão...")
    r = requests.get(url_zip)
    with open("app.zip", "wb") as f:
        f.write(r.content)

    print("Extraindo arquivos...")
    with zipfile.ZipFile("app.zip", 'r') as zip_ref:
        zip_ref.extractall(".")

    print("Atualização concluída!")
    time.sleep(1)

    print("Iniciando app atualizado...")
    subprocess.Popen(["app.exe"])  # Inicia o novo app



if __name__ == "__main__":
    time.sleep(2)  # Simula um tempo de espera antes de iniciar a atualização
    atualizar()