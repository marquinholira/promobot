from fontes import buscar_promocoes
from filtro import filtrar
from mensagem import gerar_mensagem

def main():
    print("===================================")
    print("       PROMOBOT BRASIL")
    print("===================================")

    promocoes = buscar_promocoes()

    promocoes = filtrar(promocoes)

    mensagem = gerar_mensagem(promocoes)

    print(mensagem)

if __name__ == "__main__":
    main()
