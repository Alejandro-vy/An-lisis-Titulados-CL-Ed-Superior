# 📊 Análisis Exploratorio de Datos (EDA) - Titulados en Chile

# Contexto

Como sabemos en Chile el crecimiento de personas que estan entrando a la educacion superior ha aumentado considerablemente

## 📚 Descripción del Proyecto
Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre los titulados de educación superior en Chile.  
El objetivo principal es analizar tendencias y patrones en la titulación, respondiendo preguntas clave como:
- ¿Qué carreras tienen mayor cantidad de titulados?
- ¿Qué tipo de instituciones generan más titulados?
- ¿A qué edad promedio se titula una persona?
- ¿Cuál es el porcentaje de alumnos que terminan la carrera en la duración teórica?
- ¿Quién saca más profesionales: la Región Metropolitana o las regiones?

## 📂 Estructura del Proyecto
```
📁 EDA_Titulados_Chile/  
 ├── 📄 README.md  *(Descripción del proyecto)*  
 ├── 📄 requirements.txt  *(Dependencias necesarias)*  
 ├── 📁 data/  *(Archivos de datos crudos y procesados)*  
 │   ├── titulados_chile.csv  
 │   └── titulados_limpios.csv  
 ├── 📁 notebooks/  *(Códigos y análisis en Jupyter Notebook)*  
 │   ├── 01_EDA_Titulados.ipynb  
 │   └── 02_Visualizaciones.ipynb  
 ├── 📁 src/  *(Scripts de procesamiento y análisis de datos)*  
 │   ├── limpieza_datos.py  
 │   └── analisis_estadistico.py  
 ├── 📁 reports/  *(Resultados y gráficos generados)*  
 │   ├── resumen_EDA.html  
 │   └── visualizaciones.png  
```

## 📊 Datos Utilizados
- **Fuente:** [Nombre de la fuente de datos]  
- **Descripción:** Los datos contienen información sobre titulados en educación superior en Chile.  
- **Principales variables:**  
  - `carrera`: Nombre de la carrera.  
  - `tipo_institucion`: Universidad, Instituto, CFT.  
  - `region`: Región donde se tituló.  
  - `edad_titulacion`: Edad al momento de titularse.  
  - `duracion_real`: Duración real de los estudios.  
  - `duracion_teorica`: Duración teórica de la carrera.  

## 🛠️ Instalación y Configuración
Para ejecutar el análisis en tu máquina, sigue estos pasos:

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tuusuario/EDA_Titulados_Chile.git
cd EDA_Titulados_Chile
```

### 2️⃣ Instalar dependencias
Asegúrate de tener **Python 3.8+** instalado y ejecuta:
```bash
pip install -r requirements.txt
```

### 3️⃣ Ejecutar los notebooks
Abre Jupyter Notebook y ejecuta los análisis:
```bash
jupyter notebook
```

## 📈 Resultados Clave
🔹 **La carrera con más titulados:** Ingeniería Comercial.  
🔹 **La edad promedio de titulación:** 25 años.  
🔹 **El porcentaje de alumnos que terminan en la duración teórica:** 60%.  
🔹 **Región con más titulados:** Región Metropolitana.  

## 🖼️ Visualizaciones
![Ejemplo de gráfico](reports/visualizaciones.png)

## 📄 Licencia
Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---
📧 **Contacto:** Para consultas, escribe a `janoverayagi@gmail.com`
