import os
import sqlite3
import pandas as pd

def inserir_dados_no_banco():
    conn = sqlite3.connect('./test.db')
    try:
        file_path = "~/Downloads/Producao.csv"
        file_path = os.path.expanduser(file_path)

        file_path2 = "~/Downloads/ProcessaViniferas.csv"
        file_path2 = os.path.expanduser(file_path2)
       
        file_path3 = "~/Downloads/Comercio.csv"
        file_path3 = os.path.expanduser(file_path3)

        file_path4 = "~/Downloads/ImpVinhos.csv"
        file_path4 = os.path.expanduser(file_path4)

        file_path5 = "~/Downloads/ExpVinho.csv"
        file_path5 = os.path.expanduser(file_path5)

        ## producao
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        df = pd.read_csv(file_path, sep=';')
        df = df.astype(str)

        df.to_sql('tb_producao', conn, if_exists='replace', index=False)

        ## processamento
        if not os.path.exists(file_path2):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path2}")

        df = pd.read_csv(file_path2, sep=';')
        df = df.astype(str)

        df.to_sql('tb_processamento', conn, if_exists='replace', index=False)

        ## comercializacao
        if not os.path.exists(file_path3):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path3}")

        df = pd.read_csv(file_path3, sep=';')
        df = df.astype(str)

        df.to_sql('tb_comericalizacao', conn, if_exists='replace', index=False)

        ## importacao
        if not os.path.exists(file_path4):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path4}")

        df = pd.read_csv(file_path4, sep=';')
        df = df.astype(str)

        df.to_sql('tb_importacao', conn, if_exists='replace', index=False)

        ## exportacao
        if not os.path.exists(file_path5):
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path5}")

        df = pd.read_csv(file_path5, sep=';')
        df = df.astype(str)

        df.to_sql('tb_importacao', conn, if_exists='replace', index=False)

        
        conn.close()

        return {"status": "success", "message": "Dados inseridos no banco com sucesso"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


def consultar_dados(query="SELECT * FROM dados_vitivinicultura LIMIT 10"):
    try:
        # Conectar ao SQLite
        conn = sqlite3.connect('./test.db')
        
        # Executar a consulta
        df = pd.read_sql_query(query, conn)
        conn.close()

        # Converter o resultado para JSON
        return {"status": "success", "data": df.to_dict(orient="records")}
    except Exception as e:
        return {"status": "error", "message": str(e)}



def executar_consulta_sql(query, parametros=()):
    try:
        conn = sqlite3.connect('./test.db')
        cursor = conn.cursor()

        # Executa a consulta
        cursor.execute(query, parametros)
        colunas = [desc[0] for desc in cursor.description]
        resultados = [dict(zip(colunas, row)) for row in cursor.fetchall()]

        conn.close()
        return resultados
    except sqlite3.Error as e:
        raise Exception(f"Erro ao executar consulta SQL: {e}")

