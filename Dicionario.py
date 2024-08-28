# Criando um dicionário de produtos
catalogo_produtos = {
    "001": {"nome": "Camiseta", "preco": 29.99, "estoque": 100},
    "002": {"nome": "Calça Jeans", "preco": 59.99, "estoque": 50},
    "003": {"nome": "Tênis", "preco": 79.99, "estoque": 30},
    "004": {"nome": "Bermuda", "preco": 39.99, "estoque": 80}
}

# Exibindo informações sobre um produto específico
codigo_produto = "002"
print("Informações sobre o produto", codigo_produto + ":")
print("Nome:", catalogo_produtos[codigo_produto]["nome"])
print("Preço:", catalogo_produtos[codigo_produto]["preco"])
print("Estoque:", catalogo_produtos[codigo_produto]["estoque"])

print("\nAtualizando...")

# Atualizando o estoque de um produto
catalogo_produtos["003"]["estoque"] -= 10

# Adicionando um novo produto ao catálogo
catalogo_produtos["005"] = {"nome": "Jaqueta", "preco": 99.99, "estoque": 20}

# Removendo um produto do catálogo
del catalogo_produtos["004"]

# Exibindo o catálogo atualizado
print("\nCatálogo de produtos atualizado:")
for codigo, produto in catalogo_produtos.items():
    print("Código:", codigo)
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Estoque:", produto["estoque"])
    print()


catalogo_produtos["001"] = {"nome": "Short", "preco": 89.99, "estoque": 10}

# Exibindo informações sobre um produto específico
codigo_produto = "001"
print("Informações sobre o produto", codigo_produto + ":")
print("Nome:", catalogo_produtos[codigo_produto]["nome"])
print("Preço:", catalogo_produtos[codigo_produto]["preco"])
print("Estoque:", catalogo_produtos[codigo_produto]["estoque"])