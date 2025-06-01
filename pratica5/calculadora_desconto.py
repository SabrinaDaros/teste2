def calculadora_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final




preco_original = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite o percentual de desconto: "))

preco_com_desconto = calculadora_desconto(preco_original, desconto)

print(f"O preço final com {desconto} % de desconto é: R$ {preco_com_desconto:.2f}.")