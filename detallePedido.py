from producto import Producto
from receta import Receta
from languageEN import EN
class DetallePedido:
    
    ListDetallePedidos = {}

    def __init__(
        self, numero, 
        cantidad, detalle, pedido):
        '''ATTRIBUTES
            self._codigo
            self._cantidad
            self._pedido
            self._receta
            self._producto
        '''
        self.set_codigo(numero, pedido.get_codigo(), detalle.get_codigo())
        self.set_cantidad(cantidad)
        if isinstance(detalle, Receta):
            self.set_receta(detalle)
        else:
            self.set_producto(detalle)
        self.set_pedido(pedido)
        DetallePedido.ListDetallePedidos[self.get_codigo()] = self

    
    def set_codigo(self, numero, codigo_pedido, codigo_detalle):
        self._codigo = numero +'-'+ codigo_pedido +'-'+ codigo_detalle

    def get_codigo(self):
        return self._codigo

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_cantidad(self):
        return self._cantidad
    
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
        producto_o_receta = null
        if  self.get_producto() is not None:
            producto_o_receta = self.get_producto()
        else:
            producto_o_receta = self.get_receta()

        Str = Mensajes.men.get('formatoDetallePedido') % (
            self.get_codigo(), producto_o_receta.get_nombre(), 
            self.get_cantidad())
        return Str
    
    @staticmethod
    def delete_detalle(codigo):
        detalle = DetallePedido.ListDetallePedidos.pop(codigo)
        detalle.get_pedido().get_detalle_pedidos().pop(codigo)
        if detalle.get_producto() is not None:
            detalle.get_producto().get_detalle_pedidos().pop(codigo)
        if detalle.get_receta() is not None:
            detalle.get_receta().get_detalle_pedidos().pop(codigo)
        


        