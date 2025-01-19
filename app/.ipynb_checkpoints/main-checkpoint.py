from fastapi import FastAPI, Query
from app.scraping import get_producao_scraping, get_processamento_scraping, get_comercializacao_scraping, get_importacao_scraping, get_exportacao_scraping
from app.database import inserir_dados_no_banco, executar_consulta_sql

app = FastAPI(
    title="API Viticultura Embrapa",
    description="Consulta os dados de produção, processamento e comercialização de vinhos",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da Embrapa!"}

# Rota para dados de Produção
@app.get("/scraping_producao")
def get_producao():
    try:
        data = get_producao_scraping()  # Chama a função de scraping
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Rota para dados de Processamento
@app.get("/scraping_processamento")
def get_processamento():
    try:
        data = get_processamento_scraping()  # Chama a função de scraping
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Rota para dados de Processamento
@app.get("/scraping_comercializacao")
def get_comercializacao():
    try:
        data = get_comercializacao_scraping()  # Chama a função de scraping
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Rota para dados de Processamento
@app.get("/scraping_importacao")
def get_comercializacao():
    try:
        data = get_importacao_scraping()  # Chama a função de scraping
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Rota para dados de Processamento
@app.get("/scraping_exportacao")
def get_comercializacao():
    try:
        data = get_exportacao_scraping()  # Chama a função de scraping
        return {"status": "success", "data": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}


# Rota para carregar dados no banco de dados
@app.post("/carregar_dados")
def carregar_dados():
    try:
        result = inserir_dados_no_banco()  # Chama a função de inserção no banco
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Rota para consultar dados
@app.get("/consultar_dados")
def consultar_dados(
    tabela: str,
    coluna: str = Query(None, description="Nome da coluna para filtrar os dados"),
    valor: str = Query(None, description="Valor para filtrar os dados")
):
    """
    Endpoint para consultar dados do banco SQLite.
    Parâmetros:
    - tabela: Nome da tabela no banco de dados.
    - coluna: Coluna a ser filtrada (opcional).
    - valor: Valor para filtrar os dados na coluna (opcional).
    """
    try:
        # Constrói a query SQL
        if coluna and valor:
            query = f"SELECT * FROM {tabela} WHERE {coluna} = ?"
            parametros = (valor,)
        else:
            query = f"SELECT * FROM {tabela}"
            parametros = ()

        # Executa a consulta
        dados = executar_consulta_sql(query, parametros)

        # Retorna os resultados
        return {"status": "success", "data": dados}
    except Exception as e:
        return {"status": "error", "message": str(e)}
