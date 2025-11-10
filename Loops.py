# (while) Loop que executa ações enquanto a condição for verdadeira.

# (for) Loop que percorre sequências, repetindo ações para cada elemento.

print("1- While (Enquanto verdadeiro)\n")
print("2- While (Contador definido)\n")
print("3- for\n")
desicao = input("Escolha um loop para demostração?: ")

if desicao == "1":
    while True:
     print("00")

#--------------------------------------

elif desicao == "2":
    final = 1
    while final <=10:
        print("5")

        final = final +1

#--------------------------------------

elif desicao == "3":
     for x in range(5):
         print("0")
