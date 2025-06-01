import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + "!@#$%&*"
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerar_senha(tamanho_senha)
print(f"Sua senha gerada é: {nova_senha}")