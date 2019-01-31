

class Pedido:

    ListPedidos = []
    auto_increment_codigo = 0

    def __init__(
        self, descripcion
        usuario, chef):
        '''ATTRIBUTES
            self._codigo
            self._fecha
            self._descripcion
            self._usuario
            self._chef
        '''
        self._ListDetallePedido = []
        self.set_codigo(str(auto_increment_codigo))
        self.set_fecha('''Tomo la fecha desde python''')
        self.set_descripcion(descripcion)
        self.set_usuario(usuario)
        self.set_chef(chef)

    def set_codigo(self, codigo):
        self._codigo = codigo

    def get_codigo(self):
        return self._codigo
    
    def set_fecha(self, fecha):
        self._fecha = fecha

    def get_fecha(self):
        return self._fecha
    
    def set_descripcion(self, descripcion):
        self._descripcion = descripcion

    def get_descripcion(self):
        return self._descripcion
    
    def set_usuario(self, usuario):
        self._usuario = usuario

    def get_usuario(self):
        return self._usuario
    
    def set_chef(self, chef):
        self._chef = chef

    def get_chef(self):
        return self._chef
    
    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedido.append(detalle_pedido)

    def get_detalle_pedidos(self):
        return self._ListDetallePedido
    
    def toString(self):
        Str = Mensajes.men.get('formatoPedido') % (
            self.get_codigo(), self.get_fecha(), 
            self.get_descripcion(), self.get_usuario().get_nombre(), self.get_chef().get_nombre())
            for detalle in _ListDetallePedido:
            Str+= detalle.toString()
        return Str