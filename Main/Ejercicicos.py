from math import sqrt
from getpass import getpass
import os
from time import sleep
seguir="S"
while (seguir=="S"):
    print ("\n \n Menu principal:")
    print ("1-Total alumnos")
    print ("2-Figuritas")
    print ("3-Promedio")
    print ("4-Dolares a Pesos")
    print ("5-Antiguedad")
    print ("6-Hipotenusa")
    print ("0-Salir")
    opcion=input("Ingrese opcion:")
    if (opcion=="1"):
        Sociales=input("cuantos alumnos hay en Sociales? ")
        Naturales=input("cuantos alumnos hay en Naturales? ")
        Economia=input("cuantos alumnos hay en Economia? ")
        Total=int(Sociales)+int(Naturales)+int(Economia)
        print("En itinerario son ", Total, " Alumnos")
        if (Naturales>Sociales and Naturales>Economia):
            print ("Naturales tiene mas alumnos")
        else :
            if(Sociales>Economia and Sociales>Naturales):
                print ("sociales tiene mas alumnos")
            else :
                if(Economia>Sociales and Economia>Naturales):
                        print ("Economia tiene mas alumnos")
                else:
                        print ("hay 2 o mas cursos con la misma cantdad")
    if (opcion=="2"):
        Juan=input("Figuritas de Juan ")
        Maria=input("Figuritas de Maria ")
        if (Juan!=Maria):
            Juan, Maria = Maria, Juan
            print("Juan tiene", Juan, "Figuritas ")
            print("Maria tiene", Maria, " Figuritas ")
        else:
            print ("No se le puede cambiar las figuritas porque ambos tienen la misma cantidad")
    if (opcion=="3"):
        primer=input("Que nota tenes en tu primer cuatriestre ")
        segundo=input("Que nota tenes en tu segundo cuatrimestre ")
        nota=(int(primer)+int(segundo))/2
        print("tu promedio es", float (nota))
        if (nota>=7):
            print ("Estas aprobado")
        else:
            print ("Estas desaprobado")
    if (opcion=="4"):
        Dolar=input("cuantos dolares tienes? ")
        if (Dolar>=1000):
            print ("Sus dolares fueron retenidos por el banco")
        else:
            Peso=input("cuanto vale el peso argentino? ")
            Resultado=int(Dolar)*int(Peso)
            print("usted tiene $" + str(Resultado))
    if (opcion=="5"):
        inicio=input("Para saber la antiguedad del trabajador necesiamos primero saber en que año empezo a trabajar en la empresa ")
        final=input("Ahora necesitamos saber hasta que año llevo trabajando en la empresa ")
        antiguedad=int(final)-int(inicio)
        print("El trabajador tiene", antiguedad, "años de antiguedad trabajando")
        if (antiguedad>=30):
            print ("El trabajador ya puede jubilarse")
        else:
            años=30-int (antiguedad)
            print ("Aún le quedan",años,"años trabajando en su empresa para jubilarse")
    if (opcion=="6"):
        usuario=input("ingrese usuario ")
        clave=getpass(prompt="ingrese clave ")
        if (usuario=="admin" and clave=="iti"):
            A=input("Ingrese cateto A:")
            B=input("Ingrese cateto B:")
            H= sqrt(pow(float(A),2)+float(B)**2)
            print ("La hipotenusa es", H)
        else:
            os.system("cls")
            os.system("color 0c")
            print("usurio o contraceña incorrecto")
            os.system("cls")
            os.system("color 07")
    if (opcion=="0"):
        seguir="N"
    
