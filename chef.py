from usuario import Usuario

class Chef(Usuario):

    ListChefs = {}

    def __init__(
            self, admin, email, 
            name, password, born_date):
        '''ATTRIBUTES
            self._admin
            self._email
            self._name
            self._password
            self._born_date
            self._status
            self._status_chef
        '''
        super().__init__(
                    admin, email, name,
                    password, born_date)
        self._ListCalificacionesChef = {}
        self._ListPedidosChef = {}
        self.set_status_chef(True)
        Chef.ListChefs[email] = self
    
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
    def get_chef_by_email(email):
        return Chef.ListChefs.get(email)
        

    @staticmethod
    def get_chef_by_name(name):
        ListCoincidencias = []
        for chef in Chef.ListChefs.values():
            if chef.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(chef)
        return ListCoincidencias