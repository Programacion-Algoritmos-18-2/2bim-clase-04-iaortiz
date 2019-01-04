from modelo.mi_modelo import Equipo
from modelo.mi_modelo import Operaciones
from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir

m = MiArchivo()
m2 = MiArchivoEscribir() # objeto para escribir el archivo
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]
lista_equipos =[]
for d in lista:
    eq = Equipo(d[0], d[1], d[2], d[3])
    lista_equipos.append(eq)

print(lista_equipos)
print("TRABAJO EN CLASE")
opcion = input("- Elija el número de acuerdo al tipo de ordenación que usted desee:"
               "\n\t1.Por nombre\n\t2.Por campeonatoss\n")
if opcion == "1":
    lista = [e.obtener_nombre() for e in lista_equipos]
    operacion = Operaciones(lista_equipos)
    lista_2 = []
    lista_2 = operacion.ordenar_nombre()
elif opcion == "2":
    lista = [e.obtener_campeonatos() for e in lista_equipos]
    operacion = Operaciones(lista_equipos)
    lista_2 = []
    lista_2 = operacion.ordenar_campeonatos()

print("NOMBRE\tCIUDAD\tCAMPEONATOS\tJUGADORES")
for l in lista_2:
    m2.agregar_informacion(l)
    print(l)

m.cerrar_archivo()
m2.cerrar_archivo()
#lista.sort()
#print(lista)

