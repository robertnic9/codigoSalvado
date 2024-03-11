class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False
    marca = ""
    modelo = ""

    def arrancar(self):
        self.enmarcha = True

    def estable(self):
        if self.enmarcha:
            return "El coche está en marcha"
        else:
            return "El coche no está en marcha"

    def descripcion(self):
        datos = "Marca:", self.marca, "Modelo:", self.modelo, "Largo:", self.largoChasis, "Ancho: ", self.anchoChasis, "Ruedas: ", self.ruedas
        return datos

class Camion(Coche):
    PesoCarga = 3000

class persona():
    nombre = ""
    apellidos = ""
    edad = ""

    def descripcion_per(self):
        datos = "Nombre:", self.nombre, "Apellidos:", self.apellidos, "Edad:", self.edad
        return datos

class taxi(Coche,persona):
    def descripcion_taxi(self):
        dato = "Nombre:", self.nombre, "Apellidos:", self.apellidos , "Modelo", self.modelo
        return dato


micoche = Coche()
micoche2 = Coche()
micoche2.largoChasis = 200
micoche2.anchoChasis = 100

micoche3 = Coche()
micoche3.largoChasis = 400
micoche3.anchoChasis = 150

micoche.marca = "Seat"
micoche.modelo = "Ibiza"

micoche2.marca = "BMW"
micoche2.modelo = "M3"

print(micoche.descripcion())
print(micoche2.descripcion())

miCamion = Camion()
miCamion.ruedas = 8
miCamion.marca = "Volvo"
miCamion.modelo = "KIko"
print(miCamion.descripcion())

persona1 = persona()
persona1.nombre = "Manolo"
persona1.apellidos = "Culamen"

persona2 = persona()
persona2.nombre = "Pajaro"
persona2.apellidos = "Blanco"

print(persona1.descripcion_per())

taxi1 = taxi()
print(taxi1.descripcion_taxi())


class Cochazo():
    def __init__(self,largo,ancho,ruedas,color) -> None: #Constructor de la clase Coche
        self.__largoChasis = largo
        self.__anchoChasis = ancho
        self.__ruedas = ruedas
        self.__enmarcha = False # __ para hacerlo variable
        self.__color = color
    def cambiarRuedas(self,n):
        self.__ruedas = n

    def numeroRuedas(self):
        return self.__ruedas

    def valorlargochasis(self):
        return self.__largoChasis

    def valorlargochasis(self):
        return self.__largoChasis

    def valoranchochasis(self):
        return self.__anchoChasis

    def arrancar(self):
        self.enmarcha = True

    def cambiarColor(self, c):
        self.__color = c
    def estado(self):
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El ccoche está parado"

    def descripcion(self):
        datos =  "Largo:", self.__largoChasis, "Ancho: ", self.__anchoChasis, "Ruedas: ", self.__ruedas , "Color: " , self.__color 

micochazo = Cochazo(700,155,4,"Morado")
print("-----------------------------")
micochazo.cambiarColor("Azul")
micochazo.__color = "bLANCO"
print(micochazo.descripcion())

class camionazo(self):
    def __init__(self,largo,ancho,ruedas,color,carga) -> None:
        self.__pesoCarga = carga
        
    def descripcion(self):
        datos = super().descripcion()
        datos ="Carga: " , self.__pesoCarga
        return datos


micamionazo = camionazo(300,173,8,"Negro,",3000)

print(micamionazo.descripcion())