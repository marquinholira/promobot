from app.navegador import abrir_pagina, fechar


def buscar():

    playwright, navegador, pagina = abrir_pagina(
        "https://www.pelando.com.br"
    )

    print("Título da página:")
    print(pagina.title())

    print("\nPrimeiros links encontrados:\n")

    links = pagina.locator("a")

    quantidade = min(20, links.count())

    for i in range(quantidade):

        texto = links.nth(i).inner_text().strip()

        if texto:

            print(texto)

    fechar(playwright, navegador)

    return []
