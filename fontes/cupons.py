from modelo import Cupom

def buscar():

    return [

        Cupom(
            codigo="MELI50",
            descricao="R$50 OFF acima de R$300",
            validade="05/08/2026",
            origem="Mercado Livre"
        ),

        Cupom(
            codigo="ELETRONICOS10",
            descricao="10% OFF em eletrônicos",
            validade="05/08/2026",
            origem="Mercado Livre"
        )

    ]
