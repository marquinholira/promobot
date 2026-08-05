from fontes.exemplo import buscar

promocoes = buscar()

for p in promocoes:

    print("---------------------------")

    print("Loja:", p.loja)

    print("Produto:", p.titulo)

    print("Preço:", p.preco)

    print("Desconto:", p.desconto, "%")

    print("Cupom:", p.cupom)
