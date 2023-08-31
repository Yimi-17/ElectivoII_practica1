import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("homework/archivo_2.csv", delimiter=";", encoding="ISO-8859-1")

# Crear una tabla de contingencia para el análisis
tabla_contingencia = pd.crosstab(data['estado_civil'], data['nivel_educativo'])

# Crear un gráfico de barras apilado
ax = tabla_contingencia.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Relación entre Estado Civil y Niveles de Educación')
plt.xlabel('Estado Civil')
plt.ylabel('Cantidad')
plt.xticks(rotation=0)
plt.legend(title='Nivel Educativo', bbox_to_anchor=(1, 1))
plt.show()