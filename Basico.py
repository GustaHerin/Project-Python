print("int, número inteiro, ex: 10")
print("float, número decimal, ex: 3.14")
print("bool, valor verdadeiro ou falso, ex: True")
print("str, texto, ex: 'Olá Mundo'")
print("list, lista de elementos, ex: [1, 2, 3, 'a']")
print("tuple, tupla (imutável), ex: (1, 2, 3)")
print("set, conjunto (não tem repetição), ex: {1, 2, 3}")
print("dict, dicionário (chave:valor), ex: {'nome':'João', 'idade':25}")
print("type(), mostra o tipo de uma variável, ex: type(10) -> <class 'int'>")
print("len(), mostra o tamanho/quantidade de elementos, ex: len('abc') -> 3")
print("input(), lê algo do usuário como texto")
print("print(), mostra algo na tela")
print("if, usado para executar um bloco de código se a condição for True") # se
print("elif, usado para testar outra condição se a primeira não for True") #senão
print("else, usado para executar um bloco se todas as condições anteriores forem False")

print("----------------------------------\n")

soma = 1 + 1
multiplicacao = 2 * 2
divisao = 3 / 2
divisao_inteira = 3 // 2 # resultado sem casas decimais
subtracao = 1 - 2
potencia = 7 ** 2
modulo = 3 % 2 #resto da divisão

print("----------------------------------\n")

print("5 <= 5:", 5 <= 5)   # menor ou igual
print("5 >= 5:", 5 >= 5)   # maior ou igual
print("5 == 5:", 5 == 5)   # igual
print("5 != 5:", 5 != 5)   # diferente

print("----------------------------------\n")

print("for, usado para repetir um bloco de código um número determinado de vezes")
print("Exemplo: for i in range(5): print(i) -> repete de 0 até 4")
for i in range(5):
    print("Contagem do for:", i)

print("while, usado para repetir um bloco de código enquanto uma condição for verdadeira")
print("Exemplo: contador = 0; while contador < 5: print(contador); contador += 1")
contador = 0
while contador < 5:
    print("Contagem do while:", contador)
    contador += 1

print("break, usado para interromper um laço de repetição antes do fim")
print("Exemplo: for i in range(10): if i == 5: break -> para o loop quando i for 5")
for i in range(10):
    if i == 5:
        print("Chegou no 5, parando o loop com break!")
        break
    print("Número:", i)

print("continue, usado para pular uma iteração e ir direto para a próxima")
print("Exemplo: for i in range(5): if i == 2: continue -> pula o número 2 e continua o loop")
for i in range(5):
    if i == 2:
        print("Pulando o número 2 com continue!")
        continue
    print("Número:", i)

print("----------------------------------\n")
print("Hello World") #Exibi texto

print(10.5+5) #Soma

print("----------------------------------\n")

nome = input("Qual e o seu nome? ")
ida = int(input("Qual sua idade? "))
pes = float(input("Qual seu peso? "))
resul = (int(ida+pes))

print(nome, "sua idade mais o peso dão: ", resul)

print("----------------------------------\n")
print("Ensinando a usar o bool")

senha = input("Digite a senha: ")
if bool(senha):
    print("Você digitou algo!")
else:
    print("Não digitou nada!")

