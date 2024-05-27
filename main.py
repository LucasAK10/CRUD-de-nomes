#lista 
lista = []

# inserir pessoa na lista 
nome = input("Digite o nome a ser inserido: ")
lista.append(nome)
print('Pessoa inserida com sucesso!')

# listar pessoas
if lista:
    print('Lista de pessoas')

else:
    print("Pessoas cadastradas: ")
    for index, pessoa in enumerate(lista, start=1):
        print(f"{index}. {pessoa}")

# pesquisar pessoas na lista
nome = input("Digite o nome da pessoa a ser pesquisada: ")
if nome in lista:
    print(f"{nome} está na lista de pessoas cadastradas.")
else:
    print(f"{nome} não encontrado na lista.")


# ordenar lista
lista.sort()
print("Lista ordenada por ordem alfabética.")

# atualizar nomes
nome_antigo = input("Digite o nome a ser atualizado: ")
if nome_antigo in lista:
        index = lista.index(nome_antigo)
        novo_nome = input("Digite o novo nome: ")
        lista[index] = novo_nome
        print("Nome atualizado com sucesso!")
else:
        print(f"{nome_antigo} não encontrado na lista.")

# deletar nome da lista
nome = input("Digite o nome da pessoa a ser removida: ")
if nome in lista:
    lista.remove(nome)
    print("Nome removido da lista.")
else:
    print(f"{nome} não encontrado na lista.")


# lista de pessoas 
lista_de_pessoas = []

while True:
        print("\n----- Menu -----")
        print("1. Inserir pessoa na lista")
        print("2. Listar pessoas cadastradas")
        print("3. Pesquisar pelo nome de uma pessoa")
        print("4. Ordenar a lista por ordem alfabética")
        print("5. Atualizar nome")
        print("6. Deletar nome da lista")
        print("7. Sair do programa")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            inserir_pessoa(lista_de_pessoas)
        elif escolha == "2":
            listar_pessoas(lista_de_pessoas)
        elif escolha == "3":
            pesquisar_pessoa(lista_de_pessoas)
        elif escolha == "4":
            ordenar_lista(lista_de_pessoas)
        elif escolha == "5":
            atualizar_nome(lista_de_pessoas)
        elif escolha == "6":
            deletar_nome(lista_de_pessoas)
        elif escolha == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

