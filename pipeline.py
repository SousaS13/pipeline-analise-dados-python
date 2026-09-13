# ==============================================================================
# PROJETO: Pipeline de Extração, Tratamento e Análise de Dados
# AUTORA: Thaynara Sousa Nascimento
# OBJETIVO: Simular higienização e tratamento de dados institucionais (ETL)
# ==============================================================================

import pandas as pd
import numpy as np

def executar_pipeline():
    print("--- Iniciando o processo de ETL (Extração, Transformação e Carga) ---")
    
    # 1. SIMULAÇÃO DE EXTRAÇÃO (DADOS BRUTOS)
    # Criando um dicionário com inconsistências comuns (valores nulos e duplicados)
    dados_brutos = {
        'id_servidor':,
        'nome': ['Carlos Silva', 'Ana Souza', np.nan, 'Carlos Silva', 'Mariana Costa', 'João Santos'],
        'ato_administrativo': ['Nomeação', 'Exoneração', 'Aposentadoria', 'Nomeação', np.nan, 'Licença'],
        'data_publicacao': ['2026-01-10', '2026-01-11', '2026-01-11', '2026-01-10', '2026-01-12', '2026-01-13']
    }
    
    # Transformando em um DataFrame do Pandas
    df = pd.DataFrame(dados_brutos)
    print("\n[INFO] Base de dados bruta carregada:")
    print(df)

    # 2. SIMULAÇÃO DE TRANSFORMAÇÃO (TRATAMENTO E HIGIENIZAÇÃO)
    print("\n--- Iniciando Tratamento de Dados com Pandas ---")
    
    # Removendo registros duplicados (Consistência)
    total_antes = len(df)
    df = df.drop_duplicates()
    print(f"[SUCESSO] Linhas duplicadas removidas. Total anterior: {total_antes} | Atual: {len(df)}")
    
    # Tratando valores nulos (Limpeza)
    # Substituindo nomes ausentes por 'Não Identificado' e atos por 'Pendente'
    df['nome'] = df['nome'].fillna('Não Identificado')
    df['ato_administrativo'] = df['ato_administrativo'].fillna('Ato Não Informado')
    print("[SUCESSO] Tratamento de valores nulos concluído com preenchimento padrão.")
    
    # Padronizando textos (Filtro estruturado)
    df['ato_administrativo'] = df['ato_administrativo'].str.upper()
    print("[SUCESSO] Textos de atos administrativos padronizados em caixa alta.")

    # 3. RESULTADO DA ANÁLISE EXPLORATÓRIA
    print("\n[INFO] Base de dados limpa e pronta para relatórios / carga em SQL:")
    print(df)
    
    # Exemplo de consulta/agregação rápida (simulando Queries SQL)
    print("\n--- Relatório Gerencial: Contagem de Atos por Tipo ---")
    print(df['ato_administrativo'].value_counts())

if __name__ == "__main__":
    executar_pipeline()
