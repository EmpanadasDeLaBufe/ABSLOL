from .Lugar import Lugar
class Barrio(Lugar):
    Poblacion = None

    def addPoblacion(self, Poblacion):
        self.Poblacion = Poblacion

    def delPoblacion(self):
        self.Poblacion = None

    def modPoblacion(self, Poblacion):
        self.Poblacion = Poblacion