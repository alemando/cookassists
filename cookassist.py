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
    chef = False

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
            while ejecutar and (CookAssist.user is not None):
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
        if CookAssist.chef:
            menu = {
                '1': CookAssist.menu_producto,
                '2': CookAssist.menu_receta,
                '3': CookAssist.menu_pedido,
                '4': CookAssist.menu_chef,
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
                '5': CookAssist.menu_chef,
                '6': CookAssist.menu_usuario,
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
                '5': CookAssist.menu_chef,
                '6': CookAssist.menu_usuario,
                '7': CookAssist.menu_language
                
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
    def mensaje(option, show=True):
        if show:
            print(EN.men.get(option))
        else:
            return EN.men.get(option)
    
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
        if CookAssist.chef:
            menu = {
                '1': CookAssist.edit_my_user,
                '2': CookAssist.change_login_way
            }
            option = input(CookAssist.mensaje('menu_usuario_chef', False))
        elif CookAssist.user.get_admin():
            chef = Chef.get_chef_by_email(CookAssist.user.get_email())
            if chef:
                if chef.get_status_chef():
                    menu = {
                        '1': CookAssist.search_user,
                        '2': CookAssist.new_user,
                        '3': CookAssist.edit_my_user,
                        '4': CookAssist.change_to_admin,
                        '5': CookAssist.user_status,
                        '6': CookAssist.change_login_way
                    }
                    option = input(CookAssist.mensaje('menu_usuario_admin_is_chef', False))
                else:
                    menu = {
                        '1': CookAssist.search_user,
                        '2': CookAssist.new_user,
                        '3': CookAssist.edit_my_user,
                        '4': CookAssist.change_to_admin,
                        '5': CookAssist.user_status
                    }
                    option = input(CookAssist.mensaje('menu_usuario_admin', False))
            else:
                menu = {
                    '1': CookAssist.search_user,
                    '2': CookAssist.new_user,
                    '3': CookAssist.edit_my_user,
                    '4': CookAssist.change_to_admin,
                    '5': CookAssist.user_status
                }
                option = input(CookAssist.mensaje('menu_usuario_admin', False))
        else:
            chef = Chef.get_chef_by_email(CookAssist.user.get_email())
            if chef:
                if chef.get_status_chef():
                    menu = {
                        '1': CookAssist.edit_my_user,
                        '2': CookAssist.user_my_status,
                        '3': CookAssist.change_login_way
                    }
                    option = input(CookAssist.mensaje('menu_usuario_user_is_chef', False))
                else:
                    menu = {
                        '1': CookAssist.edit_my_user,
                        '2': CookAssist.user_my_status
                    }
                    option = input(CookAssist.mensaje('menu_usuario_user', False))
            else:
                menu = {
                    '1': CookAssist.edit_my_user,
                    '2': CookAssist.user_my_status
                }
                option = input(CookAssist.mensaje('menu_usuario_user', False))
        
        return menu.get(option)

    @staticmethod
    def login():
        email = input(CookAssist.mensaje('email', False))
        password = input(CookAssist.mensaje('password', False))
        CookAssist.user = Usuario.check_login(email, password)
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
        email = input(CookAssist.mensaje('email', False))
        name = input(CookAssist.mensaje('name', False))
        password = input(CookAssist.mensaje('password', False))
        born_date = input(CookAssist.mensaje('born_date', False))
        if Usuario.get_user_by_email(email) is None:
            Usuario(admin, email, name, password, born_date)
        else:
            CookAssist.mensaje('user_duplicated')
        
    @staticmethod
    def search_user():
        option = input(CookAssist.mensaje('search_user', False))
        if option == '1':
            email = input(CookAssist.mensaje('email', False))
            user = Usuario.get_user_by_email(email)
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
                    print(num +' '+ users[i].get_email() +' '+ users[i].get_name())
                option = int(input(CookAssist.mensaje('option', False)))
                print(users[(option-1)])
                return users[(option-1)]
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def edit_my_user():
        user = CookAssist.user
        option = input(CookAssist.mensaje('edit_my_user', False))
        value = None
        while option != '4':
            if option == '1':
                name = input(CookAssist.mensaje('name', False))
                user.set_name(name)
            elif option == '2':
                old_password = input(CookAssist.mensaje('old_password', False))
                new_password =  input(CookAssist.mensaje('new_password', False))
                if old_password == user.get_password():
                    password = new_password
                    user.set_password(password)
                else:
                    CookAssist.mensaje('wrong_password')
            elif option == '3':
                born_date = input(CookAssist.mensaje('born_date', False))
                user.set_born_date(born_date)
            option = option = input(CookAssist.mensaje('edit_my_user', False))
        
    @staticmethod
    def change_to_admin():
        user = CookAssist.search_user()
        if user:
            admin = False
            adm = input(CookAssist.mensaje('admin', False))
            if adm == '1':
                admin = True
            user.set_admin(admin)
    
    @staticmethod
    def user_status():
        user = CookAssist.search_user()
        if user:
            status = True
            option = input(CookAssist.mensaje('status', False))
            if option == '2':
                status = False
            user.set_status(status)

    @staticmethod
    def user_my_status():
        user = CookAssist.user
        option = input(CookAssist.mensaje('status_inactive', False))
        if option == '1':
            user.set_status(False)
            CookAssist.sign_off()
    
    @staticmethod
    def change_login_way():
        option = input(CookAssist.mensaje('login_way', False))
        email = CookAssist.user.get_email()
        if option == '1':
            CookAssist.chef = False
        else:
            CookAssist.chef = True

    #Chef
    @staticmethod
    def menu_chef():
        menu = {}
        option = None
        if CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_chef,
                '2': CookAssist.new_chef,
                '3': CookAssist.chef_status,
                '4': CookAssist.promote_to_chef,
                '5': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_chef_admin', False))
        else:
            menu = {
                '1': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_chef_user', False))
        return menu.get(option)

    #Metodo necesario?
    @staticmethod
    def search_chef():
        option = input(CookAssist.mensaje('search_chef', False))
        if option == '1':
            email = input(CookAssist.mensaje('email', False))
            chef = Chef.get_chef_by_email(email)
            if chef:
                print(chef.str_chef())
                return chef
            else:
                CookAssist.mensaje('chef_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            chefs = Chef.get_chef_by_name(name)
            if len(chefs) != 0:
                CookAssist.mensaje('search_user_header')
                for i in range(len(chefs)):
                    num = str(i + 1)
                    print(num +' '+ chefs[i].get_email() +' '+ chefs[i].get_name())
                option = int(input(CookAssist.mensaje('option', False)))
                print(chefs[(option-1)].str_chef())
                return chefs[(option-1)]
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def new_chef():
        admin = False
        if CookAssist.user:
            if CookAssist.user.get_admin():
                adm = input(CookAssist.mensaje('admin', False))
                if adm == '1':
                    admin = True
        email = input(CookAssist.mensaje('email', False))
        name = input(CookAssist.mensaje('name', False))
        password = input(CookAssist.mensaje('password', False))
        born_date = input(CookAssist.mensaje('born_date', False))
        if Usuario.get_user_by_email(email) is None:
            if Chef.get_chef_by_email(email) is None:
                Chef(admin, email, name, password, born_date)
            else:
                CookAssist.mensaje('chef_duplicated')
        else:
            CookAssist.mensaje('user_duplicated')
    @staticmethod
    def chef_status():
        chef = CookAssist.search_chef()
        if chef:
            status = True
            option = input(CookAssist.mensaje('status', False))
            if option == '2':
                status = False
            chef.set_status_chef(status)

    @staticmethod
    def promote_to_chef():
        user = CookAssist.search_user()
        option = input(CookAssist.mensaje('chef_promote', False))
        if option == '1':
            admin = user.get_admin()
            email = user.get_email()
            name = user.get_name()
            password = user.get_password()
            born_date = user.get_born_date()
            chef = Chef(admin, email, name, password, born_date)
            chef.set_promote_calificaciones(user.get_calificaciones())
            chef.set_promote_pedidos(user.get_pedidos())
    
    @staticmethod
    def see_best_chef():
        pass

    #Producto
    @staticmethod
    def menu_producto():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.search_producto,
                '2': CookAssist.new_producto,
                '3': CookAssist.edit_producto,
                '4': CookAssist.producto_status,
                '5': CookAssist.add_cuantity
            }
            option = input(CookAssist.mensaje('menu_producto_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_producto,
                '2': CookAssist.new_producto,
                '3': CookAssist.edit_producto,
                '4': CookAssist.producto_status,
                '5': CookAssist.add_cuantity
            }
            option = input(CookAssist.mensaje('menu_producto_admin', False))
        else:
            menu = {
                '1': CookAssist.search_producto
            }
            option = input(CookAssist.mensaje('menu_producto_user', False))
        return menu.get(option)
    
    @staticmethod
    def search_producto():
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
    def new_producto():
        nombre = input(CookAssist.mensaje('nombre', False))
        categoria = input(CookAssist.mensaje('categoria', False))
        cantidad = input(CookAssist.mensaje('cantidad', False))
        necesario = input(CookAssist.mensaje('necesario', False))
        medicion = input(CookAssist.mensaje('medicion', False))
        ilimitado = input(CookAssist.mensaje('ilimitado', False))
        Producto(nombre, categoria, cantidad, necesario, medicion, ilimitado)

    @staticmethod
    def edit_producto():
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
    def producto_status():
        pass

    @staticmethod
    def add_cuantity():
        pass
    
    #Receta
    @staticmethod
    def menu_receta():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.search_receta,
                '2': CookAssist.new_receta,
                '3': CookAssist.edit_receta,
                '4': CookAssist.receta_status,
                '5': CookAssist.best_recetas
            }
            option = input(CookAssist.mensaje('menu_receta_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_receta,
                '2': CookAssist.new_receta,
                '3': CookAssist.edit_receta,
                '4': CookAssist.receta_status,
                '5': CookAssist.best_recetas
            }
            option = input(CookAssist.mensaje('menu_receta_admin', False))
        else:
            menu = {
                '1': CookAssist.search_receta,
                '2': CookAssist.best_recetas
            }
            option = input(CookAssist.mensaje('menu_receta_user', False))
        return menu.get(option)

    @staticmethod
    def search_receta():
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
    def edit_receta():
        nombre = input(CookAssist.mensaje('nombre', False))
        tiempo_preparacion = int(input(CookAssist.mensaje('tiempo', False)))
        detalle = CookAssist.add_detalle_receta()
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
                valor = CookAssist.add_detalle_receta()
            elif opcion == '4':
                codigo = input(CookAssist.mensaje('codigo', False))
                cantidad = input(CookAssist.mensaje('cantidad', False))
                valor = {'codigo' : codigo, 'cantidad' : cantidad}
            elif opcion == '5':
                valor = input(CookAssist.mensaje('codigo', False))
            if opcion != '6':
                receta.editar_receta(opcion, valor)
    
    @staticmethod
    def add_detalle_receta():
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

    @staticmethod
    def receta_status():
        pass

    @staticmethod
    def best_recetas():
        pass

    #Pedido
    @staticmethod
    def menu_pedido():
        menu = {}
        option = None
        if CookAssist.chef:
            menu_pedido = {
                '1': CookAssist.search_take_pedidos,
                '2': CookAssist.search_pedido,
                '3': CookAssist.edit_pedido,
                '4': CookAssist.delete_pedido,
                '5': CookAssist.take_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_my_pedido,
                '2': CookAssist.search_pedido,
                '3': CookAssist.new_pedido,
                '4': CookAssist.edit_pedido,
                '5': CookAssist.delete_pedido,
                '6': CookAssist.generate_a_summary_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_admin', False))
        else:
            menu = {
                '1': CookAssist.search_my_pedido,
                '2': CookAssist.new_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_user', False))
        return menu.get(option)
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
    def menu_calificacion():
        menu = {}
        option = None
        if CookAssist.chef:
            menu_pedido = {
                '1': CookAssist.search_my_calificacion,
                '2': CookAssist.search_pedido,
                '3': CookAssist.edit_pedido,
                '4': CookAssist.delete_pedido,
                '5': CookAssist.take_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.search_my_pedido,
                '2': CookAssist.search_pedido,
                '3': CookAssist.new_pedido,
                '4': CookAssist.edit_pedido,
                '5': CookAssist.delete_pedido,
                '6': CookAssist.generate_a_summary_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_admin', False))
        else:
            menu = {
                '1': CookAssist.search_my_calificacion,
                '2': CookAssist.edit_my_calificacion,
                '2': CookAssist.new_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_user', False))
        return menu.get(option)
        

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
        Chef(True, 'alemandoa@gmail.com', 'Alejandro Jiménez', '12345', '28/10/1999')
        Usuario(False, 'ejemplo@gmail.com', 'NN', '12345', '01/01/1963')
        while True:

            while CookAssist.user is None:
                CookAssist.enter()

            while CookAssist.user is not None:
                CookAssist.main()
                
            

if __name__ == '__main__':
    CookAssist.run()
