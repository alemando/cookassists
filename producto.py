from mensajes import Mensajes

class Producto:

    ListProductos = []
    auto_increment_codigo = 0

    def __init__(
        self, nombre, categoria, cantidad,
        necesario, medicion, ilimitado, descontinuado = False):
        '''ATTRIBUTES
            self._ListDetallePedidos
            self._ListDetalleRecetas
            self._codigo
            self._nombre
            self._cantidad
            self._categoria
            self._medicion
            self._necesario
            self._ilimitado
            self._descontinuado
        '''
        self._ListDetallePedidos = []
        self._ListDetalleRecetas = []
        self.set_codigo()
        self.set_nombre(nombre)
        self.set_categoria(categoria)
        self.set_cantidad(cantidad)
        self.set_necesario(necesario)
        self.set_medicion(medicion)
        self.set_ilimitado(ilimitado)
        self.set_descontinuado(descontinuado)
        Producto.ListProductos.append(self)
    #codigo al ya estar creado
    def set_codigo(self):
        codigo = Producto.get_proximo_codigo()
        self._codigo = str(codigo)

    def get_codigo(self):
        return self._codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_nombre(self):
        return self._nombre

    def set_categoria(self, categoria):
        if categoria == "1":
            categoria = "Basicos"
        elif categoria == "2":
            categoria = "Pastas"
        elif categoria == "3":
            categoria = "Liquidos"
        elif categoria == "4":
            categoria = "Snacks"
        elif categoria == "5":
            categoria = "Bebidas"
        self._categoria = categoria

    def get_categoria(self):
        return self._categoria

    def set_cantidad(self, cantidad):
        self._cantidad = int(cantidad)

    def get_cantidad(self):
        if self.get_ilimitado():
            return "Ilimitado"
        else:
            return self._cantidad

    def set_necesario(self, necesario):
        if necesario == '1':
            necesario = True
        else:
            necesario = False
        self._necesario = necesario

    def get_necesario(self):
        return self._necesario

    def set_medicion(self, medicion):
        if medicion == '1':
            medicion = 'N/A'
        elif medicion == '2':
            medicion = 'ml'
        elif medicion == "3":
            medicion = 'gr'
        self._medicion = medicion

    def get_medicion(self):
        if self._medicion == 'N/A':
            return ''
        else:
            return self._medicion

    def set_ilimitado(self, ilimitado):
        if ilimitado == '1':
            ilimitado = True
        else:
            ilimitado = False
        self._ilimitado = ilimitado

    def get_ilimitado(self):
        return self._ilimitado

    def set_descontinuado(self, descontinuado):
        if descontinuado == '1':
            descontinuado = True
        else:
            descontinuado = False
        self._descontinuado = descontinuado

    def get_descontinuado(self):
        return self._descontinuado

    def set_detalle_pedidos(self, detalle_pedido):
        self._ListDetallePedidos.append(detalle_pedido)

    def get_detalle_pedidos(self):
        return self._ListDetallePedidos

    def set_detalle_recetas(self, receta):
        self._ListDetalleRecetas.append(receta)

    def get_detalle_recetas(self):
        return self._ListDetalleRecetas

    def editar_producto(self, opcion, valor):
        if opcion == '1':
            self.set_nombre(valor)
        elif opcion == '2':
            self.set_categoria(valor)
        elif opcion == '3':
            self.set_cantidad(valor)
        elif opcion == '4':
            self.set_necesario(valor)
        elif opcion == '5':
            self.set_medicion(valor)
        elif opcion == '6':
            self.set_ilimitado(valor)

    @staticmethod
    def get_proximo_codigo():
        Producto.auto_increment_codigo += 1
        return Producto.auto_increment_codigo
        
    def toString(self):
        codigo = self.get_codigo() 
        nombre = self.get_nombre()
        categoria = self.get_categoria()
        cantidad = str(self.get_cantidad())
        medicion = self.get_medicion()
        necesario = self.get_necesario()
        if necesario :
            necesario = "Si"
        else:
            necesario = "No"
        Str = Mensajes.men.get('formatoProducto') % (
            codigo, nombre, categoria,
            cantidad, medicion, necesario)
        return Str

    @staticmethod
    def get_producto_by_codigo(codigo):
        for producto in Producto.ListProductos:
            if producto.get_codigo() == codigo:
                return producto
        return None

    @staticmethod
    def get_producto_by_nombre(nombre):
        ListCoincidencias = []
        for producto in Producto.ListProductos:
            if producto.get_nombre().find(nombre) != -1:
                ListCoincidencias.append(producto)
        return ListCoincidencias
'''
    @staticmethod
    def get_posicion_lista(codigo):
        for i in range(0,len(Producto.ListProductos)):
            if Producto.ListProductos[i].get_codigo() == codigo:
                return i
                break
        return -1

    @staticmethod
    def delete_element(codigo):
        posicion = Producto.get_posicion(codigo) 
        Producto.ListProductos.pop(posicion)
'''