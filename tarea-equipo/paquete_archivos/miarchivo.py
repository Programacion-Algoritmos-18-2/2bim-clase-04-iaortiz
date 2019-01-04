import codecs
import sys

# sys.path.append('./')
#from .paquete_modelo.mimodelo import Persona

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion.csv", "r")
    # Metodo para leer el archivo
    def obtener_informacion(self):
        return self.archivo.readlines()
    # Método para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/informacion1.csv", "a")
    # Método para agregar la información al archivo vacio
    def agregar_informacion(self, p):
        self.archivo.write("%s - %s - %d - %d " % (p.nombre, p.ciudad,
                                    p.campeonatos, p.num_jugadores))
    # Método para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()
