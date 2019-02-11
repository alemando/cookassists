from usuario import Usuario

class Chef(Usuario):

    ListChefs = {}

    def __init__(
            self, tipo_usuario, nombre, tipo_identificacion, identificacion, fecha_nacimiento, 
            contrasena):
        super().__init__(tipo_usuario, nombre, tipo_identificacion, 
                        identificacion, fecha_nacimiento, contrasena)
        self._ListCalificacionesChef = {}
        self._ListPedidosChef = {}
        Chef.ListChefs[self.get_identificacion()] = self

    def set_calificaciones_chef(self, calificacion):
        self._ListCalificacionesChef[calificacion.get_codigo()] = calificacion

    def get_calificaciones_chef(self):
        return self._ListCalificacionesChef

    def set_pedidos_chef(self, pedido):
        self._ListPedidosChef[pedido.get_codigo()] = pedido

    def get_pedidos_chef(self):
        return self._ListPedidosChef