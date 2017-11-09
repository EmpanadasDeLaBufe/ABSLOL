from .Lugar import Lugar
from .Provincia import Provincia
class Pais(Lugar):
    ListaProvincias=[]

    def addProvincia(self, Nombre, Codigo, Coordenadas):
        unaProvincia = Provincia
        unaProvincia.Nombre = Nombre
        unaProvincia.Codigo = Codigo
        unaProvincia.Coordenadas = Coordenadas
        self.ListaProvincias.append(unaProvincia)

    def delProvincia(self, Codigo):
        for i in self.ListaProvincias:
            if i.Codigo == Codigo:
                self.ListaProvincias.remove(i)

    def modProvincia(self, Codigo, nombreAtributo, atributoNuevo):
        for i in self.ListaProvincias:
            if i.Codigo == Codigo:
                i.nombreAtributo = atributoNuevo