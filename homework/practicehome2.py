import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("homework/archivo_2.csv", delimiter=";", encoding="ISO-8859-1")

# Calcular la distribución de niveles de educación en porcentajes
distribucion_niveles = data['nivel_educativo'].value_counts(normalize=True) * 100
print("Los porcentajes son:" ,distribucion_niveles)

# Crear un gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(distribucion_niveles, labels=distribucion_niveles.index, autopct='%1.1f%%', startangle=140, shadow=True)
plt.title('Distribución de Niveles de Educación')
plt.axis('equal')  # Hace que el gráfico de pastel sea circular
plt.show()