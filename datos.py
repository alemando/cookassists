import random as r
from producto import Producto

#Clase para generar datos ficticios con ciertos valores combinandolos y utilizando la clase random
# @Alejandro

class Datos:

    def generarProductos():
        Producto("Agua", "Liquidos", "infinita", True, "ml")
        #Que hacer con el agua?
        Producto("Sal", "Basicos", 1000, True, "gr")
        Producto("Azucar", "Basicos", 1000, True, "gr")
        Producto("Botella de agua", "Bebidas", 10, True, "Botella(s)")
        Producto("Spaghetti", "pastas", 100, True, "gr")
        Producto("Leche", "Liquidos", 1000, True, "ml")
        Producto("Mantequilla", "Basicos", 1000, True, "gr")
        Producto("Chocolatina", "Snacks", "infinita", True, "N/A")
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