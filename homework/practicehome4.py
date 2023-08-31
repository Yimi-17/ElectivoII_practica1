import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("homework/archivo_2.csv", delimiter=";", encoding="ISO-8859-1")

# Crear un diagrama de dispersión
plt.figure(figsize=(10, 6))
colors = {'Universidad': 'blue', 'Técnico': 'green', 'PostGrado': 'red'}
plt.scatter(data['edad'], data['nivel_educativo'], c=data['nivel_educativo'].map(colors))
plt.title('Relación entre Edad y Nivel de Educación')
plt.xlabel('Edad')
plt.ylabel('Nivel de Educación')
plt.yticks(data['nivel_educativo'].unique())  # Etiquetas únicas de nivel educativo
plt.show()