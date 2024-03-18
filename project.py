#APRESENTAÇÃO
print("Bem-vindo ao sistema CalculaDesconto do Leandro Geroto Soares - 2405080")
print("")
print("Nas compras entre R$ 2.500,00 e R$ 5.999,99 o desconto será de 4%.")
print("Nas compras entre R$ 6.000,00 e R$ 9.999,99 o desconto será de 7%.")
print("E nas compras a partir de R$ 10.000,00 o desconto será de 11%.")
print("")

#INCLUINDO INPUTS PARA ENTRADA DOS VALORES
valorUnitario = float(input("Digite o valor unitário do produto: "))
quantidadeProduto = float(input("Digite a quantidade do produto: "))

totalSemDesconto = valorUnitario*quantidadeProduto

#LÓGICA DO CALCULO DO DESCONTO
if totalSemDesconto < 2500.00:
    desconto = 0
elif totalSemDesconto < 6000.00:
    desconto = 0.04
elif totalSemDesconto < 10000.00:
    desconto = 0.07
else:
    desconto = 0.11

#APLICANDO DESCONTO
valorDesconto = totalSemDesconto * desconto
totalComDesconto = totalSemDesconto - valorDesconto

#INCLUINDO SAÍDA DO CÁLCULO DOS VALORES
print("O valor sem desconto foi R$", totalSemDesconto)
print("O valor com desconto foi R$", totalComDesconto, "(desconto", desconto * 100, "%)")
