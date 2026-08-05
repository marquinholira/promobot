from fontes import buscar_promocoes
from filtro import filtrar
from mensagem import gerar_mensagem
from salvar import salvar_texto

def main():

    print("PROMOBOT")

    promocoes = buscar_promocoes()

    promocoes = filtrar(promocoes)

    mensagem = gerar_mensagem(promocoes)

    salvar_texto(mensagem)

    print(mensagem)

if __name__ == "__main__":
    main()
