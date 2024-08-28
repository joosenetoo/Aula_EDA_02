class Fila:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        else:
            raise IndexError("A fila está vazia")

    def frente(self):
        if not self.esta_vazia():
            return self.itens[0]
        else:
            raise IndexError("A fila está vazia")

    def tamanho(self):
        return len(self.itens)

# Criar uma fila
fila_alunos = Fila()

# Lista de alunos
alunos = ["Felipe", "Michelle", "Pedro", "Lucas", "Saulo", "Luan", "Fernando"]

# Enfileirar os alunos na fila
for aluno in alunos:
    fila_alunos.enfileirar(aluno)

# Desenfileirar e imprimir os alunos até que a fila esteja vazia
print("Alunos desenfileirados da fila:")
while not fila_alunos.esta_vazia():
   print(fila_alunos.desenfileirar())