import csv

import matplotlib.pyplot as plt

# Abrindo o arquivo de dados e lendo as informações
with open('ArquivoDadosProjeto.csv', newline='') as csvfile:
    dados = csv.reader(csvfile, delimiter=';')
    next(dados)  # pula a primeira linha (cabeçalho)
    precipitacoes = {}

    # Calculando a precipitação de cada década
    for linha in dados:
        ano = int(linha[0][-4:])
        precip = float(linha[1])

        decada = (ano - 1961) // 10 + 1
        if decada not in precipitacoes:
            precipitacoes[decada] = {'precipitacao': precip, 'anos': 1, 'anos_decada': [ano]}
        else:
            precipitacoes[decada]['precipitacao'] += precip
            precipitacoes[decada]['anos'] += 1
            precipitacoes[decada]['anos_decada'].append(ano)

    # Imprimindo a média de precipitação por ano de cada década, juntamente com os anos analisados
    for decada, dados in precipitacoes.items():
        media = dados['precipitacao'] / dados['anos']
        anos = dados['anos_decada']
        print(f'Década {decada} ({anos[0]}-{anos[-1]}): {media:.2f} mm/ano')

    # Encontrando a década mais chuvosa
    decada_max = max(precipitacoes, key=lambda d: precipitacoes[d]['precipitacao'] / precipitacoes[d]['anos'])
    anos_decada_max = precipitacoes[decada_max]['anos_decada']
    print(
        f'A década mais chuvosa é a {decada_max} ({anos_decada_max[0]}-{anos_decada_max[-1]}), com média de {precipitacoes[decada_max]["precipitacao"] / precipitacoes[decada_max]["anos"]:.2f} mm/ano')

# Criando listas com as médias de precipitação e anos de cada década
medias = [precipitacoes[d]['precipitacao'] / precipitacoes[d]['anos'] for d in precipitacoes]
anos = [f'{precipitacoes[d]["anos_decada"][0]}-{precipitacoes[d]["anos_decada"][-1]}' for d in precipitacoes]

# Criando o gráfico de barras
fig, ax = plt.subplots()
ax.bar(anos, medias)

# Adicionando título e legendas aos eixos
ax.set_title('Médias de precipitação por década')
ax.set_xlabel('Décadas')
ax.set_ylabel('Precipitação média (mm/ano)')

# Exibindo o gráfico
plt.show()
