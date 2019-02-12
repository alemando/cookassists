from usuario import Usuario

class Chef(Usuario):

    ListChefs = {}

    def __init__(
            self, tipo_usuario, nombre, tipo_identificacion, 
            identificacion, fecha_nacimiento, contrasena):
        '''ATTRIBUTES
            self._admin
            self._id_type
            self._id
            self._name
            self._password
            self._born_date
            self._status
            self._status_chef
        '''
        super().__init__(tipo_usuario, nombre, tipo_identificacion, 
                        identificacion, fecha_nacimiento, contrasena)
        self._ListCalificacionesChef = {}
        self._ListPedidosChef = {}
        Chef.ListChefs[self.get_id_type() +'-'+ self.get_id()] = self
    
    def set_status_chef(self, status):
        self._status_chef = status

    def get_status_chef(self):
        return self._status_chef

    def set_calificaciones_chef(self, calificacion):
        self._ListCalificacionesChef[calificacion.get_codigo()] = calificacion

    def get_calificaciones_chef(self):
        return self._ListCalificacionesChef

    def set_pedidos_chef(self, pedido):
        self._ListPedidosChef[pedido.get_codigo()] = pedido

    def get_pedidos_chef(self):
        return self._ListPedidosChef
    
    @staticmethod
    def get_chef_by_id(id_type, id):
        return Chef.ListChefs.get(id_type +'-'+ id)

    @staticmethod
    def get_chef_by_name(name):
        ListCoincidencias = []
        for chef in Chef.ListChefs.values():
            if chef.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(chef)
        return ListCoincidencias