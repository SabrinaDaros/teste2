import json

def ler_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r' encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_json(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
        except FileNotFoundError