tarefas = list()

def adicionar_tarefa (tarefa):
    tarefas.append({"tarefa": tarefa, "concluida": False})
    print(f"Tarefa: {tarefa} |adicionada com sucesso!")

def remover_tarefa(tarefa):
    for item in tarefas:
        if item ["tarefa"] == tarefa:
            tarefas.remove(item)
            print(f"Tarefa: {tarefa} removida com sucesso")
        else:
            print("Tarefa não encontrada")

def visualizar_tarefa ():
    if not tarefas:
        print(f"Nenhuma tarefa encontrado") 
    for i, item in enumerate(tarefas):
        for i in tarefas:
            print(tarefas)

def marcar_concluida(tarefa):
    for item in tarefas:
        if item ["tarefa"] == tarefa:
            item ["concluida"] = True
            print(f"Tarefa {tarefa} marcada como concluída!")
        else:
            print("tarefa não encontrada")

while True:

    # Menu de interação
    print("""
    [1] - para adicionar tarefa
    [2] - para remover tarefa
    [3] - para visualizar tarefas
    [4] - para marcar tarefa como concluida
    [5] - para sair do programa""")
    opcao = input("Opção: ")

    if opcao == "1":
        adicionar = input("Dita a tarefa: ")
        adicionar_tarefa(adicionar)
        continue

    if opcao == "2":
        remov = str(input("diga o nome da tarefa? "))
        remover_tarefa(remov)
        continue
    if opcao == "3":
        visualizar_tarefa()
        continue

    if opcao == "4":
        marcar_concluida(tarefas)
        continue

    if opcao == "5":
        break
    else:
        print("Opção inválida")

jijiojiojiojoijiojijj