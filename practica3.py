import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("archivo_1.csv", delimiter=",")

# Contar el número de trabajadores por ciudad
trabajadores_por_ciudad = data['ciudad'].value_counts()

# Crear un gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(trabajadores_por_ciudad, labels=trabajadores_por_ciudad.index, autopct='%1.1f%%', startangle=140, shadow=True)
plt.title('Número de Trabajadores por Ciudad')
plt.axis('equal')  # Hace que el gráfico de pastel sea circular
plt.show()