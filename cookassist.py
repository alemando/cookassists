import os
from languageEN import EN
from languageES import ES
from datos import Datos
from usuario import Usuario
from chef import Chef
#from calificacion import Calificacion
from pedido import Pedido
from receta import Receta
from producto import Producto

class CookAssist:
    #cambia si es chef o usuario
    user = None

    @staticmethod
    def enter():
        option = input(CookAssist.mensaje('enter', False))
        menu = {
            '1': CookAssist.login,
            '2': CookAssist.new_user,
            '3': CookAssist.close
        }
        menu.get(option)()
        
    @staticmethod
    def main():
        main_action = CookAssist.menu()
        print('')
        if main_action:
            ejecutar = True
            while ejecutar:
                action_menu = main_action()
                print('')
                if action_menu:
                    action_menu()
                else:
                    ejecutar = False
                
        else:
            CookAssist.sign_off()

    @staticmethod
    def menu():
        menu = {}
        option = None
        if isinstance(CookAssist.user, Chef):
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_calificacion,
                '5': CookAssist.menu_usuario,
                '6': CookAssist.menu_language
            }
            option = input(CookAssist.mensaje('menu_main_chef', False))
        
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_calificacion,
                '5': CookAssist.menu_usuario,
                '6': CookAssist.menu_chef,
                '7': CookAssist.menu_language,
                '8': CookAssist.menu_data
            }
            option = input(CookAssist.mensaje('menu_main_admin', False))
        else:
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_calificacion,
                '5': CookAssist.menu_usuario,
                '6': CookAssist.menu_language
                
            }
            option = input(CookAssist.mensaje('menu_main_user', False))
        
        return menu.get(option)


    @staticmethod
    def menu_language():
        option = input(CookAssist.mensaje('menu_language', False))
        menu = {
            '1': CookAssist.change_language
        }
        return menu.get(option)

    @staticmethod
    def change_language():
        option = input(CookAssist.mensaje('language', False))
        if option == '1':
            EN.men = ES.spanish
        elif option == '2':
            EN.men = EN.english
        else:
            print(CookAssist.mensaje('opcionNoValida', False).format(opcion))
    
    @staticmethod
    def menu_data():
        option = input(CookAssist.mensaje('menu_data', False))
        menu = {
            '1': CookAssist.add_fictitious_data
        }
        return menu.get(option)

    @staticmethod
    def add_fictitious_data():
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
    def sign_off():
        CookAssist.mensaje('sign_off')
        CookAssist.user = None

    @staticmethod
    def close():
        CookAssist.mensaje('close')
        os._exit(0)

    #Usuario
    @staticmethod
    def menu_usuario():
        menu = {}
        option = None
        if isinstance(CookAssist.user, Chef):
            menu_usuario = {
                '1': CookAssist.edit_my_user,
                '3': CookAssist.change_login_way
            }
            option = input(CookAssist.mensaje('menu_usuario_chef', False))
        elif CookAssist.user.get_admin():
            if Chef.get_chef_by_id(CookAssist.user.get_id_type(), CookAssist.user.get_id()):
                menu_usuario = {
                    '1': CookAssist.search_user,
                    '2': CookAssist.new_user,
                    '3': CookAssist.edit_my_user,
                    '4': CookAssist.edit_user,
                    '5': CookAssist.user_status,
                    '6': CookAssist.change_login_way
                }
                option = input(CookAssist.mensaje('menu_usuario_admin_is_chef', False))
            else:
                menu_usuario = {
                    '1': CookAssist.search_user,
                    '2': CookAssist.new_user,
                    '3': CookAssist.edit_my_user,
                    '4': CookAssist.edit_user,
                    '5': CookAssist.user_status
                }
                option = input(CookAssist.mensaje('menu_usuario_admin', False))
        else:
            if Chef.get_chef_by_id(CookAssist.user.get_id_type(), CookAssist.user.get_id()):
                menu_usuario = {
                    '1': CookAssist.edit_my_user,
                    '2': CookAssist.user_my_status,
                    '3': CookAssist.change_login_way
                }
                option = input(CookAssist.mensaje('menu_usuario_user_is_chef', False))
            else:
                menu_usuario = {
                    '1': CookAssist.edit_my_user,
                    '2': CookAssist.user_my_status
                }
                option = input(CookAssist.mensaje('menu_usuario_user', False))
        
        return menu_usuario.get(opcion)

    @staticmethod
    def login():
        id_type = input(CookAssist.mensaje('id_type', False))
        if id_type == '1':
            id_type = 'CC'
        elif id_type == '2':
            id_type = 'TI'
        id = input(CookAssist.mensaje('id', False))
        password = input(CookAssist.mensaje('password', False))
        CookAssist.user = Usuario.check_login(id_type, id, password)
        if CookAssist.user is None:
            CookAssist.mensaje('user_not_found')

    @staticmethod
    def new_user():
        admin = False
        if CookAssist.user:
            if CookAssist.user.get_admin():
                adm = input(CookAssist.mensaje('admin', False))
                if adm == '1':
                    admin = True
        id_type = input(CookAssist.mensaje('id_type', False))
        if id_type == '1':
            id_type = 'CC'
        elif id_type == '2':
            id_type = 'TI'
        id = input(CookAssist.mensaje('id', False))
        name = input(CookAssist.mensaje('name', False))
        password = input(CookAssist.mensaje('password', False))
        born_date = input(CookAssist.mensaje('born_date', False))
        Usuario(admin, id_type, id, name, password, born_date)
        
    @staticmethod
    def search_user():
        option = input(CookAssist.mensaje('search_user', False))
        if option == '1':
            id_type = input(CookAssist.mensaje('id_type', False))
            if id_type == '1':
                id_type = 'CC'
            elif id_type == '2':
                id_type = 'TI'
            id = input(CookAssist.mensaje('id', False))
            user = Usuario.get_user_by_codigo(id_type, id)
            if user:
                print(user)
                return user
            else:
                CookAssist.mensaje('user_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            users = Usuario.get_user_by_name(name)
            if len(users) != 0:
                CookAssist.mensaje('search_user_header')
                for i in range(len(users)):
                    num = str(i + 1)
                    print(num +' '+ users[i].get_id_type() +'   '+ users[i].get_id() +' '+ users[i].get_name())
                option = int(input(CookAssist.mensaje('option', False)))
                print(users[(option-1)])
                return users[(option-1)]
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def edit_user():
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
            '1': CookAssist.search_chef,
            '2': CookAssist.new_chef,
            '3': CookAssist.edit_chef,
            '3': CookAssist.chef_status
        }
        return menu_chef.get(opcion)

    @staticmethod
    def search_chef():
        pass

    @staticmethod
    def new_chef():
        pass

    @staticmethod
    def edit_chef():
        pass

    @staticmethod
    def chef_status():
        pass


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
        Receta(nombre, tiempo_preparacion, detalle)
    
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
        CookAssist.mensaje('ver_pedido')
        opcion = input(CookAssist.mensaje('opcion', False))
        codigo = input(CookAssist.mensaje('codigo', False))
        pedido = Pedido.get_pedido_by_codigo(codigo)
        if pedido is not None:
            print(pedido)
            return pedido
        else:
            CookAssist.mensaje('codeNotFound')
            return None

    @staticmethod
    def crear_pedido():
        usuario = CookAssist.usuario
        detalle = CookAssist.agregar_detalle_pedido()
        descripcion = input(CookAssist.mensaje('descripcion', False))
        Pedido(usuario, detalle, descripcion)

    @staticmethod
    def editar_pedido():
        pedido = CookAssist.ver_pedido()
        if receta is not None:
            CookAssist.mensaje('editar_pedido')
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
    def agregar_detalle_pedido():
        CookAssist.mensaje('detallePedido')
        opcion = input(CookAssist.mensaje('opcion', False))
        detalle = []
        while opcion != '5':
            if opcion == '1':
                producto = CookAssist.ver_producto()
                if producto is not None:
                    cantidad = input(CookAssist.mensaje('cantidad', False))
                    detalle.append({'cantidad' : cantidad, 'detalle' : producto})
            elif opcion == '2':
                receta = CookAssist.ver_receta()
                if receta is not None:
                    cantidad = input(CookAssist.mensaje('cantidad', False))
                    detalle.append({'cantidad' : cantidad, 'detalle' : receta})
            elif opcion == '3':
                CookAssist.mensaje('cabeceraDetalle', False)
                for i in range(len(detalle)):
                    numero = str(i + 1)
                    print(numero +' '+ detalle[i].get('cantidad').zfill(7) 
                            +' '+ detalle[i].get('detalle').get_nombre())
                opcionDetalle = int(input(CookAssist.mensaje('opcion', False)))
                cantidad = input(CookAssist.mensaje('cantidad', False))
                detalle[opcionDetalle-1]['cantidad'] = cantidad
            elif opcion == '4':
                for i in range(len(detalle)):
                    numero = str(i + 1)
                    print(numero +' '+ detalle[i].get('cantidad').zfill(7) 
                            +' '+ detalle[i].get('detalle').get_nombre())
                posicionDetalle = int(input(CookAssist.mensaje('opcion', False)))
                detalle.pop(posicionDetalle-1)
            
            CookAssist.mensaje('detallePedido')
            opcion = input(CookAssist.mensaje('opcion', False))
        return detalle

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
        Usuario(True, 'CC', '1238938010', 'Alejandro Jiménez', '12345', '28/10/1999')

        while True:

            while CookAssist.user is None:
                CookAssist.enter()

            while CookAssist.user is not None:
                CookAssist.main()
                
            

if __name__ == '__main__':
    CookAssist.run()
