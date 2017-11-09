from .Lugar import Lugar
from .Pais import Pais
class Continente(Lugar):
    ListaPaises=[]

    def addPais(self, Nombre, Codigo, Coordenadas):
        unPais = Pais
        unPais.Nombre = Nombre
        unPais.Codigo = Codigo
        unPais.Coordenadas = Coordenadas
        self.ListaPaises.append(unPais)

    def delPais(self, Codigo):
        for i in self.ListaPaises:
            if i.Codigo == Codigo:
                self.ListaPaises.remove(i)

    def modPais(self, Codigo, nombreAtributo, atributoNuevo):
        for i in self.ListaPaises:
            if i.Codigo == Codigo:
                i.nombreAtributo = atributoNuevo