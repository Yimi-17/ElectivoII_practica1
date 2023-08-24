import pandas as pd
data = pd.read_csv("archivo_1.csv", delimiter=",")

#Describir o mostramos un resumen el archivo 
#print(data.describe())

#mostramos la suma de los ingresos
#suma_total=data['ingresos'].sum()
#print("La suma total es:",suma_total)

#mostramos la el promedio de la edad
#promedio_edad=data['edad'].mean()
#print("Promedio de edad:",promedio_edad)

#filtrar por ciudad, ejemplo "Juliaca"
#trabajadores_juliaca=data[data['ciudad']=='Juliaca']
#print(trabajadores_juliaca)

#conteo de trabajadores por ciudad
#cantidades=data['ciudad'].value_counts()
#print(cantidades)


# Calcular el promedio de ingresos para cada ciudad
#promedios_por_ciudad = data.groupby('ciudad')['ingresos'].mean()
#print("Promedio de ingresos por ciudad:", promedios_por_ciudad)


# Encontrar la persona más joven
#indice_persona_mas_joven = archivo_1['edad'].idxmin()
#persona_mas_joven = archivo_1.loc[indice_persona_mas_joven]
#print("Persona más joven:")
#print(persona_mas_joven)

# Encontrar la persona más mayor
#indice_persona_mas_mayor = archivo_1['edad'].idxmax()
#persona_mas_mayor = archivo_1.loc[indice_persona_mas_mayor]
#print("\nPersona más mayor:")
#print(persona_mas_mayor)




#mostramos el promedio de la edad por ciudad 
promedio_edad_ciudad=data.groupby('ciudad')['edad'].mean()
print("Promedio de edad:",promedio_edad_ciudad)

#mostramos el promedio ingresos por ciudad superiores a 3000 por ciudad 
promedio_ingresos_ciudad = data.groupby('ciudad')['ingresos'].mean()
# Filtrar las ciudades con ingresos promedio superiores a 3000
ciudades_superiores_3000 = promedio_ingresos_ciudad[promedio_ingresos_ciudad > 3000]
print("Ciudades con ingresos promedio superiores a 3000:", ciudades_superiores_3000)

# Ordenar las ciudades según sus ingresos de forma descendente
ciudades_ordenadas = data.sort_values(by='ingresos', ascending=False)
print("Ciudades ordenadas según sus ingresos de forma descendente:", print(ciudades_ordenadas[['ciudad', 'ingresos']]))


# Agregar una columna de impuestos (11% del ingreso)
data['impuestos'] = data['ingresos'] * 0.11
# Mostrar el DataFrame con la nueva columna
print(data)

