import pandas as pd

dados = {
    'Nome': ['Alice', 'Bruno', 'Carlos'],
    'Idade': ['25', '35', '18'],
    'Cidade': ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte']
}

df = pd.DataFrame(dados)
print(df)