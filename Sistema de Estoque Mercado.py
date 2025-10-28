#Sistema de estoque simples, feito pelo Gustavo Henrique Novaes Gomes, e Paulo Henrique Galvão.

estoque = []

while True:

    print("------Opções------")
    print("1- Adicionar Produtos.")
    print("2- Remover Produtos.")
    print("3- Consultar Estoque Atual.")
    print("4- Sair.", "\n")
    opção = input("Qual Opção Deseja Selecionar? ")


    if opção == "1":
        nome = input("Nome do Produto: ")
        estoque.append(nome)
        print("Produto Adicionado", "\n")


    elif opção == "2":
        nome = input("Nome do produto: ")

        if nome in estoque:
            estoque.remove(nome)
            print("Produto Removido", "\n")

        else:
            print("Produto Não Encontrado", "\n")

    
    elif opção == "3":
        print("Consultando o Estoque", "\n")
        print("No estoque tem", len(estoque), "Produtos", "\n")

        for nome in estoque: 
            print(nome)


    elif opção == "4":
        print("Encerrando o Sistema")
        break   

    else:
        print("Invalido", "\n")