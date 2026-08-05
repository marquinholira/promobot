from config import LINK_AFILIADO

def gerar(cupons):

    texto = "🔥 *CUPONS DO MERCADO LIVRE*\n\n"

    for cupom in cupons:

        texto += f"🎁 {cupom.descricao}\n"

        texto += f"🔑 Código: {cupom.codigo}\n"

        texto += f"📅 Válido até: {cupom.validade}\n\n"

    texto += "━━━━━━━━━━━━━━\n\n"

    texto += "🛒 Compre utilizando meu link:\n"

    texto += LINK_AFILIADO

    texto += "\n\n❤️ Obrigado por apoiar o canal."

    return texto
