from mensajes import Mensajes
from producto import Producto

class DetalleReceta:

    ListDetalleRecetas = []

    def __init__(
        self, cantidad, 
        producto, receta):
        '''ATTRIBUTES
            self._codigo
            self._cantidad
            self._producto
            self._receta
        '''
        self.set_codigo(receta.get_codigo()+'-'+producto.get_codigo())
        self.set_cantidad(cantidad)
        self.set_producto(producto)
        self.set_receta(receta)

        DetalleReceta.ListDetalleRecetas.append(self)

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_cantidad(self, cantidad):
        self._cantidad = int(cantidad)

    def get_cantidad(self):
        return self._cantidad

    def set_producto(self, producto):
        self._producto = producto
        producto.set_detalle_recetas(self)

    def get_producto(self):
        return self._producto

    def set_receta(self, receta):
        self._receta = receta
        receta.set_detalle_recetas(self)

    def get_receta(self):
        return self._receta

    def toString(self):
        Str = Mensajes.men.get('formatoDetalleReceta') % (
            self.get_codigo(), self.get_producto().get_nombre(), 
            str(self.get_cantidad()), self.get_producto().get_medicion())
        return Str
'''
    @staticmethod
    def get_posicion_lista(codigo):
        for i in range(0,len(DetalleReceta.ListDetalleRecetas)):
            if DetalleReceta.ListDetalleRecetas[i].get_codigo() == codigo:
                return i
                break
        return -1

    @staticmethod
    def delete_element(posicion):
        DetalleReceta.ListDetalleRecetas.pop(posicion)
'''