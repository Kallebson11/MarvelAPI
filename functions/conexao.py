import requests
import time
import hashlib
from decouple import config
import pandas as pd
import json
from datetime import datetime

# O valor da variável 'pubk' e 'pvk' estão armazenadas em outro arquivo
# A lib 'decouple' criptografa o valor de cada uma, protegendo-as
pubk = config('pubk')
pvk = config('pvk')

# Função que recebe a URL e o nome do arquivo como parâmetro
def requisicao_heroes(URL=None):
    
    timestamp_atual = str(time.time())
    
    md5_hash = hashlib.md5()
    md5_hash.update(bytes(timestamp_atual, 'utf-8'))
    md5_hash.update(bytes(pvk, 'utf-8'))
    md5_hash.update(bytes(pubk, 'utf-8'))
    md5 = md5_hash.hexdigest()
    
    if URL is None:
        URL = f"https://gateway.marvel.com/v1/public/characters?apikey={pubk}&hash={md5}&ts={timestamp_atual}&limit=1"
    
    try:
        # Faz a requisição da API e armazena em uma variável
        dados = requests.get(URL).json()
        
    # Tratamento de erros 
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except json.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        
    return dados
