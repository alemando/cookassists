import random as r
from producto import Producto

#Clase para generar datos ficticios con ciertos valores combinandolos y utilizando la clase random
# @Alejandro

class Datos:

    def generarProductos():
        Producto("Agua", "3", 0, "1", "2", "1")
        Producto("Sal", "1", 1000, "1", "3", "2")
        Producto("Azucar", "1", 1000, "1", "3", "2")
        Producto("Botella de agua", "Bebidas", 10, "1", "1", "2")
        Producto("Spaghetti", "2", 100, "1", "3", "2")
        Producto("Leche", "3", 1000, "1", "2", "2")
        Producto("Mantequilla", "1", 1000, "1", "2", "2")
        Producto("Chocolatina", "4", 10, "1", "1", "2")
        #Usuario(True, 'CC', '1238938010', 'Alejandro Jiménez', '12345', '28/10/1999')
'''
    @staticmethod
    def generarComentarios(cant):
        #Cantidad de comentarios que quiero generar aleatoriamente
        while cant > 0:
            puntuacion = r.randint(1, 5)
            #Tomo los valores de la descripcion segun la puntuacion el -1 para ajustar el tamaño de la lista
            descripcion = Datos.descripcion[(puntuacion-1)]
            art = r.choice(Articulo.listaArticulos)
            Comentario(descripcion,puntuacion,art);
            cant = cant - 1
'''