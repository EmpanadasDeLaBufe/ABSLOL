from .Lugar import Lugar
from .Ciudad import Ciudad
class Provincia(Lugar):
    ListaCiudades=[]

    def addCiudad(self, Nombre, Codigo, Coordenadas):
        unaCiudad = Ciudad
        unaCiudad.Nombre = Nombre
        unaCiudad.Codigo = Codigo
        unaCiudad.Coordenadas = Coordenadas
        self.ListaCiudades.append(unaCiudad)

    def delCiudad(self, Codigo):
        for i in self.ListaCiudades:
            if i.Codigo == Codigo:
                self.ListaCiudades.remove(i)

    def modCiudad(self, Codigo, nombreAtributo, atributoNuevo):
        for i in self.ListaCiudades:
            if i.Codigo == Codigo:
                i.nombreAtributo = atributoNuevo