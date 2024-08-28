# Criando uma lista
minha_lista = ["Felipe", "Charles", "Ester", "Pedro"]

# Acessando elementos da lista
primeiro_elemento = minha_lista[0]
segundo_elemento = minha_lista[1]

# Modificando elementos da lista
minha_lista[2] = "Michelle"

# Adicionando elementos à lista
minha_lista.append("Lucas")

# Removendo elementos da lista
minha_lista.remove("Charles")

# Verificando o tamanho da lista
tamanho_da_lista = len(minha_lista)

# Iterando sobre os elementos da lista
for elemento in minha_lista:
    print(elemento)

# minha_lista.append("Saulo")
# len(minha_lista)

# Função para adicionar um elemento ao final da lista
def append_element(array, x):
    array.append(x)
    return array

# Função para adicionar elementos de um iterável ao final da lista
def extend_array(array, iterable):
    array.extend(iterable)
    return array

# Função para inserir um elemento na posição i da lista
def insert_element(array, i, x):
    array.insert(i, x)
    return array

# Função para remover a primeira ocorrência de um elemento da lista
def remove_element(array, x):
    array.remove(x)
    return array

# Função para remover e retornar o elemento na posição i da lista
def pop_element(array, i=None):
    if i is None:
        return array.pop()  # Remove e retorna o último elemento
    else:
        return array.pop(i)  # Remove e retorna o elemento na posição i

# Função para retornar o índice da primeira ocorrência de um elemento na lista
def index_of_element(array, x):
    return array.index(x)

# Função para contar o número de ocorrências de um elemento na lista
def count_element(array, x):
    return array.count(x)

# Função para ordenar os elementos da lista em ordem crescente
def sort_array(array):
    array.sort()
    return array

# Função para inverter a ordem dos elementos na lista
def reverse_array(array):
    array.reverse()
    return array

# Função para remover todos os elementos da lista
def clear_array(array):
    array.clear()
    return array

# Testando as funções

# Lista inicial
array = [3, 1, 4, 1, 5, 9, 2]

print("Lista inicial:", array)

print("Após append(6):", append_element(array, 6))
print("Após extend([7, 8, 9]):", extend_array(array, [7, 8, 9]))
print("Após insert(3, 10):", insert_element(array, 3, 10))
print("Após remove(1):", remove_element(array, 1))
print("Elemento removido com pop():", pop_element(array))
print("Elemento removido com pop(2):", pop_element(array, 2))
print("Índice de 5:", index_of_element(array, 5))
print("Número de ocorrências de 9:", count_element(array, 9))
print("Após sort():", sort_array(array))
print("Após reverse():", reverse_array(array))
print("Após clear():", clear_array(array))
