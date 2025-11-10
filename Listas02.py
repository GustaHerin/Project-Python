### 🟣 1. `append(item)`
#👉 Adiciona um item no final da lista.

frutas = ["maçã", "banana"]
frutas.append("uva")
print(frutas)
# Saída: ['maçã', 'banana', 'uva']
#🧠 **Explicação:** ele sempre coloca o item novo **no final** da lista.

print("----------------------------------\n")


### 🟣 2. `insert(posição, item)`
#👉 Adiciona o item em uma **posição específica**.

frutas = ["maçã", "banana", "uva"]
frutas.insert(1, "laranja")
print(frutas)
# Saída: ['maçã', 'laranja', 'banana', 'uva']
#🧠 **Explicação:** o número indica a posição (começando do zero).

print("----------------------------------\n")

### 🟣 3. `pop()`
#👉 Remove e retorna **o último item**.

frutas = ["maçã", "banana", "uva"]
removido = frutas.pop()
print(frutas)
print("Removido:", removido)
# Saída:
# ['maçã', 'banana']
# Removido: uva
#🧠 **Explicação:** útil pra tirar o último elemento da lista.

print("----------------------------------\n")

### 🟣 4. `pop(posição)`
#👉 Remove e retorna o item de uma **posição específica**.

frutas = ["maçã", "banana", "uva"]
removido = frutas.pop(1)
print(frutas)
print("Removido:", removido)
# Saída:
# ['maçã', 'uva']
# Removido: banana
#🧠 **Explicação:** o índice define **qual** item vai sair.

print("----------------------------------\n")

### 🟣 5. `sort()`
#👉 Ordena a lista em **ordem crescente**.

numeros = [5, 2, 9, 1]
numeros.sort()
print(numeros)
# Saída: [1, 2, 5, 9]
#🧠 **Explicação:** organiza a lista (funciona com números ou palavras).

print("----------------------------------\n")

### 🟣 6. `reverse()`
#👉 Inverte a **ordem atual** da lista.

numeros = [1, 2, 3, 4]
numeros.reverse()
print(numeros)
# Saída: [4, 3, 2, 1]
#🧠 **Explicação:** apenas inverte, não organiza.

print("----------------------------------\n")

### 🟣 7. `index(item)`
#👉 Retorna a **posição do item** na lista.

frutas = ["maçã", "banana", "uva"]
pos = frutas.index("banana")
print("A posição da banana é:", pos)
# Saída: A posição da banana é: 1
#🧠 **Explicação:** útil pra saber **onde** está um elemento.

print("----------------------------------\n")

### 🟣 8. `count(item)`
#👉 Conta **quantas vezes** um item aparece.

frutas = ["maçã", "banana", "uva", "banana"]
qtd = frutas.count("banana")
print("Bananas:", qtd)
# Saída: Bananas: 2
#🧠 **Explicação:** perfeito pra contagem de elementos repetidos.

print("----------------------------------\n")

### 🟣 9. `remove(item)`
#👉 Remove **a primeira ocorrência** do item.

frutas = ["maçã", "banana", "uva", "banana"]
frutas.remove("banana")
print(frutas)
# Saída: ['maçã', 'uva', 'banana']
