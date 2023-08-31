import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("homework/archivo_2.csv", delimiter=";", encoding="ISO-8859-1")

# Calcular el promedio de ingresos por género
promedio_ingresos_genero = data.groupby('genero')['ingresos'].mean()
print(promedio_ingresos_genero)

# Crear un gráfico de barras
plt.figure(figsize=(8, 6))
promedio_ingresos_genero.plot(kind='bar', color=['blue', 'pink'])
plt.title('Promedio de Ingresos por Género')
plt.xlabel('Género')
plt.ylabel('Promedio de Ingresos')
plt.xticks(rotation=0)
plt.show()