import time
from detallePedido import DetallePedido
from languageEN import EN
class Pedido:

    ListPedidos = {}
    auto_increment_codigo = 0

    def __init__(
        self, usuario, detalle_pedido, 
        descripcion, chef = None):
        '''ATTRIBUTES
            self._codigo
            self._numero_detalle
            self._fecha
            self._descripcion
            self._usuario
            self._chef
        '''
        self._ListDetallePedido = {}
        self.set_codigo()
        self._numero_detalle = 0
        self.set_fecha()
        self.set_descripcion(descripcion)
        self.set_usuario(usuario)
        self.set_chef(chef)
        for detalle in detalle_pedido:
            DetallePedido(self.get_numero_detalle, detalle.get('cantidad'), detalle.get('detalle'), self)
        Pedido.ListPedidos[self.get_codigo()] = self

    def set_codigo(self):
        Receta.auto_increment_codigo += 1
        codigo = Receta.auto_increment_codigo
        self._codigo = str(codigo)

    def get_codigo(self):
        return self._codigo
    
    def get_numero_detalle(self):
        self._numero_detalle += 1
        return self._numero_detalle
    
    def set_fecha(self, fecha):
        self._fecha = time.strftime("%c")

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
        self._ListDetallePedido[detalle_pedido.get_codigo()] = detalle_pedido

    def get_detalle_pedidos(self):
        return self._ListDetallePedido
    
    def editar_receta(self, opcion, valor):
        if opcion == '1':
            self.set_nombre(valor)
        elif opcion == '2':
            self.set_tiempo_preparacion(valor)
        elif opcion == '3':
            for detalle in valor:
                DetalleReceta(detalle.get('cantidad'), detalle.get('producto'), self)
        elif opcion == '4':
            detalle = self.get_detalle_pedidos.get(valor.get('codigo'))
            detalle.set_cantidad(valor.get('cantidad'))
        elif opcion == '5':
            DetalleReceta.delete_receta(valor)

    def __str__(self):
        Str = EN.men.get('formatoPedido') % (
            self.get_codigo(), self.get_fecha(), self.get_descripcion(), 
            self.get_usuario().get_nombre(), self.get_chef().get_nombre())
        for detalle in _ListDetallePedido.values():
            Str+= detalle.__str__() + '\n'
        return Str

    @staticmethod
    def get_pedido_by_codigo(codigo):
        return Pedido.ListPedidos.get(codigo)