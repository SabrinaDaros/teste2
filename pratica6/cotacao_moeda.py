import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        par = f"{moeda}BRL"
        cotacao = dados[par]
        return f"""
        Moeda: {moeda} para BRL
        Valor: R$ {float(cotacao['bid']):.2f}
        Máxima: R$ {float(cotacao['high']):.2f}
        Mínima: R$ {float(cotacao['low']):.2f}
        Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
        """
    except requests.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    except KeyError:
        return f"Moeda não suportada ou não encontrada."
    
def main():
    moeda = input("Digite o código da moeda para cotação (ex. USD, EUR, GBP): ").upper()
    print("\nObtendo sua cotação...\n")
    resultado = obter_cotacao(moeda)
    print(resultado)

if __name__ == "__main__":
    main()
       
