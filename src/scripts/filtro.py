# %%

import polars as pl

import os

# %%

schema = {
    "CNPJ BÁSICO": pl.Utf8,
    "CNPJ ORDEM": pl.Utf8,
    "CNPJ DV": pl.Utf8,
    "IDENTIFICADOR MATRIZ/FILIAL": pl.Utf8,
    "NOME FANTASIA": pl.Utf8,
    "SITUAÇÃO CADASTRAL": pl.Utf8,
    "DATA SITUAÇÃO CADASTRAL": pl.Utf8, 
    "MOTIVO SITUAÇÃO CADASTRAL": pl.Utf8,
    "NOME DA CIDADE NO EXTERIOR": pl.Utf8,
    "PAIS": pl.Utf8,
    "DATA DE INÍCIO ATIVIDADE": pl.Utf8, 
    "CNAE FISCAL PRINCIPAL": pl.Utf8,
    "CNAE FISCAL SECUNDÁRIA": pl.Utf8,
    "TIPO DE LOGRADOURO": pl.Utf8,
    "LOGRADOURO": pl.Utf8,
    "NÚMERO": pl.Utf8,
    "COMPLEMENTO": pl.Utf8,
    "BAIRRO": pl.Utf8,
    "CEP": pl.Utf8,
    "UF": pl.Utf8,
    "MUNICÍPIO": pl.Utf8,
    "DDD 1": pl.Utf8,
    "TELEFONE 1": pl.Utf8,
    "DDD 2": pl.Utf8,
    "TELEFONE 2": pl.Utf8,
    "DDD DO FAX": pl.Utf8,
    "FAX": pl.Utf8,
    "CORREIO ELETRÔNICO": pl.Utf8,
    "SITUAÇÃO ESPECIAL": pl.Utf8,
    "DATA DA SITUAÇÃO ESPECIAL": pl.Utf8  
}

codigo_academia = "9313100" #Código do cnae para Atividades de condicionamento físico

situacao_cadastro = "02"

#%%

df = pl.read_csv("../CNPJ/estabelecimento_9.csv",
    separator = ";",
    encoding = "latin1",
    has_header = False,  
    new_columns = list(schema.keys()),  
    schema_overrides = schema,
    ignore_errors = True)

# %%

#filtro para os itens que contenham o codigo 9313100 e também tenham o cadastro ativo
df_filtrado = df.filter(
    (
    (pl.col("CNAE FISCAL PRINCIPAL") == codigo_academia) |
    (pl.col("CNAE FISCAL SECUNDÁRIA").str.contains(codigo_academia))
    ) &
    (pl.col("SITUAÇÃO CADASTRAL") == situacao_cadastro)
)

# %%

df_filtrado.write_csv("academias_ativas_filtradas_10.csv", separator=";")

# %%

diretorio_filtrados = ""

arquivo_final = ""

# Lista para armazenar os DataFrames filtrados
dataframes_filtrados = []

for i in range(1, 11):
    nome_arquivo = f"academias_ativas_filtradas_{i}.csv"
    caminho_completo = f"{diretorio_filtrados}/{nome_arquivo}"

    if os.path.exists(caminho_completo):
        print(f"Lendo {nome_arquivo}...")
        df = pl.read_csv(caminho_completo, 
        separator=";",
        encoding = "latin1",
        has_header = True,  
        new_columns = list(schema.keys()),  
        schema_overrides = schema,
        ignore_errors = True)
        dataframes_filtrados.append(df)
    else:
        print(f"Arquivo {nome_arquivo} não encontrado.")


if dataframes_filtrados:

    df_final = pl.concat(dataframes_filtrados)


    df_final.write_csv(arquivo_final, separator=";")
    print(f"Arquivo final gerado: {arquivo_final}")
else:
    print("Nenhum dado foi encontrado para unir.")

# %%
