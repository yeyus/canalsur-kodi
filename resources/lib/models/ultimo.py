class Ultimo(object):
    """ Class for keeping info about latest available programs """
    def __init__(self, url, tapa, nombre, nombre_programa, fecha, id, id_programa):
        self.url = url
        self.tapa = tapa
        self.nombre = nombre
        self.nombre_programa = nombre_programa
        self.fecha = fecha
        self.id = id
        self.id_programa = id_programa
    
    def str(self):
        return "({}){}".format(self.id, self.nombre)

def from_json(dct):
    return Ultimo(dct['url'], dct['tapa'], dct['nombre'], dct['nombre_programa'], dct['fecha'], dct['id'], dct['id_programa'])