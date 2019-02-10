import os
from languageEN import EN
from languageES import ES
from datos import Datos
#from usuario import Usuario
#from calificacion import Calificacion
#from pedido import Pedido
from receta import Receta
from producto import Producto

class CookAssist:
    

    @staticmethod
    def menu(opcion):
        menu = {
            '1': CookAssist.menu_usuario,
            '2': CookAssist.menu_chef,
            '3': CookAssist.menu_calificacion,
            '4': CookAssist.menu_datos,
            '5': CookAssist.menu_idioma,
            '6': CookAssist.menu_receta,
            '7': CookAssist.menu_producto,
            '8': CookAssist.menu_pedido,
            '9': CookAssist.salir
        }
        return menu.get(opcion)

    @staticmethod
    def menu_idioma(opcion):
        menu_idioma = {
            '1': CookAssist.cambiar_idioma
        }
        return menu_idioma.get(opcion)

    @staticmethod
    def cambiar_idioma():
        opcion = input(CookAssist.mensaje('language', False))
        if opcion == '1':
            EN.men = ES.spanish
        elif opcion == '2':
            EN.men = EN.english
        else:
            print(CookAssist.mensaje('opcionNoValida', False).format(opcion))
    
    @staticmethod
    def menu_datos(opcion):
        menu_datos = {
            '1': CookAssist.agregar_datos_ficticios
        }
        return menu_datos.get(opcion)

    @staticmethod
    def agregar_datos_ficticios():
        Datos.generarProductos()

    '''if imprimir is True print a string
        if not return a string
    '''
    @staticmethod
    def mensaje(opcion, imprimir=True):
        if imprimir:
            print(EN.men.get(opcion))
        else:
            return EN.men.get(opcion)
    
    @staticmethod
    def salir():
        CookAssist.mensaje('salir')
        os._exit(0)
    
    #Producto
    @staticmethod
    def menu_producto(opcion):
        menu_producto = {
            '1': CookAssist.ver_producto,
            '2': CookAssist.agregar_producto,
            '3': CookAssist.editar_producto
        }
        return menu_producto.get(opcion)
    
    @staticmethod
    def ver_producto():
        CookAssist.mensaje('ver_producto')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo', False))
            producto = Producto.get_producto_by_codigo(codigo)
            if producto is not None:
                print(producto)
                return producto
            else:
                CookAssist.mensaje('codeNotFound')
                return None
            
        elif opcion == '2':
            nombre = input(CookAssist.mensaje('nombre', False))
            producto = Producto.get_producto_by_nombre(nombre)
            if len(producto) != 0:
                CookAssist.mensaje('opcionesProducto')
                for i in range(len(producto)):
                    numero = str(i + 1)
                    print(numero +' '+ producto[i].get_codigo().zfill(6) +' '+ producto[i].get_nombre())
                opcion = int(input(CookAssist.mensaje('opcion', False)))
                print(producto[(opcion-1)])
                return producto[(opcion-1)]
            else:
                CookAssist.mensaje('notMatch')


    @staticmethod
    def agregar_producto():
        nombre = input(CookAssist.mensaje('nombre', False))
        categoria = input(CookAssist.mensaje('categoria', False))
        cantidad = input(CookAssist.mensaje('cantidad', False))
        necesario = input(CookAssist.mensaje('necesario', False))
        medicion = input(CookAssist.mensaje('medicion', False))
        ilimitado = input(CookAssist.mensaje('ilimitado', False))
        Producto(nombre, categoria, cantidad, necesario, medicion, ilimitado)

    @staticmethod
    def editar_producto():
        producto = CookAssist.ver_producto()
        if producto is not None:
            CookAssist.mensaje('editar_producto')
            opcion = input(CookAssist.mensaje('opcion', False))
            valor = None
            if opcion == '1':
                valor = input(CookAssist.mensaje('nombre', False))
            elif opcion == '2':
                valor = input(CookAssist.mensaje('categoria', False))
            elif opcion == '3':
                valor = input(CookAssist.mensaje('cantidad', False))
            elif opcion == '4':
                valor = input(CookAssist.mensaje('necesario', False))
            elif opcion == '5':
                valor = input(CookAssist.mensaje('medicion', False))
            elif opcion == '6':
                valor = input(CookAssist.mensaje('ilimitado', False))
            if opcion != '7':
                producto.editar_producto(opcion, valor)

    #Receta
    @staticmethod
    def menu_receta(opcion):
        menu_receta = {
            '1': CookAssist.ver_receta,
            '2': CookAssist.agregar_receta,
            '3': CookAssist.editar_receta,
        }
        return menu_receta.get(opcion)

    @staticmethod
    def ver_receta():
        CookAssist.mensaje('ver_receta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            codigo = input(CookAssist.mensaje('codigo', False))
            receta = Receta.get_receta_by_codigo(codigo)
            if receta is not None:
                print(receta)
                return receta
            else:
                CookAssist.mensaje('codeNotFound')
                return None
            
        elif opcion == '2':
            nombre = input(CookAssist.mensaje('nombre', False))
            receta = Receta.get_producto_by_nombre(nombre)
            if len(receta) != 0:
                CookAssist.mensaje('opcionesReceta')
                for i in range(len(receta)):
                    numero = str(i + 1)
                    print(numero +' '+ receta[i].get_codigo().zfill(6) +' '+ receta[i].get_nombre())
                opcion = int(input(CookAssist.mensaje('opcion', False)))
                print(receta[(opcion-1)])
                return receta[(opcion-1)]
            else:
                CookAssist.mensaje('notMatch')

    @staticmethod
    def agregar_receta():
        nombre = input(CookAssist.mensaje('nombre', False))
        tiempo_preparacion = int(input(CookAssist.mensaje('tiempo', False)))
        detalle = CookAssist.agregar_detalle_receta()
        receta = Receta(nombre, tiempo_preparacion, detalle)
    
    @staticmethod
    def editar_receta():
        receta = CookAssist.ver_receta()
        if receta is not None:
            CookAssist.mensaje('editar_receta')
            opcion = input(CookAssist.mensaje('opcion', False))
            valor = None
            if opcion == '1':
                valor = input(CookAssist.mensaje('nombre', False))
            elif opcion == '2':
                valor = input(CookAssist.mensaje('tiempo', False))
            elif opcion == '3':
                valor = CookAssist.agregar_detalle_receta()
            elif opcion == '4':
                codigo = input(CookAssist.mensaje('codigo', False))
                cantidad = input(CookAssist.mensaje('cantidad', False))
                valor = {'codigo' : codigo, 'cantidad' : cantidad}
            elif opcion == '5':
                valor = input(CookAssist.mensaje('codigo', False))
            if opcion != '6':
                receta.editar_receta(opcion, valor)
    
    @staticmethod
    def agregar_detalle_receta():
        CookAssist.mensaje('detalleReceta')
        opcion = input(CookAssist.mensaje('opcion', False))
        detalle = []
        while opcion != '4':
            if opcion == '1':
                producto = CookAssist.ver_producto()
                if producto is not None:
                    cantidad = input(CookAssist.mensaje('cantidad', False))
                    detalle.append({'cantidad' : cantidad, 'producto' : producto})
            elif opcion == '2':
                CookAssist.mensaje('cabeceraDetalle', False)
                for i in range(len(detalle)):
                    numero = str(i + 1)
                    print(numero +' '+ detalle[i].get('cantidad').zfill(7) 
                            +' '+ detalle[i].get('producto').get_nombre())
                opcionDetalle = int(input(CookAssist.mensaje('opcion', False)))
                cantidad = input(CookAssist.mensaje('cantidad', False))
                detalle[opcionDetalle-1]['cantidad'] = cantidad
            elif opcion == '3':
                for i in range(len(detalle)):
                    numero = str(i + 1)
                    print(numero +' '+ detalle[i].get('cantidad').zfill(7) 
                            +' '+ detalle[i].get('producto').get_nombre())
                posicionDetalle = int(input(CookAssist.mensaje('opcion', False)))
                detalle.pop(posicionDetalle-1)
            
            CookAssist.mensaje('detalleReceta')
            opcion = input(CookAssist.mensaje('opcion', False))
        return detalle
    #Pedido
    @staticmethod
    def menu_pedido(opcion):
        menu_pedido = {
            '1': CookAssist.ver_pedido,
            '2': CookAssist.crear_pedido,
            '3': CookAssist.editar_pedido,
        }
        return menu_pedido.get(opcion)

    @staticmethod
    def ver_pedido():
        pass

    @staticmethod
    def crear_pedido():
        pass

    @staticmethod
    def editar_pedido():
        pass

    #Usuario
    @staticmethod
    def menu_usuario(opcion):
        menu_usuario = {
            '1': CookAssist.ver_usuario,
            '2': CookAssist.crear_usuario,
            '3': CookAssist.editar_usuario,
        }
        return menu_usuario.get(opcion)

    @staticmethod
    def ver_usuario():
        pass
        '''
        id = int(input(CookAssist.mensaje('id', False)))
        user = Usuario.get_usuario_by_identificacion(id)
        if user is not None:
            print(user.toString())
            return user
        else:
            CookAssist.mensaje('userNotFound')
            return None
            '''


    @staticmethod
    def crear_usuario():
        pass
        '''
        #TODO: Tipo usuario
        user_type = 'cliente'
        nombre = input(CookAssist.mensaje('nombre', False))
        id = int(input(CookAssist.mensaje('id', False)))
        while not Usuario.verificar_identificacion(id):
            CookAssist.mensaje('idFound', False)
            id = input(CookAssist.mensaje('id', False))
        fecha_nac = input(CookAssist.mensaje('fecha_nac', False))
        contrasena = input(CookAssist.mensaje('contrasena', False))
        Usuario(user_type, nombre, id, fecha_nac, contrasena)
        '''

    @staticmethod
    def editar_usuario():
        pass
        '''
        #TODO: Cambiar tipo usuario
        user = CookAssist.ver_usuario()
        CookAssist.mensaje('editar_usuario')
        opcion = input(CookAssist.mensaje('opcion', False))
        while opcion is not '4':
            if opcion is '1':
                nombre = input(CookAssist.mensaje('nombre', False))
                user.set_nombre(nombre)
            elif opcion is '2':
                fecha_nac = input(CookAssist.mensaje('fecha_nac', False))
                user.set_fecha_nacimiento(fecha_nac)
            elif opcion is '3':
                vieja_contrasena = input(CookAssist.mensaje('oldContrasena', False))
                nueva_contrasena =  input(CookAssist.mensaje('newContrasena', False))
                if vieja_contrasena == user.get_contrasena():
                    user.set_contrasena = nueva_contrasena
                else:
                    CookAssist.mensaje('wrongContrasena')
            CookAssist.mensaje('editar_usuario')
            opcion = input(CookAssist.mensaje('opcion', False))
        '''

    #Chef
    @staticmethod
    def menu_chef(opcion):
        menu_chef = {
            '1': CookAssist.ver_chef,
            '2': CookAssist.agregar_chef,
            '3': CookAssist.editar_chef,
        }
        return menu_chef.get(opcion)

    @staticmethod
    def ver_chef():
        pass

    @staticmethod
    def agregar_chef():
        pass

    @staticmethod
    def editar_chef():
        pass

    #Calificacion
    @staticmethod
    def menu_calificacion(opcion):
        menu_calificacion = {
            '1': CookAssist.ver_calificacion,
            '2': CookAssist.agregar_calificacion,
            '3': CookAssist.editar_calificacion,
        }
        return menu_calificacion.get(opcion)

    @staticmethod
    def ver_calificacion():
        pass

    @staticmethod
    def agregar_calificacion():
        pass

    @staticmethod
    def editar_calificacion():
        pass

    @staticmethod
    def run():

        EN.men = ES.spanish

        while True:
            CookAssist.mensaje('menu')
            opcion_principal = input(CookAssist.mensaje('opcion', False))
            print('')
            action_principal = CookAssist.menu(opcion_principal)
            if action_principal:
                ejecutar = True

                action_string = str(action_principal)
                action_slice_start = action_string.find('.') + 1
                action_slice_last = action_string.index(' ', action_slice_start)
                action = action_string[action_slice_start:action_slice_last]
                if action == 'salir':
                    action_principal()

                while ejecutar:
                    
                    CookAssist.mensaje(action)
                    opcion_menu = input(CookAssist.mensaje('opcion', False))
                    print('')
                    action_menu = action_principal(opcion_menu)
                    if action_menu:
                        action_menu()
                    else:
                        ejecutar = False
                    
                    
            else:
                print(CookAssist.mensaje('opcionNoValida', False).format(opcion))
            

if __name__ == '__main__':
    CookAssist.run()
