def is_palindromo(texto):

    texto_limpo = ''.join(char.lower()
                          for char  in texto
                          if char.isalnum())
    
    return texto_limpo == texto_limpo[::-1]


expressao = input("Insira a expressão para verificação do palíndromo: ")
resultado = is_palindromo(expressao)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"A expressão {expressao} é um palíndromo? {resposta}")