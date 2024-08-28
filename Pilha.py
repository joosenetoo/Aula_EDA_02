class Pilha:
    def __init__(self):
        self.itens = []

    def esta_vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.itens.pop()
        else:
            raise IndexError("A pilha está vazia")

    def topo(self):
        if not self.esta_vazia():
            return self.itens[-1]
        else:
            raise IndexError("A pilha está vazia")

    def tamanho(self):
        return len(self.itens)



# Criar uma pilha
pilha_alunos = Pilha()

# Lista de alunos
alunos = ["Felipe", "Michelle", "Pedro", "Lucas", "Saulo", "Luan", "Fernando"]

# Empilhar os alunos na pilha
for aluno in alunos:
    pilha_alunos.empilhar(aluno)

for aluno in pilha_alunos.itens:
    print(aluno)

# print("Alunos desempilhados da pilha:")
# while not pilha_alunos.esta_vazia():
#     print(pilha_alunos.desempilhar())