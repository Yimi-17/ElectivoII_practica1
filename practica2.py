import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("archivo_1.csv", delimiter=",")

# Crear un histograma de edades
plt.hist(data['edad'], bins=10, edgecolor='black')

# Configurar el título y etiquetas de los ejes
plt.title('Histograma de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')

# Mostrar el histograma
plt.show()