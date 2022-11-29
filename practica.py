#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola

#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
#servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Producto:
    def __init__(self,nombre,unidades,precio):
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio

    def infoServicio(self):
        print(f"El nombre del producto es {self.nombre}")
        print(f"El precio del producto es {self.precio}€")
        print(f"Las unidades del producto es {self.unidades}€")
        print(f"Uxp = {self.precio * self.unidades}€")

class Servicio:

    def consultarDetalle(self):
        print("El servicio es basico")



class Estandar (Servicio):
    def consultarDetalle(self):
        print("Es un servicio estandar")


class Premium(Servicio):
    def consultarDetalle(self):

        print("Es un servicio premium")

p1 = Producto("camisa",10,9.95)

print (p1.nombre)




servicio = input("Indique el servicio: ")
if servicio == "premium":
    servicio1 = Premium()
    servicio1.consultarDetalle()


elif servicio == "estandar":
    servicio1 = Estandar()
    servicio1.consultarDetalle()

else:
    print("Error")











