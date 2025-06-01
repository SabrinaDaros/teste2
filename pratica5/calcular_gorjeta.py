def calcular_gorjeta(valor_conta, porcentagem_gorgeta):
    gorgeta = valor_conta * (porcentagem_gorgeta / 100)
    return gorgeta

total_conta = float(input("Insira o valor total da conta: "))
porcentagem = float(input("Insira a porcentagem da gorgeta (%): "))
gorgeta = calcular_gorjeta(total_conta, porcentagem)
print(f"Para uma conta de R$ {total_conta:.2f} a gorgeta de {porcentagem} % é R$ {gorgeta:.2f}")
