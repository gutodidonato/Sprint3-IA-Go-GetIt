
# Previsão de Preço Básica Simulada

Este projeto é uma API desenvolvida em Python para realizar previsões de preço com base em dados como preço normal, aprovação e custo de produção. O objetivo é simular um modelo de previsão de preço utilizando Machine Learning.




## Stack utilizada

**Back-end:** Python 


## Instalação

Instale utilizando o organizador de pacotes pip 

```bash
    pip install -r requirements.txt
```
    

## Utilização

```bash
    python -m uvicorn main:app --reload
```



## Documentação da API

#### Este endpoint recebe informações sobre um produto, como o preço normal, avaliação do produto e custo de produção, e retorna uma previsão do preço com base nessas entradas, aplicando regras de negócio e um modelo de Machine Learning.


```http
  POST /prever_preco/
```


envie um json desta maneira:

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `preco_normal` | `float` | **Obrigatório**. preço normal do produto |
| `aprovacao` | `float` | **Obrigatório**. avaliação na plataforma |
| `custo_producao` | `float` | **Obrigatório**. custo para confecção do produto |

#### Retorno:

```json
{
  "preco_previsto": 51.0
}
```

