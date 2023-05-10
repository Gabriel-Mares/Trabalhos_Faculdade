# Abrindo o arquivo e lendo as linhas
with open('ArquivoDadosProjeto.csv') as f:
    lines = f.readlines()

# Criando um dicionário para acumular o volume de chuva por mês/ano
acumulado_chuva = {}

# Percorrendo cada linha do arquivo
for line in lines[1:]:
    # Dividindo a linha em colunas
    data, precip, _, _, _, _, _, _ = line.split(';')
    # Extraindo o ano e o mês da data
    _, mes, ano = data.split('/')
    # Acumulando o volume de chuva no dicionário
    key = f'{mes}/{ano}'
    acumulado_chuva[key] = acumulado_chuva.get(key, 0) + float(precip)

# Encontrando o mês/ano com o maior volume de chuva
mes_ano_mais_chuvoso = max(acumulado_chuva, key=acumulado_chuva.get)

print(mes_ano_mais_chuvoso)
