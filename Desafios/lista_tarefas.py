import json
import os
from datetime import datetime

task_file = "tasks.json"


def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, "r", encoding="utf-8") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(task_file, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, task in enumerate(tasks):
            status = "Concluída" if task["data_fechamento"] else "Aberta"
            print(
                f"{i + 1}. {task['descricao']} - Aberta em {task['data_abertura']} - {status}")
            if task["data_fechamento"]:
                print(f"   Concluída em {task['data_fechamento']}")


def add_task():
    descricao = input("Digite a descrição da tarefa: ")
    data_abertura = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks = load_tasks()
    tasks.append({"descricao": descricao,
                 "data_abertura": data_abertura, "data_fechamento": None})
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso!")


def complete_task():
    tasks = load_tasks()
    view_tasks()
    index = int(input("Digite o número da tarefa concluída: ")) - 1
    if 0 <= index < len(tasks) and not tasks[index]["data_fechamento"]:
        tasks[index]["data_fechamento"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")
        save_tasks(tasks)
        print("Tarefa marcada como concluída!")
    else:
        print("Tarefa inválida ou já concluída!")


def edit_task():
    tasks = load_tasks()
    view_tasks()
    index = int(input("Digite o número da tarefa que deseja editar: ")) - 1
    if 0 <= index < len(tasks):
        nova_descricao = input("Digite a nova descrição da tarefa: ")
        tasks[index]["descricao"] = nova_descricao
        save_tasks(tasks)
        print("Tarefa editada com sucesso!")
    else:
        print("Número de tarefa inválido!")


def delete_task():
    tasks = load_tasks()
    view_tasks()
    index = int(input("Digite o número da tarefa a ser excluída: ")) - 1
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)
        print("Tarefa excluída com sucesso!")
    else:
        print("Número de tarefa inválido!")


def main():
    while True:
        print("\nMenu de Controle de Tarefas")
        print("1 - Ver tarefas")
        print("2 - Acrescentar tarefa")
        print("3 - Marcar tarefa como concluída")
        print("4 - Editar uma tarefa")
        print("5 - Excluir uma tarefa")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            view_tasks()
        elif opcao == "2":
            add_task()
        elif opcao == "3":
            complete_task()
        elif opcao == "4":
            edit_task()
        elif opcao == "5":
            delete_task()
        elif opcao == "6":
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
