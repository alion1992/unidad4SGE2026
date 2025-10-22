'''
Instalar pandas(es una libreria externa por lo que tendremos que instalarla mediante pip install pandas
'''

import pandas as pd




data = {'Nombre': ['Ana', 'Luis', 'Juan'],
        'Edad': [23, 21, 22],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}
df = pd.DataFrame(data)
print(df)
print(df['Nombre'])
print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[0:22])
print("Elemento")
print(df.iloc[0, 0])

print(df.loc[0, 'Nombre'])
print(df.describe()) #me gusta mucho
print(df.info())
print(df['Edad']+10)


mayores_21 = df[df['Edad'] > 21]
print(mayores_21)


df1 = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])

print(df1)
df_limpiarNulos = df1.dropna()
print(df_limpiarNulos)