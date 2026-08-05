from fontes.mercadolivre import buscar as buscar_ml


def buscar_promocoes():

    promocoes = []

    promocoes.extend(buscar_ml())

    return promocoes
