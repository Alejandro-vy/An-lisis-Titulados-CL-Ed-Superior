import pandas as pd

####### Análisis exploratorio de datos #######

### Cargar el dataset ###

titulados_2023_Cl = pd.read_excel('C:/Users/janov/Desktop/Datasets/Titulados-Ed-Superior-2023/2023.xlsx')


#Imprime las primeras 5 filas
print(titulados_2023_Cl.head(5))

### Inspección inicial de los datos ###


print(titulados_2023_Cl.shape)  # Número de filas y columnas
#print(titulados_2023_Cl.info())  # Tipo de datos de cada columna
print(titulados_2023_Cl.isnull().sum())  # Cantidad de valores nulos
print(titulados_2023_Cl.duplicated().sum())  # Registros duplicados




titulados_2023_Cl["FEC_NAC_ALU"] = pd.to_datetime(titulados_2023_Cl["FEC_NAC_ALU"], format='%Y%m%d', errors='coerce')
titulados_2023_Cl["FECHA_OBTENCION_TITULO"] = pd.to_datetime(titulados_2023_Cl["FECHA_OBTENCION_TITULO"], format='%Y%m%d', errors='coerce')

# Eliminar valores sin información
titulados_2023_Cl = titulados_2023_Cl[titulados_2023_Cl["FEC_NAC_ALU"] > "1900-01-01"]



