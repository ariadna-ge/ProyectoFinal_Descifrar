# Para este primer texto, se hizo un análisis en base a los histogramas, y se intuyo que estaba en italiano, por ello desciframos con  ayuda de nuestro diccionario

# Cargamos el diccionario en italiano 

def carga_dic(nombre):
    archivo = open(nombre, 'r')
    renglon = archivo.read()
    archivo.close()
    palabras = renglon.split()
    print(len(palabras), 'palabras leidas')
    return palabras

diccionario = carga_dic("DiccionarioItaliano.txt")

# Realizamos la lectura del texto a descifrar
def carga_cifrado(texto):
    archivo = open(texto, 'r')
    renglon = archivo.readline()
    archivo.close()
    return renglon

# Creamos el diccionario que realizara la sustitución en base a las pruebas realizadas
sustitucion = {'a': 't', 'b': 'v', 'c': 's', 'd': 'o', 'e': 'd', 'E': 'D', 'f': 'u', 'g': 'h', 'h': 'g', 'H': 'G', 'i': 'r', 'j': 'n', 'k': 'e', 'K': 'E', 'l': 'l', 'L': 'L', 'm': 'a', 'M': 'A', 'n': 'q', 'o': 'm', 'p': 'i', 'q': 'c', 'r': 'u', 's': 'z', 't': 'p', 'T': 'P', 'u': 'f', 'v': 'm', 'w': 'h', 'x': 'r', 'y': 'n', 'Y': 'N', 'z': 'b'}

texto= carga_cifrado("histogramas\textosComparar\textoUno.txt")
descifrar=''
for c in texto:
    if c in sustitucion:
        descifrar += sustitucion [c]
    else: 
        descifrar += c
print(descifrar)

# omaxpmxqm = matriarca
""" cont=0
for p in diccionario:
    if len(p) == 9:
            if p[1] == p[5] == p[-1]:
                if p[3] == p[6]:
                    cont+=1
                    print(p)
print()
print(cont) """

# kuukaad = effetto
""" cont=0
for p in diccionario:
    if len(p) == 7:
            if p[0] == p[3] and p[1] == p[2] and p[4] == p[5]:
                    if p[0] != p[-1] and p[0] != 'a' and p[1] != 'c' and p[4] == 't' and p[-1] != 'i' and p[2] != 'p':
                        cont+=1
                        print(p)
print()
print(cont) """

# cdyd
""" cont=0
for p in diccionario:
    if len(p) == 4:
            if p[0] != p[2] and p[1] == p[-1]:
                if p[1] == 'o':
                        cont+=1
                        print(p)
print()
print(cont) """

# ldxd
""" cont=0
for p in diccionario:
    if len(p) == 4:
            if p[1] == p[-1] and p[0] != p[2]:
                if p[1] == 'o' and p[2] == 'r' and p[0] != 't' and p[0] != 'p' and p[0] != 'f':
                    if p[0] != 'b' and p[0] != 'c':
                        cont+=1
                        print(p)
print()
print(cont) """

#tkx
""" cont=0
for p in diccionario:
    if len(p) == 3:
            if p[1] == 'e':
                if p[-1] == 'r':
                        cont+=1
                        print(p)
print()
print(cont) """

#mttmpm
""" cont=0
for p in diccionario:
    if len(p) == 6:
            if p[0]=='a' and p[0] == p[-1] and p[0] == p[3]:
                if p[1] == p[2] and p[4]=='i':
                    cont+=1
                    print(p)
print()
print(cont) """

#myyp = anni
""" cont=0
for p in diccionario:
    if len(p) == 4:
            if p[0] != p[-1] and p[1] == p[2]:
                if p[0] == 'a' and p[-1] == 'i':
                    cont+=1
                    print(p)
print()
print(cont) """

#pl
""" cont=0
for p in diccionario:
    if len(p) == 2:
            if p[0] != p[-1] :
                if p[0] == 'i':
                    cont+=1
                    print(p)
print()
print(cont) """

#ekll = dell
""" cont=0
for p in diccionario:
    if len(p) == 4:
            if p[0] != p[-1] and p[1] != p[-1]:
                if p[1] == 'e' and p[-1] =='l':
                    cont+=1
                    print(p)
print()
print(cont) """

# bpbk = vive
""" cont=0
for p in diccionario:
    if len(p) == 4:
            if p[0] != p[-1] and p[0] == p[2]:
                if p[1]=='i' and p[-1]=='e':
                    cont+=1
                    print(p)
print()
print(cont) """

# txpyqptmlokyak = principalmente
""" cont=0
for p in diccionario:
    if len(p) == 14:
        if p[0] == p[6] and p[2] == p[5]:
            cont+=1
            print(p)
print()
print(cont) """

# qgk = che
""" cont=0
for p in diccionario:
    if len(p) == 3:
        if p[0] != p[1] and p[0]=='c' and p[-1]=='e':
            cont+=1
            print(p)
print()
print(cont) """

#nfmyad = quanto
""" cont=0
for p in diccionario:
    if len(p) == 6:
        if p[0] != p[1] and p[1]=='u' and p[2]=='a':
            if p[3] == 'n' and p[4] == 't' and p[-1]=='o':
                cont+=1
                print(p)
print()
print(cont) """