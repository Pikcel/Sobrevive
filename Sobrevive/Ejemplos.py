'''
#INCISO A
def lee(archivo):
    lectura = open(archivo,"r")
    for x in range(10):
        print(lectura.readline())
    lectura.close()
nombre=input("Escribe el nombre de tu archivo con extensión .txt: ")
lee(nombre)
'''

'''
#INCISO B
#Esto es un ejemplo
#xD
lineas = []
palabras = []
n = 1
nombre = input("¿Cómo se llama tu archivo? Escribe con extensión .txt: ")
lectura = open(nombre,"r")
for line in lectura:
    lineas.append(line)
lectura.close()
nombre = input("¿Cómo se llamará tu nuevo archivo? Escribe con extensión .txt: ")
escritura = open(nombre,"w")
for x in range(len(lineas)):
    palabras = lineas[x]
    palabras = palabras.split(' ')
    for y in range(len(palabras)):
        escritura.write(" "+str(n)+": "+palabras[y])
        n+=1
escritura.close()
'''

'''
#INCISO C
lineas = []
codigo = []
def leer():
    nombre = input("¿Cómo se llama tu archivo? Escribe con extensión .txt: ")
    lectura = open(nombre,"r")
    for line in lectura:
        lineas.append(line)
    lectura.close()
def escribir():
    code = ''
    nombre = input("¿Cómo se llamará tu nuevo archivo? Escribe con extensión .txt: ")
    escritura = open(nombre,"w")
    for x in range(len(lineas)):
        comentarios = lineas[x]
        comentarios = list(comentarios)
        if "#" not in comentarios:
            for x in comentarios:
                code += x
    codigo.append(str(code))
    for y in range(len(codigo)):
        escritura.write(codigo[y])
    escritura.close()
leer()
escribir()
'''