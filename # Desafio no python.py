# Desafio no python


#  A função input sempre retorna uma string (ex: Gustavo)

nome = input("Digite o nome do aluno: ")

# A função float converte a string em número decimal (ex: 5.5)

n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: ")) 
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))     


media = (n1 + n2 + n3 + n4) / 4

# A função print receber várias variáveis separadas por vírgula.
print("A média do aluno", nome, "é: ", media)

# A função if é (Sim)
if media >= 7:
    print("O aluno está aprovado!")

# A função elif é (Senão se)
elif media <= 5 and media < 7:
    print("O aluno está de recuperação!")

# A função else é (Senão)
else:
    print("O aluno está reprovado!")
