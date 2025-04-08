# MVP Pós-Graduação PUC-Rio em Ciência de Dados e Analytics

**Aluno:** Flávio Antonio Oliveira da Silva  
**Plataforma:** Databricks Community Edition  
**Tecnologia:** PySpark

## 📘 Descrição do Projeto

Este projeto é um MVP (Minimum Viable Product) desenvolvido como parte da pós-graduação em Ciência de Dados e Analytics da PUC-Rio. O objetivo é analisar o desempenho de estudantes com base em dados educacionais públicos, avaliando a influência de fatores como curso preparatório, gênero e grupo étnico.

## 🎯 Objetivos

- Criar um pipeline de dados na nuvem utilizando a plataforma Databricks;
- Analisar a qualidade dos dados educacionais;
- Extrair insights a partir de análises exploratórias;
- Documentar todas as etapas do processo em um repositório GitHub.

## 🧩 Dataset

O dataset utilizado está disponível publicamente no Kaggle e contém:
- Gênero, grupo étnico, nível educacional dos pais;
- Tipo de lanche, curso preparatório;
- Notas em matemática, leitura e escrita.

Nome do arquivo: `StudentsPerformance.csv`

## ⚙️ Pipeline

1. **Coleta:** Upload do CSV no Databricks (via DBFS)
2. **Leitura:** Carregamento com `spark.read`
3. **Transformação:** Criação da coluna `nota_media`
4. **Qualidade:** Verificação de nulos e estatísticas
5. **Análises:**
   - Curso preparatório x desempenho
   - Gênero x desempenho
   - Grupo étnico x desempenho

## 💡 Principais Resultados

- Alunos que fizeram curso preparatório obtiveram melhor média.
- Diferença observada entre gêneros.
- O grupo étnico E teve a maior média geral, o grupo A a menor.

## 📂 Estrutura do Repositório

```
📦 mvp-puc-rio
├── 📄 README.md
├── 📄 mvp_pipeline_flavio.py
├── 📄 MVP_PUC_Rio_Ciencia_Dados_Relatorio.pdf
├── 📁 dados/ (opcional para CSV original)
```

## 🚀 Como Executar

1. Faça upload do arquivo `StudentsPerformance.csv` no Databricks (pasta `/FileStore/`)
2. Importe o notebook ou cole o código do arquivo `.py`
3. Execute as células com o cluster ativo
4. Visualize os resultados diretamente no Databricks

## 📝 Licença

Uso educacional - projeto acadêmico sem fins comerciais.
