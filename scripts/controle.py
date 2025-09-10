import sys
import os
import pyodbc
import pandas as pd
import pyspark.pandas as ps

if '__file__' in globals():
    base_path = os.path.dirname(os.path.dirname(__file__))
else:
    base_path = os.path.join(os.getcwd(), '..')

sys.path.append(base_path)
from functions.function import Conexion


try:
    conexao, cursor = Conexion(database="MarvelAPI")
    print("Conexão bem-sucedida!")
except pyodbc.Error as e:
    print(f"Erro ao conectar: {e}")
    
query = cursor.execute('''
    SELECT
        *
    FROM marvel.Heroes
''')

df = pd.DataFrame(query)
print(df)
