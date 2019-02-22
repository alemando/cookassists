from detalleReceta import DetalleReceta
from languageEN import EN
class Receta:

    ListRecetas = {}
    menu = {}
    auto_increment_code = 0

    def __init__(
        self, name, 
        time, detalle_receta, code = None, status_menu = False):
        '''ATTRIBUTES
            self._code
            self._name
            self._time
            self._status_menu
        '''
        self._ListDetalleRecetas = {}
        self._ListDetallePedidos = {}
        self._ListCalificaciones = {}
        self.set_code(code)
        self.set_name(name)
        self.set_time(time)
        self.set_status_menu(status_menu)
        for detalle in detalle_receta:
            DetalleReceta(detalle.get('quantity'), detalle.get('producto'), self)
        Receta.ListRecetas[self.get_code()] = self

    def set_code(self, code):
        aux_code = Receta.auto_increment_code
        if code:
            if code > aux_code:
                Receta.auto_increment_code = code
        else:
            Receta.auto_increment_code += 1
            code = Receta.auto_increment_code
        self._code = str(code)

    def get_code(self):
        return self._code

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_time(self, time):
        self._time = int(time)

    def get_time(self):
        return self._time

    def set_status_menu(self, status):
        if status:
            Receta.menu[self.get_code()] = self
        else:
            Receta.menu.pop(self.get_code())
        self._status_menu = status
            
    def get_status_menu(self):
        return self._status_menu

    def set_detalle_recetas(self, detalle_receta):
        self._ListDetalleRecetas[detalle_receta.get_code()] = detalle_receta

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos[detalle_pedido.get_code()] = detalle_pedido

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_calificaciones(self, calificacion):
        self._ListCalificaciones[calificacion.get_code()] = calificacion

    def get_calificaciones(self):
        return self._ListCalificaciones
    
    def change_quantity_to_producto(self, quantity, operator):
        for detalle in self.get_detalle_recetas().values():
            producto = detalle.get_producto()
            quantity_producto = detalle.get_quantity()*quantity
            producto.change_quantity(quantity_producto, operator)

    def check_receta(self, quantity):
        num_times = quantity
        for detalle in self.get_detalle_recetas().values():
            receta_times = detalle.get_producto().check_quantity(detalle.get_quantity())
            if receta_times < num_times:
                num_times = receta_times
        if num_times >= quantity:
            return True
        elif num_times == 0:
            Receta.menu.pop(self.get_code())
            return EN.men.get('sorry_receta')
        else:
            return EN.men.get('only_unity') % (num_times)

    def add_more_detalle_recetas(self, detalle_receta):
        for detalle in detalle_receta:
            DetalleReceta(detalle.get('quantity'), detalle.get('producto'), self)
    
    def see_calificacion(self):
        code = self.get_code()
        name = self.get_name()
        time = self.get_time()
        status = self.get_status_menu()
        Str = EN.men.get('receta_pattern') % (
            code, name,
            time, status)
        for calificacion in self.get_calificaciones().values():
            Str+= calificacion.__str__()
        return Str

    def str_user(self):
        code = self.get_code()
        name = self.get_name()
        Str = EN.men.get('receta_pattern_user') % (
            code, name)
        return Str


    def __str__(self):
        code = self.get_code()
        name = self.get_name()
        time = self.get_time()
        status = self.get_status_menu()
        Str = EN.men.get('receta_pattern') % (
            code, name,
            time, status)
        Str+= EN.men.get('detalle_receta_pattern_header')
        for detalle in self.get_detalle_recetas().values():
            Str+= detalle.__str__()
        return Str

    @staticmethod
    def see_receta():
        Str = EN.men.get('str_see_receta_header')
        for receta in Receta.ListRecetas.values():
            code = receta.get_code().zfill(6)
            name = receta.get_name()
            time = receta.get_time()
            status_menu = receta.get_status_menu()
            if status_menu:
                status_menu = EN.men.get('active')
            else:
                status_menu = EN.men.get('inactive')
            Str += EN.men.get('str_see_receta') % (
                    code, name, time, status_menu)
        return Str

    @staticmethod
    def see_menu():
        Str = EN.men.get('str_menu_receta_header')
        for receta in Receta.menu.values():
            code = receta.get_code().zfill(6)
            name = receta.get_name()
            time = receta.get_time()
            Str += EN.men.get('str_menu_receta') % (
                    code, name, time)
        return Str

    @staticmethod
    def get_receta_by_code(code):
        return Receta.ListRecetas.get(code)
    
    @staticmethod
    def get_receta_by_name(name):
        ListCoincidencias = []
        for receta in Receta.ListRecetas.values():
            if receta.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(receta)
        return ListCoincidencias

    @staticmethod
    def get_receta_by_code_menu(code):
        return Receta.menu.get(code)
    
    @staticmethod
    def get_receta_by_name_menu(name):
        ListCoincidencias = []
        for receta in Receta.menu.values():
            if receta.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(receta)
        return ListCoincidencias