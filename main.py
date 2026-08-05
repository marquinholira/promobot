from fontes.cupons import buscar
from historico import carregar, salvar
from mensagem import gerar

cupons = buscar()

historico = carregar()

novos = []

for cupom in cupons:

    if cupom.codigo not in historico:

        novos.append(cupom)

        historico.append(cupom.codigo)

salvar(historico)

texto = gerar(novos)

print(texto)

with open("mensagem.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write(texto)
