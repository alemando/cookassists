import os

from mensajes import Mensajes
from datos import Datos
#from usuario import Usuario
#from calificacion import Calificacion
#from Receta import Receta
from producto import Producto


class CookAssist:
    
    def __init__(self):
        pass

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
            '8': CookAssist.salir
        }
        return menu.get(opcion)

    @staticmethod
    def menu_usuario(opcion):
        menu_usuario = {
            '1': CookAssist.ver_usuario,
            '2': CookAssist.crear_usuario,
            '3': CookAssist.editar_usuario,
            '4': CookAssist.eliminar_usuario
        }
        return menu_usuario.get(opcion)

    @staticmethod
    def menu_chef(opcion):
        menu_chef = {
            '1': CookAssist.ver_chef,
            '2': CookAssist.agregar_chef,
            '3': CookAssist.editar_chef,
            '4': CookAssist.eliminar_chef
        }
        return menu_chef.get(opcion)

    @staticmethod
    def menu_calificacion(opcion):
        menu_calificacion = {
            '1': CookAssist.ver_calificacion,
            '2': CookAssist.agregar_calificacion,
            '3': CookAssist.editar_calificacion,
            '4': CookAssist.eliminar_calificacion
        }
        return menu_calificacion.get(opcion)

    @staticmethod
    def menu_datos(opcion):
        menu_datos = {
            '1': CookAssist.agregar_datos_ficticios
        }
        return menu_datos.get(opcion)

    @staticmethod
    def menu_idioma(opcion):
        menu_idioma = {
            '1': CookAssist.cambiar_idioma
        }
        return menu_idioma.get(opcion)

    '''if imprimir is True print a string
        if not return a string
    '''
    @staticmethod
    def mensaje(opcion, imprimir=True):
        if imprimir:
            print(Mensajes.men.get(opcion))
        else:
            return Mensajes.men.get(opcion)
        

    @staticmethod
    def cambiar_idioma():
        opcion = input(Mensajes.texto_idioma)
        if opcion == '1':
            Mensajes.men = Mensajes.espanol
        elif opcion == '2':
            Mensajes.men = Mensajes.ingles
        else:
            print(CookAssist.mensaje('opcionNoValida', False).format(opcion))

    @staticmethod
    def salir():
        CookAssist.mensaje('salir')
        os._exit(0)

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
                    
    @staticmethod
    def eliminar_usuario():
        pass
        '''
        id = int(input(CookAssist.mensaje('id', False)))
        pos = Usuario.get_posicion_lista(id)
        opcion = input(CookAssist.mensaje('yesNo', False))
        if opcion == '1':
            Usuario.delete_element(pos)
        '''
    
    #TODO: CHEF METODOS
    @staticmethod
    def ver_chef():
        pass

    @staticmethod
    def agregar_chef():
        pass

    @staticmethod
    def editar_chef():
        pass

    @staticmethod
    def eliminar_chef():
        pass

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
    def eliminar_calificacion():
        pass

    @staticmethod
    def agregar_datos_ficticios():
        Datos.generarProductos()
        
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
        pass
        '''
        CookAssist.mensaje('opcionesVerReceta')
        opcion = input(CookAssist.mensaje('opcion', False))
        if opcion == '1':
            pass    
        elif opcion == '2':
            pass
        '''

    @staticmethod
    def agregar_receta():
        pass
        '''
        nombre = input(CookAssist.mensaje('nombre', False))
        tiempo_preparacion = int(input(CookAssist.mensaje('tiempo', False)))
        receta = Receta(nombre, tiempo_preparacion)
        CookAssist.mensaje('opcionesDetalleReceta')
        opcion = input(CookAssist.mensaje('opcion', False))
        '''
    
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
                print(producto.toString())
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
                    numero = str(i+1)
                    print(numero +' '+ producto[i].get_codigo().zfill(6) +' '+ producto[i].get_nombre())
                opcion = int(input(CookAssist.mensaje('opcion', False)))
                print(producto[(opcion-1)].toString())
                return producto
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

    @staticmethod
    def run():

        Mensajes.men = Mensajes.espanol

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
                print (action)
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
