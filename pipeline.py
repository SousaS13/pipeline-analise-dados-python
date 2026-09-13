# ==============================================================================
# PROJETO: Pipeline de Extração, Tratamento e Análise de Dados
# AUTORA: Thaynara Sousa Nascimento
# OBJETIVO: Simular higienização e tratamento de dados institucionais (ETL)
# ==============================================================================

# IMPORTAÇÃO: Avisa ao Python que utilizaremos o Pandas para manipulação de 
# tabelas estruturadas (DataFrames) e o NumPy para tratar valores nulos (NaN).
import pandas as pd
import numpy as np

def executar_pipeline():
    print("--- Iniciando o processo de ETL (Extração, Transformação e Carga) ---")
    
    # 1. SIMULAÇÃO DE EXTRAÇÃO (DADOS BRUTOS)
    # Criando uma estrutura inicial com inconsistências comuns do dia a dia,
    # como registros duplicados e dados ausentes, simulando o Diário Oficial.
    dados_brutos = {
        'id_servidor':,
        'nome': ['Carlos Silva', 'Ana Souza', np.nan, 'Carlos Silva', 'Mariana Costa', 'João Santos'],
        'ato_administrativo': ['Nomeação', 'Exoneração', 'Aposentadoria', 'Nomeação', np.nan, 'Licença'],
        'data_publicacao': ['2026-01-10', '2026-01-11', '2026-01-11', '2026-01-10', '2026-01-12', '2026-01-13']
    }
    
    # pd.DataFrame: Transforma o dicionário comum em uma tabela estruturada.
    df = pd.DataFrame(dados_brutos)
    print("\n[INFO] Base de dados bruta carregada:")
    print(df)

    # 2. SIMULAÇÃO DE TRANSFORMAÇÃO (TRATAMENTO E HIGIENIZAÇÃO)
    print("\n--- Iniciando Tratamento de Dados com Pandas ---")
    
    # drop_duplicates(): Remove linhas idênticas. No setor público, isso evita 
    # que o mesmo ato administrativo seja processado ou contabilizado duas vezes.
    total_antes = len(df)
    df = df.drop_duplicates()
    print(f"[SUCESSO] Linhas duplicadas removidas. Total anterior: {total_antes} | Atual: {len(df)}")
    
    # fillna(): Trata valores nulos. Dados vazios quebram relatórios; preenchemos
    # campos ausentes com termos padrão para garantir a integridade da análise.
    df['nome'] = df['nome'].fillna('Não Identificado')
    df['ato_administrativo'] = df['ato_administrativo'].fillna('Ato Não Informado')
    print("[SUCESSO] Tratamento de valores nulos concluído com preenchimento padrão.")
    
    # str.upper(): Padroniza strings em letras maiúsculas. Evita que buscas e 
    # queries falhem por diferença de digitação (ex: 'nomeação' vs 'NOMEAÇÃO').
    df['ato_administrativo'] = df['ato_administrativo'].str.upper()
    print("[SUCESSO] Textos de atos administrativos padronizados em caixa alta.")

    # 3. RESULTADO DA ANÁLISE EXPLORATÓRIA
    print("\n[INFO] Base de dados limpa e pronta para relatórios / carga em SQL:")
    print(df)
    
    # value_counts(): Faz a contagem agregada de ocorrências. Simula um relatório 
    # gerencial automático para o MGI monitorar o volume de movimentações de pessoal.
    print("\n--- Relatório Gerencial: Contagem de Atos por Tipo ---")
    print(df['ato_administrativo'].value_counts())

if __name__ == "__main__":
    executar_pipeline()
