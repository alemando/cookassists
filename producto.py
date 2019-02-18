from languageEN import EN
class Producto:

    ListProductos = {}
    auto_increment_code = 0

    def __init__(
        self, name, quantity,
        important, measurement, unlimited):
        '''ATTRIBUTES
            self._code
            self._name
            self._quantity
            self._measurement
            self._important
            self._unlimited
            self._status
        '''
        self._ListDetallePedidos = {}
        self._ListDetalleRecetas = {}
        self.set_code()
        self.set_name(name)
        self.set_quantity(quantity)
        self.set_important(important)
        self.set_measurement(measurement)
        self.set_unlimited(unlimited)
        self.set_status(True)
        Producto.ListProductos[self.get_code()] = self

    #codigo al ya estar creado
    def set_code(self):
        Producto.auto_increment_code += 1
        code = Producto.auto_increment_code
        self._code = str(code)

    def get_code(self):
        return self._code

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_quantity(self, quantity):
        self._quantity = int(quantity)

    def get_quantity(self):
        return self._quantity

    def set_important(self, important):
        self._important = important

    def get_important(self):
        return self._important

    def set_measurement(self, measurement):
        self._measurement = measurement

    def get_measurement(self):
        if self._measurement == 'N/A':
            return ''
        else:
            return self._measurement

    def set_unlimited(self, unlimited):
        self._unlimited = unlimited

    def get_unlimited(self):
        return self._unlimited

    def set_status(self, status):
        self._status = status
        if not status:
            for detalle in self.get_detalle_recetas.values():
                receta = detalle.get_receta()
                receta.set_status(False)
            
    def get_status(self):
        return self._status

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos[detalle_pedido.get_codigo()] = detalle_pedido

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_detalle_recetas(self, receta):
        self._ListDetalleRecetas[receta.get_codigo()] = receta

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas

    def change_quantity(self, quantity, operator):
        if operator == '+':
            self._quantity += quantity 
        else:
            self._quantity -= quantity

    def __str__(self):
        code = self.get_code() 
        name = self.get_name()
        quantity = str(self.get_quantity())
        if self.get_unlimited:
            quantity = EN.men.get('text_unlimited')
        measurement = self.get_measurement()
        important = self.get_important()
        if important :
            important = EN.men.get('yes')
        else:
            important = EN.men.get('no')
        status = self.get_status()
        if status:
            status = EN.men.get('active')
        else:
            status = EN.men.get('inactive')
        Str = EN.men.get('producto_pattern') % (
            code, name, quantity, measurement, 
            important, status)
        return Str
    
    def str_user(self):
        code = self.get_code() 
        name = self.get_name()
        Str = EN.men.get('producto_pattern_user') % (
            code, name)
        return Str

    '''Atributo admin para listar los productos 
        que estan desactivados
    '''
    @staticmethod
    def get_producto_by_code(code, admin):
        producto = Producto.ListProductos.get(code)
        if producto:
            if producto.get_status() or admin:
                return producto
        return None

    @staticmethod
    def get_producto_by_name(name, admin):
        ListCoincidencias = []
        for producto in Producto.ListProductos.values():
            if producto.get_name().lower().find(name.lower()) != -1:
                if producto.get_status() or admin:
                    ListCoincidencias.append(producto)
        return ListCoincidencias