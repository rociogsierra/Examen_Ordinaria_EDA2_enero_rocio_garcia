
#3.1 CREACIÓN
#creo la clase artefactos valiosos
class artefactos_valiosos():
    def __init__(self, peso, nombre, precio, fecha_de_caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.fecha_de_caducidad = fecha_de_caducidad

        #imprimo el mensaje propuesto en el enunciado
        print("La conserva se ha creado con éxito")

    def __str__(self):
        return f'peso: {self.peso}, nombre: {self.nombre}, precio: {self.precio}, fecha de caducidad: {self.fecha_de_caducidad}'

#3.2 EXPERIMENTACIÓN

#creo dos artefactos
from artefactos_valiosos import*
artefacto1 = artefactos_valiosos("7", "maiz", "3", "27/10/2023")
artefacto2 = artefactos_valiosos("0.1", "tomate", "9", "07/11/2025")     

#modificar algun valor por su fecha de caducidad
artefacto2 = artefactos_valiosos("0.1", "tomate", "9", "01/01/2023") 




        