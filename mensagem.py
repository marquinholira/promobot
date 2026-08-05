def gerar_mensagem(lista):

    texto = "🔥 CUPONS DO MERCADO LIVRE\n\n"

    for item in lista:

        texto += f"🟢 {item['titulo']}\n"

        if item["cupom"]:

            texto += f"Código: {item['cupom']}\n"

        texto += "\n"

    texto += "🛒 Em breve seu link de afiliado ficará aqui."

    return texto
