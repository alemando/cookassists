from languageEN import EN
class Producto:

    ListProductos = {}
    menu = {}
    auto_increment_code = 0

    def __init__(
        self, name, quantity, measurement, 
        code = None, status = True, status_menu = False):
        '''ATTRIBUTES
            self._code
            self._name
            self._quantity
            self._measurement

            self._status
            selg._status_menu
        '''
        self._ListDetallePedidos = {}
        self._ListDetalleRecetas = {}
        self.set_code(code)
        self.set_name(name)
        self.set_quantity(quantity)
        self.set_measurement(measurement)
        self.set_status(status)
        self.set_status_menu(status_menu)
        Producto.ListProductos[self.get_code()] = self

    def set_code(self, code):
        aux_code = Producto.auto_increment_code
        if code:
            if code > aux_code:
                Producto.auto_increment_code = code
        else:
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

    def set_measurement(self, measurement):
        self._measurement = measurement

    def get_measurement(self):
        if self._measurement == 'N/A':
            return ''
        else:
            return self._measurement

    def set_status(self, status):
        self._status = status
        if not status:
            for detalle in self.get_detalle_recetas().values():
                receta = detalle.get_receta()
                receta.set_status_menu(False)
            
    def get_status(self):
        return self._status

    def set_status_menu(self, status):
        if status:
            Producto.menu[self.get_code()] = self
        else:
            Producto.menu.pop(self.get_code(), 'error')
        self._status_menu = status
            
    def get_status_menu(self):
        return self._status_menu

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos[detalle_pedido.get_code()] = detalle_pedido

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_detalle_recetas(self, receta):
        self._ListDetalleRecetas[receta.get_code()] = receta

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas

    def change_quantity(self, quantity, operator):
        if operator == '+':
            self._quantity += quantity 
        else:
            self._quantity -= quantity

    def check_quantity(self, quantity):
        producto_quantity = self.get_quantity()
        return producto_quantity // quantity

    def check_producto(self, quantity):
        num_times = self.get_quantity()
        if num_times >= quantity:
            return True
        elif num_times == 0:
            Producto.menu.pop(self.get_code())
            return EN.men.get('sorry_producto')
        else:
            return EN.men.get('only_unity') % (num_times)

    def __str__(self):
        code = self.get_code() 
        name = self.get_name()
        quantity = str(self.get_quantity())
        measurement = self.get_measurement()
        status = self.get_status()
        if status:
            status = EN.men.get('active')
        else:
            status = EN.men.get('inactive')
        status_menu = self.get_status_menu()
        if status_menu:
            status_menu = EN.men.get('active')
        else:
            status_menu = EN.men.get('inactive')

        Str = EN.men.get('producto_pattern') % (
            code, name, quantity, 
            measurement, status, status_menu)
        return Str
    
    @staticmethod
    def see_low_producto():
        Str = EN.men.get('str_see_low_producto_header')
        for producto in Producto.ListProductos.values():
            code = producto.get_code().zfill(6)
            name = producto.get_name()
            quantity = producto.get_quantity()
            measurement = producto.get_measurement()
            if (measurement == 'gr' or measurement == 'ml') and quantity <1000:
                Str += EN.men.get('str_see_low_producto') % (
                    code, name, quantity, measurement)
            elif measurement =='' and quantity < 10:
                Str += EN.men.get('str_see_low_producto') % (
                    code, name, quantity, measurement)
        return Str

    @staticmethod
    def see_producto():
        Str = EN.men.get('str_see_producto_header')
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
    def see_menu():
        Str = EN.men.get('str_menu_producto_header')
        for producto in Producto.menu.values():
            code = producto.get_code().zfill(6)
            name = producto.get_name()
            Str += EN.men.get('str_menu_producto') % (
                    code, name)
        return Str


    '''Atributo admin para listar los productos 
        que estan desactivados
    '''
    @staticmethod
    def get_producto_by_code(code):
        return Producto.ListProductos.get(code)

    @staticmethod
    def get_producto_by_name(name):
        ListCoincidencias = []
        for producto in Producto.ListProductos.values():
            if producto.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(producto)
        return ListCoincidencias

    @staticmethod
    def get_producto_by_code_menu(code):
        return Producto.menu.get(code)

    @staticmethod
    def get_producto_by_name_menu(name):
        ListCoincidencias = []
        for producto in Producto.menu.values():
            if producto.get_name().lower().find(name.lower()) != -1:
                ListCoincidencias.append(producto)
        return ListCoincidencias