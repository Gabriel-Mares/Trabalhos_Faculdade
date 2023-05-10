x = 0
while x <= 3:
    print('Digite a funcionalidade que deseja:')
    print('1- leitura do arquivo, organizando em tuplas e exibindo a lista com todos os dados.')
    print('2- Visualização de precipitação apartir do mes e ano informado pelo usuário.')
    print('3- Visualização da temperatura máxima dos primeiros 7 dias de cada mês de um ano informado pelo usuário.')
    print('4- Encerrar programa.')
    x = int(input())

    if x == 1:
        print('1- leitura do arquivo, organizando em tuplas e exibindo a lista com todos os dados.')

        # 1-leitura do arquivo, organizando em tuplas e exibindo a lista com todos os dados.
        arquivo = open("ArquivoDadosProjeto.csv", "r")
        for linha in arquivo:
            valores = linha.split(';')
            print(linha)
        arquivo.close()

    if x == 2:
        print('2- Visualização de precipitação apartir do mes e ano informado pelo usuário.')

        # 2 Visualização de precipitação apartir do mes e ano informado pelo usuário.
        mes = input("Digite o mês (MM): ")
        ano = input("Digite o ano (AAAA): ")

        # Abre o arquivo de dados de precipitação
        arquivo = open("ArquivoDadosProjeto.csv", "r")

        # Ignora a primeira linha (títulos das colunas)
        next(arquivo)

        # Loop para ler as linhas do arquivo
        for linha in arquivo:
            # Separa os campos da linha
            campos = linha.split(";")

            # Extrai a data e a precipitação
            data = campos[0]
            precipitacao = float(campos[1])

            # Verifica se a data está dentro do período de interesse
            if data[3:5] == mes and data[6:10] == ano:
                # Imprime a data e a precipitação
                print(data + ": " + str(precipitacao))

        # Fecha o arquivo
        arquivo.close()

    if x == 3:
        print('3- Visualização da temperatura máxima dos primeiros 7 dias de cada mês de um ano informado pelo usuário.')
        # 3-Visualização de dados de temperatura dos primeiros 7 dias de cada mês de um ano informado pelo usuário.
        # Abrir o arquivo de dados de temperatura
        arquivo = open("ArquivoDadosProjeto.csv", "r")

        # Pedir ao usuário para inserir o ano de interesse
        ano = input("Digite o ano (AAAA): ")

        # Ignorar a primeira linha do arquivo, que contém os títulos das colunas
        next(arquivo)

        # Criar uma lista vazia para armazenar as temperaturas máximas dos primeiros 7 dias de cada mês
        temperaturas = [None] * 12

        # Criar um loop para ler cada linha do arquivo
        for linha in arquivo:
            # Separar os campos de cada linha usando o separador ";"
            campos = linha.split(";")

            # Extrair a data e a temperatura máxima de cada linha
            data = campos[0]
            tempMax = float(campos[2])

            # Verificar se a data corresponde aos primeiros 7 dias de cada mês e ao ano de interesse inserido pelo usuário
            if (int(data[0:2]) <= 7) and data[6:10] == ano:
                mes = int(data[3:5])

                if temperaturas[mes - 1] is None or tempMax > temperaturas[mes - 1]:
                    temperaturas[mes - 1] = tempMax

        # Depois de ler todo o arquivo, exibir a temperatura máxima correspondente a cada mês
        for mes in range(1, 13):
            print(f"Temperatura máxima nos 7 primeros dias de {mes:02d}/{ano}: {temperaturas[mes - 1]:.2f}")

        # Fechar o arquivo após terminar de utilizá-lo
        arquivo.close()

