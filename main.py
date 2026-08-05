from app.navegador import abrir_pagina, fechar


def main():

    playwright, navegador, pagina = abrir_pagina(
        "https://www.google.com"
    )

    print(pagina.title())

    fechar(playwright, navegador)


if __name__ == "__main__":
    main()
