from producto import Producto
from receta import Receta
from languageEN import EN
class DetallePedido:
    
    ListDetallePedidos = {}

    def __init__(
        self, num, 
        quantity, detalle, pedido):
        '''ATTRIBUTES
            self._code
            self._quantity
            self._pedido
            self._receta
            self._producto
        '''
        self.set_code(num, pedido.get_code(), detalle.get_code())
        self.set_quantity(quantity)
        if isinstance(detalle, Receta):
            detalle.change_quantity_to_producto(quantity,'-')
            self.set_receta(detalle)
        else:
            detalle.change_quantity(quantity,'-')
            self.set_producto(detalle)
        self.set_pedido(pedido)
        DetallePedido.ListDetallePedidos[self.get_code()] = self

    
    def set_code(self, num, code_pedido, code_detalle):
        self._code = str(num) +'-'+ code_pedido +'-'+ code_detalle

    def get_code(self):
        return self._code

    def set_quantity(self, quantity):
        self._quantity = int(quantity)

    def get_quantity(self):
        return self._quantity
    
    def set_pedido(self, pedido):
        self._pedido = pedido
        pedido.set_detalle_pedidos(self)

    def get_pedido(self):
        return self._pedido
    
    def set_receta(self, receta):
        self._receta = receta
        receta.set_detalle_pedidos(self)

    def get_receta(self):
        return self._receta
    
    def set_producto(self, producto):
        self._producto = producto
        
        producto.set_detalle_pedidos(self)

    def get_producto(self):
        return self._producto
    
    def __str__(self):
        code = self.get_codigo()

        producto_o_receta = null
        if  self.get_producto():
            producto_o_receta = self.get_producto()
        else:
            producto_o_receta = self.get_receta()
        name = producto_o_receta.get_nombre()
        quantity = self.get_quantity()
        Str = Mensajes.men.get('detalle_pedido_pattern') % (
            code, name, quantity) 
        return Str
    
    @staticmethod
    def delete_detalle(code):
        detalle = DetallePedido.ListDetallePedidos.pop(code)
        detalle.get_pedido().get_detalle_pedidos().pop(code)
        if detalle.get_producto() is not None:
            detalle.get_producto().get_detalle_pedidos().pop(code)
        if detalle.get_receta() is not None:
            detalle.get_receta().get_detalle_pedidos().pop(code)
        #debo sumar lo que quite al crear
        


        