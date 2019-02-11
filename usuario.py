from languageEN import EN

class Usuario:

    ListUsuarios = {}

    def __init__(
            self, admin, id_type, id, 
            name, password, born_date):
        '''ATTRIBUTES
            self._admin
            self._id_type
            self._id
            self._name
            self._password
            self._born_date
        '''
        self._ListCalificaciones = {}
        self._ListPedidos = {}
        self.set_admin(admin)
        self.set_id_type(id_type)
        self.set_id(id)
        self.set_name(name)
        self.set_password(password)
        self.set_born_date(born_date)
        Usuario.ListUsuarios[self.get_id_type() +'-'+ self.get_id()] = self

    def set_admin(self, admin):
        self._admin = admin

    def get_admin(self):
        return self._admin

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_id_type(self, id_type):
        self._id_type = id_type

    def get_id_type(self):
        return self._id_type

    def set_id(self, id):
        self._id= id

    def get_id(self):
        return self._id

    def set_born_date(self, born_date):
        self._born_date = born_date

    def get_born_date(self):
        return self._born_date

    def set_password(self, password):
        self._password = password

    def get_password(self):
        return self._password

    def set_calificaciones(self, calificacion):
        self._ListCalificaciones[calificacion.get_codigo()] = calificacion

    def get_calificaciones(self):
        return self._ListCalificaciones

    def set_pedidos(self, pedido):
        self._ListPedidos[pedido.get_codigo()] = pedido

    def get_pedidos(self):
        return self._ListPedidos

    def __str__(self):
        Str = EN.men.get('str_user') % (
                self.get_admin(), self.get_name(), 
                self.get_id_type, self.get_id(), self.get_born_date())
        return Str

    @staticmethod
    def get_user_by_id(id_type, id):
        return Usuario.ListUsuarios.get(id_type +'-'+ id)

    @staticmethod
    def check_id(id):
        for user in Usuario.ListUsuarios.values():
            if user.get_id() == id:
                return False
        return True

    @staticmethod
    def check_login(id_type, id, password):
        user = Usuario.get_user_by_id(id_type, id)
        if user is not None:
            if user.get_password() == password:
                return user
        return None
        
