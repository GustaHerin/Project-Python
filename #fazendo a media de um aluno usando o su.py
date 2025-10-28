#fazendo a media de um aluno usando o sum e o len
#sum e usado para somar valores em uma lista
#len e usado para contar quantos valores tem em uma lista

nome = input("Digite o nome do aluno: ")

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: ")) 
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))     

soma = sum([n1, n2, n3, n4]) / len([n1, n2, n3, n4])
 
print("A média do aluno", nome, "é: ", soma)

if soma >= 7:
    print("O aluno está aprovado!")

elif soma >= 5 and soma < 7:
    print("O aluno está de recuperação!")

else:
    print("O aluno está reprovado!")