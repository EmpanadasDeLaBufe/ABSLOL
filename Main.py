import os
from Clases.Continente import Continente
from Clases.Pais import Pais
from Clases.Provincia import Provincia
from Clases.Ciudad import Ciudad
from Clases.Barrio import Barrio

ListaContinentes = []

def addContinente(Nombre, Codigo, Coordenadas):
    unContinente = Continente
    unContinente.Nombre = Nombre
    unContinente.Codigo = Codigo
    unContinente.Coordenadas = Coordenadas
    ListaContinentes.append(unContinente)

def delContinente(Codigo):
    for i in ListaContinentes:
        if i.Codigo == Codigo:
            ListaContinentes.remove(i)

def modContinente(Codigo, nombreAtributo, atributoNuevo):
    for i in ListaContinentes:
        if i.Codigo == Codigo:
            i.nombreAtributo = atributoNuevo

def main():
    os.system("cls")
    print("1- Continente")
    print("2- Pais")
    print("3- Provincia")
    print("4- Ciudad")
    print("5- Barrio")
    print("6- Poblacion")
    print("7- Listar Lugares")
    Opcion = input("Con que desea trabajar?  ")

    if Opcion == "1":
        os.system("cls")
        print("1- Agregar Continente")
        print("2- Borrar Continente")
        print("3- Modificar Continente")
        Opcion = input("Que desea hacer?  ")

        if Opcion == "1":
            Nombre = input("Nombre del continente  ")
            Codigo = input("Codigo del continente  ")
            Coordenadas = input("Coordenadas del continente  ")
            addContinente(Nombre, Codigo, Coordenadas)
            print("Continente agregado!")
            input()

        if Opcion == "2":
            if len(ListaContinentes) > 0:
                Codigo = input("Ingresar codigo de Continente a eliminar  ")
                delContinente(Codigo)
                print("Continente eliminado!")
                input()
            else:
                print("No hay Continentes")
                input()

        if Opcion == "3":
            if len(ListaContinentes) > 0:
                Codigo = input("Ingresar codigo Continente  ")
                nombreAtributo = input("Ingresar nombre atributo a modificar  ")
                atributoNuevo = input("Ingresar atributo nuevo  ")
                modContinente(Codigo, nombreAtributo, atributoNuevo)
                print("Continente modificado!")
                input()
            else:
                print("No hay continentes")
                input()

    if Opcion == "2":
        os.system("cls")

        Codigo = input("Ingresar codigo del continente al que esta asociado  ")
        for i in ListaContinentes:
            if i.Codigo == Codigo:
                Aux = i
        os.system("cls")
        print("1- Agregar Pais")
        print("2- Borrar Pais")
        print("3- Modificar Pais")
        Opcion = input("Que desea hacer?  ")

        if Opcion == "1":
            Nombre = input("Nombre del pais  ")
            Codigo = input("Codigo del pais  ")
            Coordenadas = input("Coordenadas del pais  ")
            Aux.addPais(Nombre, Codigo, Coordenadas)
            input("Pais creado  ")

        if Opcion == "2":
            if len(Aux.ListaPaises) > 0:
                Codigo = input("Ingresar codigo de Pais a eliminar  ")
                Aux.delPais(Codigo)
                print("Pais eliminado!")
                input()
            else:
                print("No hay Paises en ese continente")
                input()

        if Opcion == "3":
            if len(Aux.ListaContinentes) > 0:
                Codigo = input("Ingresar codigo pais  ")
                nombreAtributo = input("Ingresar nombre atributo a modificar  ")
                atributoNuevo = input("Ingresar atributo nuevo  ")
                Aux.modPais(Codigo, nombreAtributo, atributoNuevo)
                print("Pais modificado!")
                input()
            else:
                print("No hay paises en ese continente")
                input()

    if Opcion == "3":
        os.system("cls")
        Codigo = input("Ingresar codigo del pais al que esta asociado  ")
        for i in ListaContinentes:
            for x in i.ListaPaises:
                if x.Codigo == Codigo:
                    Aux = x
        os.system("cls")
        print("1- Agregar provincia")
        print("2- Borrar provincia")
        print("3- Modificar provincia")
        Opcion = input("Que desea hacer?  ")

        if Opcion == "1":
            Nombre = input("Nombre del pais  ")
            Codigo = input("Codigo del pais  ")
            Coordenadas = input("Coordenadas del pais  ")
            Aux.addProvincia(Nombre, Codigo, Coordenadas)
            input("Provincia creada  ")

        if Opcion == "2":
            if len(Aux.ListaProvincias) > 0:
                Codigo = input("Ingresar codigo de provincia a eliminar  ")
                Aux.delProvincia(Codigo)
                print("Provincia eliminada!")
                input()
            else:
                print("No hay provincias en ese pais")
                input()

        if Opcion == "3":
            if len(Aux.ListaProvincias) > 0:
                Codigo = input("Ingresar codigo provincia  ")
                nombreAtributo = input("Ingresar nombre atributo a modificar  ")
                atributoNuevo = input("Ingresar atributo nuevo  ")
                Aux.modProvincia(Codigo, nombreAtributo, atributoNuevo)
                print("Provincia modificada!")
                input()
            else:
                print("No hay provincias en ese pais")
                input()

    if Opcion == "4":
        os.system("cls")
        Codigo = input("Ingresar codigo de la provincia al que esta asociado  ")
        for i in ListaContinentes:
            for x in i.ListaPaises:
                for z in x.ListaCiudades:
                    if z.Codigo == Codigo:
                        Aux = z
        os.system("cls")
        print("1- Agregar ciudad")
        print("2- Borrar ciudad")
        print("3- Modificar ciudad")
        Opcion = input("Que desea hacer?  ")

        if Opcion == "1":
            Nombre = input("Nombre del pais  ")
            Codigo = input("Codigo del pais  ")
            Coordenadas = input("Coordenadas del pais  ")
            Aux.addCiudad(Nombre, Codigo, Coordenadas)
            input("Ciudad creada  ")

        if Opcion == "2":
            if len(Aux.ListaCiudadades) > 0:
                Codigo = input("Ingresar codigo de la ciudad a eliminar  ")
                Aux.delCiudad(Codigo)
                print("Ciudad eliminada!")
                input()
            else:
                print("No hay Ciudades en esa provincia")
                input()

        if Opcion == "3":
            if len(Aux.ListaCiudadades) > 0:
                Codigo = input("Ingresar codigo ciudad  ")
                nombreAtributo = input("Ingresar nombre atributo a modificar  ")
                atributoNuevo = input("Ingresar atributo nuevo  ")
                Aux.modCiudad(Codigo, nombreAtributo, atributoNuevo)
                print("Ciudad modificada!")
                input()
            else:
                print("No hay Ciudades en esa provincia")
                input()

    if Opcion == "5":
        os.system("cls")
        Codigo = input("Ingresar codigo de la ciudad al que esta asociado  ")
        for i in ListaContinentes:
            for x in i.ListaPaises:
                for z in x.ListaProvincias:
                    for w in z.ListaCiudades:
                        if w.Codigo == Codigo:
                            Aux = w
        os.system("cls")
        print("1- Agregar barrio")
        print("2- Borrar barrio")
        print("3- Modificar barrio")
        Opcion = input("Que desea hacer?  ")

        if Opcion == "1":
            Nombre = input("Nombre del barrio  ")
            Codigo = input("Codigo del barrio  ")
            Coordenadas = input("Coordenadas del barrio  ")
            Aux.addBarrio(Nombre, Codigo, Coordenadas)
            input("Barrio creado  ")

        if Opcion == "2":
            if len(Aux.ListaBarrios) > 0:
                Codigo = input("Ingresar codigo del barrio a eliminar  ")
                Aux.delBarrio(Codigo)
                print("Barrio eliminado!")
                input()
            else:
                print("No hay barrios en esa ciudad")
                input()

        if Opcion == "3":
            if len(Aux.ListaBarrios) > 0:
                Codigo = input("Ingresar codigo barrio  ")
                nombreAtributo = input("Ingresar nombre atributo a modificar  ")
                atributoNuevo = input("Ingresar atributo nuevo  ")
                Aux.modBarrio(Codigo, nombreAtributo, atributoNuevo)
                print("Barrio modificado!")
                input()
            else:
                print("No hay barrios en esa ciudad")
                input()

    if Opcion == "6":
        os.system("cls")
        Codigo = input("Ingresar codigo del barrio  ")
        for i in ListaContinentes:
            for x in i.ListaPaises:
                for z in x.ListaProvincias:
                    for w in z.ListaCiudades:
                        for q in w.ListaBarrios:
                            if q.Codigo == Codigo:
                                Aux = q
        os.system("cls")
        print("1- Agregar Poblacion")
        print("2- Borrar Poblacion")
        print("3- Modificar Poblacion")
        Opcion = input("Que desea hacer?  ")

        if Opcion == "1":
            Poblacion = input("Poblacion del barrio  ")
            Aux.addPoblacion(Poblacion)
            input("Poblacion agregada  ")

        if Opcion == "2":
            Aux.delPoblacion()
            input("Poblacion borrada  ")

        if Opcion == "3":
            Poblacion = input("Ingresar nueva poblacion  ")
            Aux.modPoblacion(Poblacion)
            print("Barrio modificado!")
            input()

    if Opcion == "7":
        os.system("cls")
        for a in ListaContinentes:
            print(a.Codigo, a.Nombre)
            for b in a.ListaPaises:
                print(b.Codigo, b.Nombre)
                for c in b.ListaProvincias:
                    print(c.Codigo, c.Nombre)
                    for d in c.ListaCiudades:
                        print(d.Codigo, d.Nombre)
                        for e in d.ListaBarrios:
                            print(e.Codigo, e.Nombre)
        input("Enter para continuar  ")




os.system("cls")
Opcion = input("Hola!!!!! Apreta e para agregar un continente  ")
if Opcion == "E" or Opcion == "e":
    Nombre = input("Nombre del continente  ")
    Codigo = input("Codigo del continente  ")
    Coordenadas = input("Coordenadas del continente  ")
    addContinente(Nombre, Codigo, Coordenadas)
while True:
    main()