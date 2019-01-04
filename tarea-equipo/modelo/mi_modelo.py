class Equipo(object):
    # Constructor
    def __init__(self, nom, ciu, camp, nj):
        # Declaración de variables
        self.nombre = nom
        self.ciudad = ciu
        self.campeonatos = int(camp)
        self.num_jugadores = int(nj)

    # Métodos get y set para cada atributo
    def agregar_nombre (self , n):
        self.nombre = n
    def obtener_nombre (self):
        return self.nombre
    def agregar_ciudad (self , a):
        self.ciudad = a
    def obtener_ciudad(self):
        return self.ciudad
    def agregar_campeonatos (self, cp):
        self.campeonatos = int(cp)
    def obtener_campeonatos (self):
        return self.campeonatos
    def agregar_num_jugadores (self, nju):
        self.num_jugadores = int(nju)
    def obtener_num_jugadores (self):
        return self.num_jugadores

    # Método str para presentar
    def __str__(self):
        return "%s - %s - %d - %d " % (self.nombre, self.ciudad,\
                self.campeonatos, self.num_jugadores)
    def __repr__(self):
        return "%s - %s - %d - %d " % (self.nombre, self.ciudad, \
                                         self.campeonatos, self.num_jugadores)

class Operaciones(object):

    def __init__(self, listado):
        self.listado_equipos = listado

    def ordenar_nombre(self):
        return sorted(self.listado_equipos, key=lambda Equipo: Equipo.obtener_nombre())
    def ordenar_campeonatos(self):
        return sorted(self.listado_equipos, key=lambda Equipo: Equipo.obtener_campeonatos())