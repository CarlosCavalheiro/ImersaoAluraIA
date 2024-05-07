# ImersaoAluraIA
# History-Analyzer

Este repositório contém um script Python que analisa um arquivo CSV de histórico de navegação na web e fornece insights sobre os sites mais visitados e o tempo gasto em cada um.

## Funcionalidades

* Lê um arquivo CSV de histórico de navegação.
* Calcula o tempo gasto em cada site.
* Identifica os 10 sites mais visitados com maior tempo de acesso.
* Exibe os resultados no console.

## Requisitos

* Python 3.x
* Pandas

## Como usar

1. Clone o repositório:

```
git clone https://github.com/CarlosCavalheiro/ImersaoAluraIA/history-analyzer.git

```

Instale as dependências:

```
pip install pandas

```

* Exporte seu histórico de navegação em formato CSV. (Utilize a extesão do Chrome Export Chrome History)
```
https://chromewebstore.google.com/detail/export-chrome-history/dihloblpkeiddiaojbagoecedbfpifdj
```

* Coloque o arquivo CSV na pasta do projeto e renomeie-o para history.csv.
* Execute o script:

```
python history_analyzer.py

```


## Exemplo de arquivo CSV

O script espera um arquivo CSV com o seguinte formato:

```
order,id,date,time,title,url,visitCount,typedCount,transition
1,1234,2024-05-01,10:00:00,"Página Inicial | Google",https://www.google.com/,1,0,typed
2,1235,2024-05-01,10:05:00,"Resultados da pesquisa | Google",https://www.google.com/search?q=python,2,0,link
3,1236,2024-05-01,10:10:00,"Documentação do Python",https://www.python.org/,5,0,link
```

## Observações
* O script assume que a próxima entrada no histórico após uma visita a um site é a saída desse site.
* O tempo gasto em um site pode não ser preciso se o usuário deixar abas abertas por longos períodos.

## Próximos passos
* Adicionar a capacidade de filtrar os dados por usuário.
* Implementar diferentes critérios de ordenação.
* Criar visualizações dos dados, como gráficos de barras e pizza.
* Criar uma interface web para a aplicação.

## Exemplo criado com inspiração na Aula 01 - Imersão de IA Alura
Carlos Cavalheiro
