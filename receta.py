from detalleReceta import DetalleReceta
from languageEN import EN
class Receta:

    ListRecetas = {}
    auto_increment_code = 0

    def __init__(
        self, name, 
        time, detalle_receta):
        '''ATTRIBUTES
            self._code
            self._name
            self._time
            self._status
        '''
        self._ListDetalleRecetas = {}
        self._ListDetallePedidos = {}
        self._ListCalificaciones = {}
        self.set_code()
        self.set_name(name)
        self.set_time(time)
        self.set_status(False)
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

    def set_status(self, status):
        self._status = status
            
    def get_status(self):
        return self._status

    def set_detalle_recetas(self, detalle_receta):
        self._ListDetalleRecetas[detalle_receta.get_codigo()] = detalle_receta

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos[detalle_pedido.get_codigo()] = detalle_pedido

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_calificaciones(self, calificacion):
        self._ListCalificaciones[calificacion.get_codigo()] = calificacion

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
    def get_receta_by_code(code):
        return Receta.ListRecetas.get(code)
    
    @staticmethod
    def get_receta_by_name(name):
        ListCoincidencias = []
        for receta in Receta.ListRecetas.values():
            if receta.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(receta)
        return ListCoincidencias