# Importación de las clases Equipo y operaciones
from modelo.mi_modelo import Equipo
from modelo.mi_modelo import Operaciones
# Importación de los metodos para trabajar los archivos
from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
# Creación de 2 objetos tipo archivo
m = MiArchivo()
m2 = MiArchivoEscribir() # objeto para escribir el archivo
# Obtenemos información del texto
lista = m.obtener_informacion()
# Eliminamos el caracter | con split
lista = [l.split("|") for l in lista]
# Creación de lista de equipos
lista_equipos =[]
# For para recorrer la lista, y agregar cada objeto en lista de equipos
for d in lista:
    eq = Equipo(d[0], d[1], d[2], d[3])
    lista_equipos.append(eq)

#Presentación
print("TRABAJO EN CLASE")
# Ingreso de la opción para presentar una forma de ordenacion
opcion = input("- Elija el número de acuerdo al tipo de ordenación que usted desee:"
               "\n\t1.Por nombre\n\t2.Por campeonatoss\n")
# Condicional if con opcion 1 para ordenar por nombre
if opcion == "1":
    # Recorremos la lista buscando los nombres
    lista = [e.obtener_nombre() for e in lista_equipos]
    # Ordenamos de acuerdo a los nombres por orden alfabetico
    operacion = Operaciones(lista_equipos)
    # Creación de una segunda lista donde agregamos la lista ordenada
    lista_2 = []
    lista_2 = operacion.ordenar_nombre()
# Condicional if con opcion 2 para ordenar por campeonatos
elif opcion == "2":
    # Recorremos la lista buscando los campeonatos
    lista = [e.obtener_campeonatos() for e in lista_equipos]
    # Ordenamos de acuerdo a los campeonatos de menor a mayor
    operacion = Operaciones(lista_equipos)
    # Creación de una segunda lista donde agregamos la lista ordenada
    lista_2 = []
    lista_2 = operacion.ordenar_campeonatos()

print("NOMBRE\tCIUDAD\tCAMPEONATOS\tJUGADORES")
# Recorremos la lista 2
for l in lista_2:
    # Agregamos la lista ordenada en el nuevo archivo
    m2.agregar_informacion(l)
    print(l)
# Cerramos los archivos
m.cerrar_archivo()
m2.cerrar_archivo()


