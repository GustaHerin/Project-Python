#Dicionarios usam chave e valor para armazenar informações.

#       variavel ={
#           "chave":"valor",
#       }

pers1 = {
    "Nome": "Jake",
    "Idade": 33,
    "Hp": 500,
    "Lv": 999,
    "Dano": 175
}

pers2 = {
    "Nome": "Mai",
    "Idade": 22,
    "Hp": 350,
    "Lv": 899,
    "Dano": 358
}

pers3 = {
    "Nome": "Lila",
    "Idade": 89,
    "Hp": 99,
    "Lv": 500,
    "Dano": 5000
}

print("Quer ver os status completos ou so o Hp? ")
print("1 - So o Hp")
print("2 - Os status completos")
modo = input("Escolha: ")

if modo == "1":
    while True:
        print("Personagens do Jogo")
        print("1 - Jake")
        print("2 - Mai")
        print("3 - lila")
        name = input("Qual personagem voce gostaria de ver o Hp")

        if name == "1":
            print(pers1["Hp"])

        elif name == "2":
            print(pers2["Hp"])

        elif name == "3":
            print(pers3["Hp"])

        else:
            print("Digite uma opcao valida")
            break

elif modo == "2":
    while True:

     print("Personagens do Jogo")
     print("1 - Jake")
     print("2 - Mai")
     print("3 - lila")
     deci = input("Qual personagem voce gostaria de ver os status")

     if deci == "1":
        print(pers1)

     elif deci == "2":
        print(pers2)

     elif deci == "3":
        print(pers3)

     else:
        print("Digite uma opcao valida")
        break