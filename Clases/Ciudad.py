from .Lugar import Lugar
from .Barrio import Barrio
class Ciudad(Lugar):
    ListaBarrios=[]

    def addBarrio(self, Nombre, Codigo, Coordenadas):
        unBarrio = Barrio
        unBarrio.Nombre = Nombre
        unBarrio.Codigo = Codigo
        unBarrio.Coordenadas = Coordenadas
        self.ListaBarrios.append(unBarrio)

    def delBarrio(self, Codigo):
        for i in self.ListaBarrios:
            if i.Codigo == Codigo:
                self.ListaBarrios.remove(i)

    def modBarrio(self, Codigo, nombreAtributo, atributoNuevo):
        for i in self.ListaBarrios:
            if i.Codigo == Codigo:
                i.nombreAtributo = atributoNuevo