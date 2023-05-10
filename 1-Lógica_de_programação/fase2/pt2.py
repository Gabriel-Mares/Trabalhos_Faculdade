def calcular_media(lista):
    if not lista:
        return 0
    soma = 0
    for valor in lista:
        soma += valor
    media = soma / len(lista)
    return media


def calcular_moda(lista):
    contagem = {}
    for valor in lista:
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
    moda = []
    frequencia_maxima = 0
    for valor, frequencia in contagem.items():
        if frequencia > frequencia_maxima:
            moda = [valor]
            frequencia_maxima = frequencia
        elif frequencia == frequencia_maxima:
            moda.append(valor)
    if len(moda) == len(lista):
        moda = []
    return moda


# leitura do arquivo
arquivo = open('ArquivoDadosProjeto.csv', 'r')
linhas = arquivo.readlines()
arquivo.close()

# separação dos dados em listas
temperaturas_minimas = []
umidades = []
velocidades_vento = []

for linha in linhas[1:]:
    dados = linha.strip().split(';')
    data = dados[0]
    ano = int(data[6:])
    mes = int(data[3:5])
    if mes == 8 and 2006 <= ano <= 2016:
        temperatura_minima = float(dados[3])
        umidade = float(dados[5])
        velocidade_vento = float(dados[6])
        temperaturas_minimas.append(temperatura_minima)
        umidades.append(umidade)
        velocidades_vento.append(velocidade_vento)

# cálculo da média e da moda para cada mês de agosto
for ano in range(2006, 2017):
    print(f"Agosto/{ano}")
    temperaturas_minimas_agosto = []
    umidades_agosto = []
    velocidades_vento_agosto = []
    for linha in linhas[1:]:
        dados = linha.strip().split(';')
        data = dados[0]
        ano_dado = int(data[6:])
        mes = int(data[3:5])
        if mes == 8 and ano_dado == ano:
            temperatura_minima = float(dados[3])
            umidade = float(dados[5])
            velocidade_vento = float(dados[6])
            temperaturas_minimas_agosto.append(temperatura_minima)
            umidades_agosto.append(umidade)
            velocidades_vento_agosto.append(velocidade_vento)

    media_temperaturas = calcular_media(temperaturas_minimas_agosto)
    moda_temperaturas = calcular_moda(temperaturas_minimas_agosto)
    media_umidades = calcular_media(umidades_agosto)
    moda_umidades = calcular_moda(umidades_agosto)
    media_velocidades = calcular_media(velocidades_vento_agosto)
    moda_velocidades = calcular_moda(velocidades_vento_agosto)

    print(f"Média temperatura mínima: {media_temperaturas}")
    print(f"Moda temperatura mínima: {moda_temperaturas}")
    print(f"Média umidade do ar: {media_umidades}")
    print(f"Moda umidade do ar: {moda_umidades}")
    print(f"Média velocidade do vento: {media_velocidades}")
    print(f"Moda velocidade do vento: {moda_velocidades}")
    print("----------------")
