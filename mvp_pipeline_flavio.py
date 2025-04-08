
# MVP Pós-Graduação PUC-Rio em Ciência de Dados e Analytics
# Aluno: Flávio Antonio Oliveira da Silva

# ==========================================
# 1. Leitura do CSV no Databricks
# ==========================================

file_path = "dbfs:/FileStore/StudentsPerformance.csv"

df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load(file_path)

df.show(5)
df.printSchema()

# ==========================================
# 2. Criação da coluna nota_media e ETL
# ==========================================

from pyspark.sql.functions import col, round, count, when, avg

# Criar nova coluna com média das três notas
df_transformado = df.withColumn("nota_media", round(
    (col("math score") + col("reading score") + col("writing score")) / 3, 2))

# Verificar valores nulos por coluna
df_transformado.select([
    count(when(col(c).isNull(), c)).alias(c + "_nulos")
    for c in df_transformado.columns
]).show()

# Salvar como arquivo Parquet (formato otimizado)
output_path = "dbfs:/FileStore/StudentsPerformance_Transformado.parquet"
df_transformado.write.mode("overwrite").parquet(output_path)

# Registrar a tabela temporária para consultas SQL
df_transformado.createOrReplaceTempView("alunos_transformado")

# ==========================================
# 3. Análise da qualidade dos dados
# ==========================================

# Estatísticas descritivas básicas
df_transformado.select(
    "math score", "reading score", "writing score", "nota_media"
).describe().show()

# ==========================================
# 4. Análises Exploratórias
# ==========================================

# 4.1 Desempenho por curso preparatório
df_transformado.groupBy("test preparation course") \
    .agg(round(avg("nota_media"), 2).alias("media_geral")) \
    .orderBy("media_geral", ascending=False) \
    .show()

# 4.2 Desempenho por gênero
df_transformado.groupBy("gender") \
    .agg(round(avg("nota_media"), 2).alias("media_geral")) \
    .orderBy("gender") \
    .show()

# 4.3 Desempenho por grupo étnico
df_transformado.groupBy("race/ethnicity") \
    .agg(round(avg("nota_media"), 2).alias("media_geral")) \
    .orderBy("media_geral", ascending=False) \
    .show()
