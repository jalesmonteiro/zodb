from ZODB import FileStorage, DB
from models import ListaDeTarefas
from transaction import commit
import os
import time

def limpar_tela():
    # Limpa a tela no Windows ou no Linux/MacOS
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Configuração do banco de dados
    storage = FileStorage.FileStorage('tarefas.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root

    # Crie uma lista de tarefas se ela não existir
    if not hasattr(root, 'tarefas'):
        root.tarefas = ListaDeTarefas()
        commit()
    else:
        print("Lista de tarefas já existe.")

    # Acessa a lista de tarefas
    lista_de_tarefas = root.tarefas

    # Exemplo de uso
    while True:
        # Exibir lista de tarefas
        if not lista_de_tarefas.tarefas:
            print("\nNão há tarefas.")
        else:
            print("\nTarefas:")
            for indice, tarefa in enumerate(lista_de_tarefas.tarefas):
                print(f"{indice}: {tarefa}")

        # Exibir menu
        print("\n1. Adicionar tarefa\n2. Remover tarefa\n3. Concluir tarefa\n4. Reabrir tarefa\n5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            descricao = input("Digite a descrição da tarefa: ")
            lista_de_tarefas.adicionar_tarefa(descricao)
            commit()
            print("Tarefa adicionada com sucesso!")
            time.sleep(1)  # Aguarde 1 segundo
            limpar_tela()

        elif escolha == '2':
            if not lista_de_tarefas.tarefas:
                print("Não há tarefas para remover.")
                time.sleep(1)  # Aguarde 1 segundo
                limpar_tela()
            else:
                indice = int(input("\nDigite o índice da tarefa para remover: "))
                lista_de_tarefas.remover_tarefa(indice)
                commit()
                print("Tarefa removida com sucesso!")
                time.sleep(1)  # Aguarde 1 segundo
                limpar_tela()

        elif escolha == '3':
            if not lista_de_tarefas.tarefas:
                print("Não há tarefas para concluir.")
                time.sleep(1)  # Aguarde 1 segundo
                limpar_tela()
            else:
                indice = int(input("\nDigite o índice da tarefa para concluir: "))
                lista_de_tarefas.concluir_tarefa(indice)
                commit()
                print("Tarefa concluída com sucesso!")
                time.sleep(1)  # Aguarde 1 segundo
                limpar_tela()

        elif escolha == '4':
            if not lista_de_tarefas.tarefas:
                print("Não há tarefas para reabrir.")
                time.sleep(1)  # Aguarde 1 segundo
                limpar_tela()
            else:
                indice = int(input("\nDigite o índice da tarefa para reabrir: "))
                lista_de_tarefas.reabrir_tarefa(indice)
                commit()
                print("Tarefa reaberta com sucesso!")
                time.sleep(1)  # Aguarde 1 segundo
                limpar_tela()

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")
            time.sleep(1)  # Aguarde 1 segundo
            limpar_tela()