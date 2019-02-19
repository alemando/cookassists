from detalleReceta import DetalleReceta
from languageEN import EN
class Receta:

    ListRecetas = {}
    menu = {}
    auto_increment_code = 0

    def __init__(
        self, name, 
        time, detalle_receta):
        '''ATTRIBUTES
            self._code
            self._name
            self._time
            self._status_menu
        '''
        self._ListDetalleRecetas = {}
        self._ListDetallePedidos = {}
        self._ListCalificaciones = {}
        self.set_code()
        self.set_name(name)
        self.set_time(time)
        self.set_status_menu(False)
        for detalle in detalle_receta:
            DetalleReceta(detalle.get('quantity'), detalle.get('producto'), self)
        Receta.ListRecetas[self.get_code()] = self

    #receta codigo ya creado
    def set_code(self):
        Receta.auto_increment_code += 1
        codigo = Receta.auto_increment_code
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

    def set__status_menu(self, status):
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
        
    def __str__(self):
        code = self.get_code()
        name = self.get_name()
        time = self.get_time()
        status = self.get_status()
        Str = EN.men.get('receta_pattern') % (
            code, name,
            time, status)
        #concatenado el detalle receta
        for detalle in self._ListDetalleRecetas.values():
            Str+= detalle.__str__() + '\n'
        return Str

    @staticmethod
    def see_producto():
        Str = EN.men.get('str_see_receta_header')
        for producto in Producto.ListProductos.values():
            code = producto.get_code().zfill(6)
            name = producto.get_name()
            status = producto.get_status()
            if status:
                status = EN.men.get('active')
            else:
                status = EN.men.get('inactive')
            
            status_menu = producto.get_status_menu()
            if status_menu:
                status_menu = EN.men.get('active')
            else:
                status_menu = EN.men.get('inactive')
            Str += EN.men.get('str_see_producto') % (
                    code, name, status, status_menu)
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