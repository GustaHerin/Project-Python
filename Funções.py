# def serve para definir uma função no python.
# O def pode ter retorno e pode nao ter.

def funcao(n1, n2, n3):
    return (n1 + n2) / n3

while True:
    print("Notas do alunos!!!")
    nome = input("Nome do aluno: ")
    n1 = float(input("Nota 1?: "))
    n2 =  float(input("Nota 2?: "))
    n3 = float(input("Qual bimestre o aluno estar?: "))

    resul = funcao(n1, n2, n3)

    print("O" ,nome, "ficou com " ,resul, "de media geral.")

    sair = input("Deseja continuar (s/n)?: ")
    if sair == "n":
        break