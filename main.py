from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


#=================================================== Estipulando Preço Previsto
df = pd.read_excel("predicao.xlsx")
df["Preço Previsto"] = df["Preço Normal"] * df["Aprovação"]
df["Preço Previsto"] = np.where(
    df["Preço Previsto"] < df["Custo Produção"],
    df["Custo Produção"] + 2,
    df["Preço Previsto"]
)


#=================================================== TREINO 
X = df[["Preço Normal", "Aprovação", "Custo Produção"]]
y = df["Preço Previsto"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)


#==================================================================
#=================================================== FASTAPI 
app = FastAPI()


class PrevisaoInput(BaseModel):
    preco_normal: float
    aprovacao: float
    custo_producao: float


@app.post("/prever_preco/")
def prever_preco(dados: PrevisaoInput):
    entrada = np.array([[dados.preco_normal, dados.aprovacao, dados.custo_producao]])
    preco_previsto = model.predict(entrada)[0]
    if preco_previsto < dados.custo_producao:
        preco_previsto = dados.custo_producao + 2
    
    return {"preco_previsto": preco_previsto}

@app.get("/")
def home():
    return {"mensagem": "API de previsão de preços está no ar!"}
