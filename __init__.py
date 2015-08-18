# -*- coding: utf-8 -*-
import json

class telefono:

    def __init__(self,numero=0,propietario="",operador=""):
        self.numero = numero
        self.propietario = propietario
        self.operador = operador
        self.contactos = []

    def addContact(self,nombre,numero):
        contacto = json.dumps({'nombre':nombre,'numero':numero})
        self.contactos.append(contacto)
        print("Nuevo contacto: ",contacto)

    def findContact(self,nombre):
        test = False
        for contacto in self.contactos:
            c = json.loads(contacto)
            if nombre == str(c["nombre"]):
                print("El numero de",nombre,"es",int(c["numero"]))
                test = True
        if test != True:
            print("No se encontró el contacto!")

    def info(self):
        print("Telefono de propiedad de:",self.propietario," con el numero:",self.numero,", que pertenece al operador",self.operador)
        print("Lista de telefonos:")
        print(self.contactos)

def main():
    iphone = telefono(3008162990,"Miguel Romero","Tigo")
    iphone.addContact("Papa",3016890833)
    iphone.addContact("Tere",3002574751)
    iphone.info()
    iphone.findContact("Tere")

main()