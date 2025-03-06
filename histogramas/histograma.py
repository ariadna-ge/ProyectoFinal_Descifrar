import matplotlib.pyplot as plt
alfabeto = 'abcdefghijklmnopqrstuvwxyz' # Definir el alfabeto

# Inicializar el diccionario de frecuencias
histo1 = {}
for c in alfabeto:
    histo1[c] = 0

# Leer el archivo de texto, el nombre se modifica de acuerdo a como se nombraron los archivos
archivo = open('textoDos.txt', 'r')
cad = archivo.read()
archivo.close()

# Contar las ocurrencias de cada letra en el texto
for c in cad:
    if c in alfabeto:
        histo1[c] += 1

# Ordenar el diccionario por valores de mayor a menor
histo1_ordenado = dict(sorted(histo1.items(), key=lambda item: item[1], reverse=True))

# Guardar los resultados en un archivo CSV, el nombre del archivo se modifica para que no se repita
archivo = open('salidaDos.csv', 'w')
for letra, frecuencia in histo1_ordenado.items():
    archivo.write(letra + ',' + str(frecuencia) + '\n')
archivo.close()

# Graficar los resultados en barras
plt.figure(figsize=(10, 6)) 
plt.bar(histo1_ordenado.keys(), histo1_ordenado.values(), color='#CB9DF0')

plt.title('Frecuencia de letras en el texto', fontsize=16)
plt.xlabel('Letras', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)

plt.xticks(rotation=45)
plt.show()