# %% [markdown]
# # Análisis Exploratio (EDA)

# %% [markdown]
# Preguntas objetivos:
# 
# - ¿Qué carreras tienen mayor cantidad de titulados?
# - ¿Qué tipo de instituciones generan más titulados?
# - A que edad promedio se titula una persona de la educación superior? ### no está la cat edad
# - Cual es el porcentaje de alumnos que terminan la carrera en la duración teórica?
# - Quién saca más profesionales la RM o regiones?
# 

# %%
import pandas as pd

####### Análisis exploratorio de datos #######

### Cargar el dataset ###

titulados_2023= pd.read_excel('C:/Users/janov/Desktop/Datasets/Titulados-Ed-Superior-2023/2023.xlsx')

#Imprime las primeras 5 filas
#print(titulados_2023_Cl.head(5))

print(titulados_2023.info())

# %%
# Seleccionar solo las columnas necesarias
columnas_utiles = ["codigo_unico","mrun","gen_alu","fec_nac_alu", "cat_periodo", "anio_ing_carr_act", "nomb_titulo_obtenido", "nomb_carrera", "tipo_inst_1",
                   "dur_total_carr", "dur_estudio_carr", "region_sede", "gen_alu"]

# Filtrar las columnas que existen en el dataframe
columnas_existentes = [col for col in columnas_utiles if col in titulados_2023.columns]

titulados_2023 = titulados_2023[columnas_existentes]

# Contar filas con 'fec_nac_alu' igual a 19000101
#registros_sin_fecha_nac = titulados_2023[titulados_2023['fec_nac_alu'] == 19000101].shape[0]
#print(f"Registros sin información de fecha de nacimiento: {registros_sin_fecha_nac}") ------> 0

from datetime import datetime

# Convertir la columna 'fec_nac_alu' a formato de fecha
titulados_2023['fec_nac_alu'] = pd.to_datetime(titulados_2023['fec_nac_alu'], format='%Y%m')

# Calcular la edad
titulados_2023['edad'] = titulados_2023['fec_nac_alu'].apply(lambda x: datetime.now().year - x.year - ((datetime.now().month, datetime.now().day) < (x.month, x.day)))


# Verificar cambios
print(titulados_2023.info())





# %% [markdown]
# # Inspección inicial de los datos

# %%
print(titulados_2023.shape)  # Número de filas y columnas

print("###########################")
print(titulados_2023.info())  # Tipo de datos de cada columna

# %% [markdown]
# # Manejo de nulos

# %%
print(titulados_2023.isnull().sum())  # Cantidad de valores nulos


# %%
titulados_2023['nomb_titulo_obtenido'] = titulados_2023['nomb_titulo_obtenido'].fillna('sin informacion')
titulados_2023['mrun'] = titulados_2023['mrun'].fillna(-1)

# Verificar cambios
print(titulados_2023.isnull().sum())


# %% [markdown]
# # Manejo de duplicados

# %%
total_filas = titulados_2023.shape[0]  # Total de filas
duplicados = titulados_2023.duplicated().sum()  # Filas duplicadas

print(f"Total de filas: {total_filas}")
print(f"Filas duplicadas encontradas: {duplicados}")

duplicados = titulados_2023[titulados_2023.duplicated(keep=False)]  # Obtener todas las filas duplicadas


# Eliminar duplicados y mantener solo el primer registro
titulados_2023 = titulados_2023.drop_duplicates()

# Verificar cambios
print(f"Total de filas después de eliminar duplicados: {titulados_2023.shape[0]}")











# %% [markdown]
# # Comprobar Dataset post-limpieza

# %%
print(titulados_2023.info())  # Confirmar que no hay valores nulos y tipos de datos correctos
print(titulados_2023.describe())  # Resumen estadístico de las variables numéricas
#print(titulados_2023.head())  # Vista previa del dataset


# %% [markdown]
# # Análisis Preguntas objetivos

# %% [markdown]
# # ¿Qué carreras tienen mayor cantidad de titulados?

# %%
import matplotlib.pyplot as plt
import seaborn as sns

top_carreras = titulados_2023["nomb_carrera"].value_counts().head(10)

plt.figure(figsize=(12, 6))
ax = sns.barplot(x=top_carreras.values, y=top_carreras.index, hue=top_carreras.index, palette="Blues_d", dodge=False, legend=False)
plt.xlabel("Cantidad de Titulados")
plt.ylabel("Carrera")
plt.title("Top 10 Carreras con Más Titulados en 2023")

# Agregar etiquetas en las barras
for i in ax.containers:
    ax.bar_label(i, fmt='%d')

plt.show()


# %% [markdown]
# # ¿Qué tipo de instituciones generan más titulados?

# %%
# Reemplazar valores en la columna 'tipo_inst_1'
titulados_2023['tipo_inst_1'] = titulados_2023['tipo_inst_1'].replace('Centros de FormaciÃ³n TÃ©cnica', 'Centros de Formación Técnica')



tipo_inst = titulados_2023["tipo_inst_1"].value_counts()

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=tipo_inst.values, y=tipo_inst.index, palette="Blues_d", hue=tipo_inst.index, legend=False)
plt.xlabel("Cantidad de Titulados")
plt.ylabel("Tipo de Institución")
plt.title("Cantidad de Titulados por Tipo de Institución en 2023")

# Agregar etiquetas en las barras
for i in ax.containers:
    ax.bar_label(i, fmt='%d')

plt.show()


# %% [markdown]
# # ¿A qué edad promedio se titula una persona de la educación superior?

# %%
edad_promedio = titulados_2023["edad"].mean()
print(f"Edad promedio de titulación: {edad_promedio:.2f} años")

plt.figure(figsize=(8, 5))
sns.histplot(titulados_2023["edad"], bins=30, kde=True, color="blue")
plt.xlabel("Edad")
plt.ylabel("Cantidad de Titulados")
plt.title("Distribución de Edad al Titularse")
plt.xlim(18, 80)  # Acotar el rango del eje x
plt.show()


# %% [markdown]
# #  ¿Quién saca más profesionales: RM o regiones?

# %%
# Agrupar las regiones en "Metropolitana" y "Regiones"
titulados_agrupados = titulados_2023["region_sede"].apply(lambda x: "Metropolitana" if x == "Metropolitana" else "Regiones").value_counts()

plt.figure(figsize=(8, 5))
ax = sns.barplot(x=titulados_agrupados.values, y=titulados_agrupados.index, palette="Blues_d", hue=titulados_agrupados.index, legend=False)
plt.xlabel("Cantidad de Titulados")
plt.ylabel("Región")
plt.title("Cantidad de Titulados por Región en 2023")
plt.xlim(0, 180000)  # Acotar el rango del eje x

# Agregar etiquetas en las barras
for i in ax.containers:
    ax.bar_label(i, fmt='%d')

plt.show()



