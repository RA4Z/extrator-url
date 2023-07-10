#url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

url = ' '

# SANITIZAÇÃO DA URL
url = url.strip()

# VALIDAÇÃO DA URL
if url == '':
    raise ValueError('A URL está vazia!')

# SEPARA BASE E OS PARÂMETROS
indice_interrogacao = url.find('?')
url_base = url[0:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

# BUSCA O VALOR DE UM PARÂMETRO
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

# ESCREVE OS DADOS NO TERMINAL
print('\n-------------\n')
print(valor.title())
print('\n-------------\n')
