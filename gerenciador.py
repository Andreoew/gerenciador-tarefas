def adicionar_tarefa(tarefas, nome_tarefa):
  #tarefa: nome da tarefa
  # completada: indicar se essa tarefa já foi completada ou não
  tarefa = {"tarefa": nome_tarefa, "completada": False}
  tarefas.append(tarefa)
  print("\n✅ Adicionando...")
  # print(f"✅ Tarefa [{nome_tarefa}] foi adicionada com sucesso!")
  print(f"Tarefa \033[1;32m{nome_tarefa}\033[0m foi adicionada com sucesso!")
  return 

# ver todas a tarefas
def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  if len(tarefas) == 0:
    print("\033[1;31mNão existe tarefas registradas.\033[0m")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["completada"] else " "
    nome_tarefa = tarefa["tarefa"]
    print(f"{indice}. [{status}] \033[1;32m{nome_tarefa}\033[0m")
  return

# atualizar nome de uma tarefa
def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
    tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
    print("\n✅ sucesso! ✅")
    print(f"Tarefa \033[1;32m{indice_tarefa}\033[0m atualizada para  \033[1;32m{novo_nome_tarefa}\033[0m")
  else:
    print("\n ❌ Erro. ❌")
    print("Índice de tarefa inválido.")
  return

def completar_tarefa(tarefas, indice_tarefa):
  indice_tarefa_ajustado = int(indice_tarefa) - 1
  tarefas[indice_tarefa_ajustado]["completada"] = True
  print(f"Tarefa {indice_tarefa} marcada como completada")
  return

def deletar_tarefas_completadas(tarefas):
  for tarefa in tarefas:
    if tarefa["completada"]:
      tarefas.remove(tarefa)
  print("Tarefas completadas foram deletadas.")
  return

tarefas = []
while True:
  print("\n\033[1;32mMenu do Gerenciador de Lista de tarefas:\033[0m")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Atualizar tarefa")
  print("4. Completar tarefa")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("\n\033[1;33mDigite a sua escolha:\033[0m ")

  if escolha == "1":
    nome_tarefa = input("\n\033[1;33mDigite o nome da tarefa que deseja adicionar:\033[0m ")
    adicionar_tarefa(tarefas, nome_tarefa)
  elif escolha == "2":
    ver_tarefas(tarefas)
  elif escolha == "3":
    ver_tarefas(tarefas)
    indice_tarefa = input("\n\033[1;33mDigite o número da tarefa que deseja atualizar:\033[0m ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
  elif escolha == "4":
    ver_tarefas(tarefas)
    indice_tarefa = input("\n\033[1;33mDigite o número da tarefa que deseja completar:\033[0m ")
    completar_tarefa(tarefas, indice_tarefa)
  elif escolha == "5":
    deletar_tarefas_completadas(tarefas)
    ver_tarefas(tarefas)
  elif escolha == "6":
    break
print("Programa finalizado")