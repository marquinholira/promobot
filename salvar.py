def salvar_texto(texto):

    with open("mensagem.txt", "w", encoding="utf-8") as arquivo:

        arquivo.write(texto)
