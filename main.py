import datetime
import os
import schedule
import time

print('App on...')

def commit_and_push():
    # Define o caminho para o arquivo main.txt
    path = "/home/the-pedrosantana/pessoal/automated-commiter/main.txt"

    # Pega a data e hora atuais
    now = datetime.datetime.now()

    # Cria a string com a data e hora no formato desejado
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")

    # Adiciona a data ao arquivo main.txt
    with open(path, "w") as file:
        file.write(f"\nData de atualização: {date_string}\n")

    print("Arquivo atualizado com sucesso!")

    # Adiciona as mudanças ao Git e faz commit
    os.system("git add .")
    os.system(f'git commit -m "Adiciona a data de atualização {date_string}"')

    # Faz push das mudanças para o repositório remoto
    os.system("git push origin main")
    print("Mudanças enviadas ao github com sucesso!")

# Agenda a execução do código a cada 1 dia
schedule.every(1).minutes.do(commit_and_push)

counter = 0
while True:
    print(f'Loading... {counter}')
    counter += 1
    if 1 == 1:
        schedule.run_pending()
        time.sleep(1)