

class DetallePedido:
    
    ListDetallePedidos = []

    def __init__(
        self, cantidad,
        pedido, receta, producto):
        '''ATTRIBUTES
            self._codigo
            self._cantidad
            self._pedido
            self._receta
            self._producto
        '''
        self.set_codigo(pedido.get_codigo()+'-'+receta.get_codigo())
        self.set_cantidad(cantidad)
        self.set_pedido(pedido)
        self.set_receta(receta)
        self.set_producto(producto)
        DetallePedido.ListDetallePedidos.append(self)

    
    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def get_cantidad(self):
        return self._cantidad
    
    def set_pedido(self, pedido):
        self._pedido = pedido

    def get_pedido(self):
        return self._pedido
    
    def set_receta(self, receta):
        self._receta = receta

    def get_receta(self):
        return self._receta
    
    def set_producto(self, producto):
        self._producto = producto

    def get_producto(self):
        return self._producto
    
    def toString(self):
        producto_o_receta = null
        if  self.get_producto == null:
            producto_o_receta = self.get_receta()
        else:
            producto_o_receta = self.get_producto()

        Str = Mensajes.men.get('formatoDetallePedido') % (
            self.get_codigo(), producto_o_receta.get_nombre(), 
            self.get_cantidad())
        return Str

        