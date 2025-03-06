alfabeto = 'abcdefhijklmnopqrstuv' #Se crea un alfabeto

dic1 = set() # Se usa un conjunto para evitar duplicados automáticamente en el diccionario

archivos_entrada = ['texto.txt']# Lista de archivos a leer

# Procesar cada archivo
for archivo in archivos_entrada:
    try:
        with open(archivo, 'r', encoding='utf-8') as arch: #abre los archivos de entrada
            for renglon in arch: # evalúa cada renglón de cada archivo
                renglon = renglon.lower() # convierte a minúsculas a mayúsculas
                datos = renglon.split()
            for palabra in datos:
                # Limpiar palabra eliminando caracteres no alfabéticos
                palabra_limpia = ''.join([letra for letra in palabra if letra in alfabeto])

                if palabra_limpia: # Agrega palabras a nuestro diccionario
                    dic1.add(palabra_limpia)
    except FileNotFoundError: #Excepción si no se encuentra archivo de entrada
        print(f"El archivo '{archivo}' no se encontró y será omitido.")

# Ordena palabras alfabéticamente
palabras_ordenadas = sorted(dic1)

# Guarda las palabras únicas y ordenadas en el archivo de salida
with open('Diccionario.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(palabras_ordenadas))

# Imprime el número total de palabras guardadas
print(f"Se guardaron {len(palabras_ordenadas)} palabras únicas en el archivo 'Diccionario.txt'.")