import matplotlib.pyplot as plt
#from pandasUteis.pandas_utils import frequency_by_natural_order, frequency_by_buckets
import pandas as pd

df = pd.read_csv('/home/alunos/luisMauricio/IA/python/ejer2_1125.csv')

"""
Criando um histograma para com os pesos dos alunos
"""

peso = df['Peso']

plt.figure(figsize=(8, 6))
plt.hist(peso, bins=range(40, 110,10))
plt.title('Distribuicao de Pesos')
plt.xlabel('Peso')
plt.ylabel('Alunos')
#plt.savefig('imagens/peso-histograma.png')
plt.show()
plt.close()
