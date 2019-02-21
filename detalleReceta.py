from languageEN import EN
class DetalleReceta:

    ListDetalleRecetas = {}

    def __init__(
        self, quantity, 
        producto, receta):
        '''ATTRIBUTES
            self._code
            self._quantity
            self._producto
            self._receta
        '''
        self.set_code(receta.get_code(), producto.get_code())
        self.set_quantity(quantity)
        self.set_producto(producto)
        self.set_receta(receta)
        DetalleReceta.ListDetalleRecetas[self.get_code()] = self

    def set_code(self, code_receta, code_producto):
        self._code = code_receta +'-'+ code_producto

    def get_code(self):
        return self._code

    def set_quantity(self, quantity):
        self._quantity = int(quantity)

    def get_quantity(self):
        return self._quantity

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
        code = self.get_code()
        producto_name = self.get_producto().get_name()
        quantity = self.get_quantity()
        measurement = self.get_producto().get_measurement()
        Str = EN.men.get('detalle_receta_pattern') % (
            code, producto_name, 
            quantity, measurement)
        return Str

    @staticmethod
    def delete_detalle(code):
        detalle = DetalleReceta.ListDetalleRecetas.pop(code)
        detalle.get_receta().get_detalle_recetas().pop(code)
        detalle.get_producto().get_detalle_recetas().pop(code)

