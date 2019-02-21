import datetime
from detallePedido import DetallePedido
from languageEN import EN
class Pedido:

    ListPedidos = {}
    auto_increment_code = 0

    def __init__(
        self, usuario, detalle_pedido, description, date = None,
        code = None, chef = None, qualified = False, ready = False):
        '''ATTRIBUTES
            self._code
            self._num_detalle
            self._date
            self._description
            self._usuario
            self._chef
            self._ready
            self._qualified
        '''
        self._ListDetallePedido = {}
        self.set_code(code)
        self._num_detalle = 0
        self.set_date(date)
        self.set_qualified(qualified)
        self.set_ready(ready)
        self.set_description(description)
        self.set_usuario(usuario)
        self.set_chef(chef)
        for detalle in detalle_pedido:
            DetallePedido(self.get_num_detalle(), detalle.get('quantity'), detalle.get('detalle'), self)
        Pedido.ListPedidos[self.get_code()] = self

    def set_code(self, code):
        aux_code = Pedido.auto_increment_code
        if code:
            if code > aux_code:
                Pedido.auto_increment_code = code
        else:
            Pedido.auto_increment_code += 1
            code = Pedido.auto_increment_code
        self._code = str(code)

    def get_code(self):
        return self._code
    
    def get_num_detalle(self):
        self._num_detalle += 1
        return self._num_detalle
    
    def set_date(self, date):
        if date is None:
            self._date = datetime.datetime.now().strftime("%d/%m/%Y")
        else:
            self._date = date

    def get_date(self):
        return self._date

    def set_ready(self, ready):
        self._ready = ready

    def get_ready(self):
        return self._ready

    def set_qualified(self, qualified):
        self._qualified = qualified

    def get_qualified(self):
        return self._qualified

    
    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description
    
    def set_usuario(self, usuario):
        self._usuario = usuario
        usuario.set_pedidos(self)

    def get_usuario(self):
        return self._usuario
    
    def set_chef(self, chef):
        if chef:
            self._chef = chef
            chef.set_pedidos_chef(self)
        else:
            self._chef = chef

    def get_chef(self):
        return self._chef
    
    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedido[detalle_pedido.get_code()] = detalle_pedido

    def get_detalle_pedidos(self):
        return self._ListDetallePedido
    
    def add_more_detalle_pedido(self, detalle_pedido):
        for detalle in detalle_pedido:
            DetallePedido(detalle.get('quantity'), detalle.get('detalle'), self)

    def __str__(self):
        code = self.get_code()
        date = self.get_date()
        user = self.get_usuario().get_name()
        chef = self.get_chef()
        if chef:
            chef = self.get_chef().get_name()
        else:
            chef = ''
        ready = self.get_ready()
        if ready:
            ready = EN.men.get('yes')
        else:
            ready = EN.men.get('no')
        Str = EN.men.get('pedido_pattern') % (
            code, date,  
            user, chef, ready)
        Str+= EN.men.get('detalle_pedido_pattern_header')
        for detalle in self.get_detalle_pedidos().values():
            Str+= detalle.__str__()
        return Str

    @staticmethod
    def see_pedido():
        Str = EN.men.get('str_see_pedido_header')
        for pedido in Pedido.ListPedidos.values():
            code = pedido.get_code().zfill(6)
            date = pedido.get_date()
            usuario = pedido.get_usuario().get_name()
            chef = pedido.get_chef()
            if chef:
                chef = pedido.get_chef().get_name()
            else:
                chef = ''
            ready = pedido.get_ready()
            if ready:
                ready = EN.men.get('yes')
            else:
                ready = EN.men.get('no')
            Str += EN.men.get('str_see_pedido') % (
                    code, date, ready, usuario, chef)
        return Str

    @staticmethod
    def see_pedido_pending():
        Str = EN.men.get('str_see_pedido_header')
        for pedido in Pedido.ListPedidos.values():
            if (pedido.get_chef() is None) or (not pedido.get_ready()): 
                code = pedido.get_code().zfill(6)
                date = pedido.get_date()
                usuario = pedido.get_usuario().get_name()
                chef = pedido.get_chef()
                if chef:
                    chef = pedido.get_chef().get_name()
                else:
                    chef = ''
                ready = pedido.get_ready()
                if ready:
                    ready = EN.men.get('yes')
                else:
                    ready = EN.men.get('no')
                Str += EN.men.get('str_see_pedido') % (
                        code, date, ready, usuario, chef)
        return Str

    @staticmethod
    def see_take_pedido(chef):
        Str = EN.men.get('str_see_pedido_header')
        
        for pedido in chef.get_pedidos_chef().values():
            if not pedido.get_ready(): 
                code = pedido.get_code().zfill(6)
                date = pedido.get_date()
                usuario = pedido.get_usuario().get_name()
                chef = pedido.get_chef()
                if chef:
                    chef = pedido.get_chef().get_name()
                else:
                    chef = ''
                ready = pedido.get_ready()
                if ready:
                    ready = EN.men.get('yes')
                else:
                    ready = EN.men.get('no')
                Str += EN.men.get('str_see_pedido') % (
                        code, date, ready, usuario, chef)
        return Str
    
    @staticmethod
    def see_my_pedido(user):
        Str = EN.men.get('str_see_pedido_header')
        
        for pedido in user.get_pedidos().values():
            code = pedido.get_code().zfill(6)
            date = pedido.get_date()
            usuario = pedido.get_usuario().get_name()
            chef = pedido.get_chef()
            if chef:
                chef = pedido.get_chef().get_name()
            else:
                chef = ''
            ready = pedido.get_ready()
            if ready:
                ready = EN.men.get('yes')
            else:
                ready = EN.men.get('no')
            Str += EN.men.get('str_see_pedido') % (
                    code, date, ready, usuario, chef)
        return Str
    
    @staticmethod
    def get_pedido_by_code(code):
        return Pedido.ListPedidos.get(code)

    @staticmethod
    def get_pedido_by_date(date):
        ListCoincidencias = []
        for pedido in Pedido.ListPedidos.values():
            if pedido.get_date().find(date) != -1:
                ListCoincidencias.append(pedido)
        return ListCoincidencias
        