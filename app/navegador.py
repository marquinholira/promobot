from playwright.sync_api import sync_playwright


def abrir_pagina(url):

    playwright = sync_playwright().start()

    navegador = playwright.chromium.launch(
        headless=True
    )

    pagina = navegador.new_page()

    pagina.goto(
        url,
        wait_until="networkidle"
    )

    return playwright, navegador, pagina


def fechar(playwright, navegador):

    navegador.close()

    playwright.stop()
