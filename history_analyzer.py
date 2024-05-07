import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("history_month.csv")

# Criar colunas de data e hora
df['datetime_entry'] = pd.to_datetime(df['date'] + ' ' + df['time'])

# Ordenar por data e hora de entrada
df = df.sort_values(by=['datetime_entry'])

# Calcular tempo de acesso (assumindo que a próxima entrada é a saída)
df['time_spent'] = df['datetime_entry'].diff()

# Remover a primeira linha, que não possui tempo de acesso
df = df.iloc[1:]

# Agrupar por URL e somar o tempo de acesso
grouped_df = df.groupby('url')['time_spent'].sum().reset_index()

# Converter o tempo total para segundos
grouped_df['time_spent_seconds'] = grouped_df['time_spent'].dt.total_seconds()

# Ordenar por tempo total de acesso
grouped_df = grouped_df.sort_values(by=['time_spent_seconds'], ascending=False)

# Selecionar os 10 sites com maior tempo de acesso
top_10_sites = grouped_df.head(10)

# Exibir resultados
print(top_10_sites[['url', 'time_spent_seconds']])