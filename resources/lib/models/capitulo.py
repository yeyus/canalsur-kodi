class Capitulo(object):
    """ Class for keeping info about a Capitulo """
    def __init__(self, url, tapa, capitulo, fecha, id):
        self.url = url
        self.tapa = tapa
        self.capitulo = capitulo
        self.fecha = fecha
        self.id = id
    
    def str(self):
        return "({}){}".format(self.id, self.capitulo)

def from_json(dct):
    return Capitulo(dct['url'], dct['tapa'], dct['capitulo'], dct['fecha'], dct['id'])
