class Programa(object):
    """ Class for keeping info about a Programa """
    def __init__(self, nombre, descripcion, publicidad, id):
        self.nombre = nombre
        self.descripcion = descripcion
        self.publicidad = publicidad
        self.id = id
    
    def thumbnail(self):
        return "https://www.canalsur.es/resources/programas/{}_principal.jpg".format(self.id)
    
    def banner(self):
        return "https://www.canalsur.es/resources/programas/{}_fondo.jpg".format(self.id)
    
    def str(self):
        return "({}){}".format(self.id, self.nombre)

def from_json(dct):
    return Programa(dct['nombre'], dct['descripcion'], dct['publicidad'], dct['id'])

