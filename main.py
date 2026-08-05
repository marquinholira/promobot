from playwright.sync_api import sync_playwright

def main():

    with sync_playwright() as p:

        navegador = p.chromium.launch(
            headless=True
        )

        pagina = navegador.new_page()

        pagina.goto("https://www.google.com")

        print("Título da página:")

        print(pagina.title())

        navegador.close()

if __name__ == "__main__":
    main()
