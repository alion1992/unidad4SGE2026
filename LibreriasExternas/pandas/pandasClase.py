import pandas as pd


data = {'Nombre': ['Ana', 'Luis', 'Juan'],
        'Edad': [23, 21, 17],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla'],
        'Nacionalidad': ['Española', 'Española', 'Española']}


dataframe = pd.DataFrame(data)
print(dataframe)
print("-------------")
print(dataframe[dataframe['Edad'] > 18])
print("-------------")

'''dataFrame2 = dataframe[dataframe['Edad'] > 18]
print(dataFrame2)'''
print("-------------")
print(dataframe.tail(1)) #head
print("-------------")
print(dataframe.iloc[0:33])
print(dataframe.loc[0])
print(dataframe['Edad'] + 10)
dataframe['Direccion '] = dataframe['Ciudad'] + " " + dataframe['Nacionalidad']
print(dataframe)