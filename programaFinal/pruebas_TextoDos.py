# Para este segundo texto, se hizo un análisis en base a los histogramas, y se intuyo que estaba en inglés, por ello desciframos con  ayuda de nuestro diccionario

# Cargamos el diccionario en inglés 
def carga_dic(nombre):
    archivo = open(nombre, 'r')
    renglon = archivo.read()
    archivo.close()
    palabras = renglon.split()
    print(len(palabras), 'palabras leidas')
    return palabras

diccionario = carga_dic("DiccionarioIngles.txt")


# Realizamos la lectura del texto a descifrar
def carga_cifrado(texto):
    archivo = open(texto, 'r')
    renglon = archivo.readline()
    archivo.close()
    return renglon

# Creamos el diccionario que realizara la sustitución en base a las pruebas realizadas
sustitucion= {
     'a':'h', 'b':'s', 'c':'a', 'd':'r', 'e':'f', 'f':'l', 'g':'c', 'h':'p', 'i':'b', 'j':'m', 'k':'y', 'l':'v', 'M':'I', 'm':'i', 'n':'e', 'o':'d', 'q':'q', 'r':'w', 's':'o', 't':'x', 'u':'t', 'w':'u', 'x':'g', 'y':'k', 'z':'n'
}

texto= carga_cifrado('textoDos.txt')
descifrar=''
for c in texto:
    if c in sustitucion:
        descifrar += sustitucion [c]
    else: 
        descifrar += c
print(descifrar)


# prueba con mzamimumsz
""" cont=0
for p in diccionario:
    if len(p) == 10:
            if p[0] == p[3] == p[5] == p[7] and p[1] == p[9]:
                    cont+=1
                    print(p)
print()
print(cont)
# prueba con bmuwcumszb
cont=0
for p in diccionario:
    if len(p) == 10:
            if p[0] == p[9] and p[1] == p[6] and p[2] == p[5]:
                    cont+=1
                    print(p)
print()
print(cont)
# prueba con bwggnbbewf
cont=0
for p in diccionario:
    if len(p) == 10:
            if p[0] == p[5] == p[6] and p[2] == p[3]:
                    cont+=1
                    print(p)
print()
print(cont)
# prueba con hnu
cont=0
for p in diccionario:
    if len(p) == 3:
            if p[0] != p[1] != p[2]:
                    if p[1] == 'e' and p[2] == 't':
                        cont+=1
                        print(p)
print()
print(cont)
# prueba con gsjhfnt
cont=0
for p in diccionario:
    if len(p) == 7:
            if p[0] != p[1] != p[2] != p[3] != p[4] != p[5] != p[6]:
                    if p[0] == 'c' and p[1] == 'o' and p[4] == 'l' and p[5] == 'e':    
                        cont+=1
                        print(p)
print()
print(cont)
# prueba con usock
cont=0
for p in diccionario:
    if len(p) == 5:
            if p[0] != p[1] != p[2] != p[3] != p[4]:
                    if p[0] == 't' and p[1] == 'o' and p[2] == 'd' and p[3] == 'a':    
                        cont+=1
                        print(p)
print()
print(cont)
# prueba con hcgy
cont=0
for p in diccionario:
    if len(p) == 4:
            if p[0] != p[1] != p[2] != p[3]:
                    if p[0] == 'p' and p[1] == 'a' and p[2] == 'c':    
                        cont+=1
                        print(p)
print()
print(cont)
# prueba con onlnfshmzx
cont=0
for p in diccionario:
    if len(p) == 10:
            if p[1] == p[3]:
                    if p[0] == 'd' and p[1] == 'e' and p[4] == 'l' and p[5] == 'o' and p[6] == 'p' and p[7] == 'i' and p[8] == 'n':    
                        cont+=1
                        print(p)
print()
print(cont)
# prueba con onlnfshmzx
cont=0
for p in diccionario:
    if len(p) == 10:
            if p[1] == p[3]:
                    if p[0] == 'd' and p[1] == 'e' and p[4] == 'l' and p[5] == 'o' and p[6] == 'p' and p[7] == 'i' and p[8] == 'n':    
                        cont+=1
                        print(p)
print()
print(cont)"""
# prueba con qwcdundb
""" cont=0
for p in diccionario:
    if len(p) == 8:
            if p[1] == 'u' and p[2] == 'a' and p[3] == 'r' and p[4] == 't' and p[5] == 'e' and p[6] == 'r' and p[7] == 's':    
                cont+=1
                print(p)
print()
print(cont)  """