import pandas as pd
import matplotlib.pyplot as plt

#importacao de arquivo (nome, encoding para Brail, separador, lenguaguem)
arquivo = pd.read_csv('IES_2011.csv', encoding='ISO-8859-1',sep=';', engine='python')
ies = arquivo.iloc[:, 9]
mroies = ies.value_counts()
print(mroies)

mroies2 = pd.Series(mroies.index,index=mroies.values)

plt.figure(figsize=(8,8))
plt.plot(mroies.tolist(),marker='o')
plt.grid()
plt.title('NRO IES POR UF')
plt.xlabel('NRO')
plt.ylabel('UF')
plt.show()
