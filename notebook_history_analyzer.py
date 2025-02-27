# -*- coding: utf-8 -*-
"""Análise de tempo de navegação com base no histórico de acessos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ugDg24m7So08C7kGnMAH7MbtU3lF-b_p

# Analise de histórico de acesso
O arquivo history_month.csv parece conter um registro de histórico de navegação na web, possivelmente exportado de um navegador como o Google Chrome. Vamos analisar as colunas e tentar entender o que elas representam:
Colunas:
order: Um número sequencial que indica a ordem cronológica das visitas.
id: Um identificador único para cada entrada do histórico.
date: A data da visita.
time: A hora da visita.
title: O título da página visitada.
url: O URL da página visitada.
visitCount: O número de vezes que a página foi visitada.
typedCount: O número de vezes que o URL foi digitado manualmente.
transition: O tipo de transição que levou à visita (ex: link, typed, auto_bookmark).

# Passo 1: Importar bibliotecas e carregar dados
"""

import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv("history_month.csv")

"""# Passo 2: Calcular tempo de acesso

Como o arquivo não possui uma coluna com o tempo de acesso, precisaremos calcular a diferença entre a hora de entrada e saída de cada site.

"""

# Criar colunas de data e hora
df['datetime_entry'] = pd.to_datetime(df['date'] + ' ' + df['time'])

# Ordenar por data e hora de entrada
df = df.sort_values(by=['datetime_entry'])

# Calcular tempo de acesso (assumindo que a próxima entrada é a saída)
df['time_spent'] = df['datetime_entry'].diff()

# Remover a primeira linha, que não possui tempo de acesso
df = df.iloc[1:]

"""# Passo 3: Agrupar por URL e calcular tempo total

"""

# Agrupar por URL e somar o tempo de acesso
grouped_df = df.groupby('url')['time_spent'].sum().reset_index()

# Converter o tempo total para segundos
grouped_df['time_spent_seconds'] = grouped_df['time_spent'].dt.total_seconds()

# Ordenar por tempo total de acesso
grouped_df = grouped_df.sort_values(by=['time_spent_seconds'], ascending=False)

"""# Passo 4: Selecionar os 10 sites mais visitados"""

# Selecionar os 10 sites com maior tempo de acesso
top_10_sites = grouped_df.head(10)

# Exibir resultados
print(top_10_sites[['url', 'time_spent_seconds']])

