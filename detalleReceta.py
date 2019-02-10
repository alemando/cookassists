from producto import Producto
from languageEN import EN
class DetalleReceta:

    ListDetalleRecetas = {}

    def __init__(
        self, cantidad, 
        producto, receta):
        '''ATTRIBUTES
            self._codigo
            self._cantidad
            self._producto
            self._receta
        '''
        self.set_codigo(receta.get_codigo(), producto.get_codigo())
        self.set_cantidad(cantidad)
        self.set_producto(producto)
        self.set_receta(receta)
        DetalleReceta.ListDetalleRecetas[self.get_codigo()] = self

    def set_codigo(self, codigo_receta, codigo_producto):
        self._codigo = codigo_receta +'-'+ codigo_producto

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

    def __str__(self):
        Str = EN.men.get('formatoDetalleReceta') % (
            self.get_codigo(), self.get_producto().get_nombre(), 
            str(self.get_cantidad()), self.get_producto().get_medicion())
        return Str

    @staticmethod
    def delete_receta(codigo):
        detalle = DetalleReceta.ListDetalleRecetas.pop(codigo)
        detalle.get_receta().get_detalle_recetas().pop(codigo)
        detalle.get_producto().get_detalle_recetas().pop(codigo)

