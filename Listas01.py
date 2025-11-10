print("Aprendendo Listas\n")

caixa = []

while True:

    print("Oque deseja fazer?")
    print("1 Adicionar Itens?")
    print("2 remover Itens?")
    print("3 Mostra tudo da lista?")
    desi = input("Qual opção: ")

    if desi == "1":
     caixa.append(input("Oque quer adicionar? "))

    elif desi == "2":
     caixa.remove(input("Oque quer remover? "))

    elif desi == "3":
      print(caixa)

    elif desi == "4":
        break
