import os
from Clases import Continente
from Clases import Pais
from Clases import Provincia
from Clases import Ciudad
from Clases import Barrio

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
    print("6- Salir")
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
        Opcion = input("Que desea hacer?")
        print("1- Agregar Pais")
        print("2- Borrar Pais")
        print("3- Modificar Pais")

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

    if Opcion == "3":
        os.system("cls")
        Opcion = input("Que desea hacer?")
        print("1- Agregar Provincia")
        print("2- Borrar Provincia")
        print("3- Modificar Provincia")

        if Opcion == "1":
            addProvincia()

        if Opcion == "2":
            delProvincia()

        if Opcion == "3":
            modProvincia()

    if Opcion == "4":
        os.system("cls")
        Opcion = input("Que desea hacer?")
        print("1- Agregar Ciudad")
        print("2- Borrar Ciudad")
        print("3- Modificar Ciudad")

        if Opcion == "1":
            addCiudad()

        if Opcion == "2":
            delCiudad()

        if Opcion == "3":
            modCiudad()

    if Opcion == "5":
        os.system("cls")
        Opcion = input("Que desea hacer?")
        print("1- Agregar Poblacion")
        print("2- Borrar Poblacion")
        print("3- Modificar Poblacion")

        if Opcion == "1":
            addCiudad()

        if Opcion == "2":
            delCiudad()

        if Opcion == "3":
            modCiudad()


os.system("cls")
Opcion = input("Hola!!!!! Apreta e para agregar un continente  ")
if Opcion == "E" or Opcion == "e":
    Nombre = input("Nombre del continente  ")
    Codigo = input("Codigo del continente  ")
    Coordenadas = input("Coordenadas del continente  ")
    addContinente(Nombre, Codigo, Coordenadas)
while True:
    main()