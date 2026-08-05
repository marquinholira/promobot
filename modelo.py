from dataclasses import dataclass

@dataclass
class Promocao:

    loja: str

    titulo: str

    preco: float

    preco_antigo: float

    desconto: int

    cupom: str

    cashback: str

    categoria: str

    link: str

    imagem: str
