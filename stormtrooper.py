
#1.1 CREACIÓN
class stormtrooper():
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    
    def  __str__(self):
        return f'nombre: {self.nombre}, rango: {self.rango}'
        print("el stormtrooper se ha creado con éxito")


