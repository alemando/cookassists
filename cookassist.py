import os
from languageEN import EN
from languageES import ES
from datos import Datos
from usuario import Usuario
from chef import Chef
from calificacion import Calificacion
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
                '1': CookAssist.menu_day,
                '2': CookAssist.menu_producto,
                '3': CookAssist.menu_receta,
                '4': CookAssist.menu_pedido,
                '5': CookAssist.menu_calificacion,
                '6': CookAssist.menu_chef,
                '7': CookAssist.menu_usuario,
                '8': CookAssist.menu_language
            }
            option = input(CookAssist.mensaje('menu_main_chef', False))
        
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.menu_day,
                '2': CookAssist.menu_producto,
                '3': CookAssist.menu_receta,
                '4': CookAssist.menu_pedido,
                '5': CookAssist.menu_calificacion,
                '6': CookAssist.menu_chef,
                '7': CookAssist.menu_usuario,
                '8': CookAssist.menu_language,
                '9': CookAssist.menu_data
            }
            option = input(CookAssist.mensaje('menu_main_admin', False))
        else:
            menu = {
                '1': CookAssist.menu_day,
                '2': CookAssist.menu_pedido,
                '3': CookAssist.menu_calificacion,
                '4': CookAssist.menu_chef,
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
        CookAssist.chef = False

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
                        '1': CookAssist.see_user,
                        '2': CookAssist.search_user,
                        '3': CookAssist.new_user,
                        '4': CookAssist.edit_my_user,
                        '5': CookAssist.change_to_admin,
                        '6': CookAssist.user_status,
                        '7': CookAssist.change_login_way
                    }
                    option = input(CookAssist.mensaje('menu_usuario_admin_is_chef', False))
                else:
                    menu = {
                        '1': CookAssist.see_user,
                        '2': CookAssist.search_user,
                        '3': CookAssist.new_user,
                        '4': CookAssist.edit_my_user,
                        '5': CookAssist.change_to_admin,
                        '6': CookAssist.user_status
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
        chef = Chef.get_chef_by_email(CookAssist.user.get_email())
        if chef:
            status = chef.get_status_chef()
            if status:
                CookAssist.change_login_way()
    @staticmethod
    def see_user():
        print(Usuario.see_user())
    
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
                Str = CookAssist.mensaje('search_user_header', False)
                for i in range(len(users)):
                    num = str(i + 1)
                    email = users[i].get_email()
                    name = users[i].get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, email, name)
                print(Str)
                option = int(input(CookAssist.mensaje('option', False)))
                user = users[(option-1)]
                print(user)
                return user
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
                '1': CookAssist.see_chef,
                '2': CookAssist.search_chef,
                '3': CookAssist.new_chef,
                '4': CookAssist.chef_status,
                '5': CookAssist.promote_to_chef,
                '6': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_chef_admin', False))
        else:
            menu = {
                '1': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_chef_user', False))
        return menu.get(option)

    @staticmethod
    def see_chef():
        print(Chef.see_chef())

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
                Str = CookAssist.mensaje('search_user_header', False)
                for i in range(len(chefs)):
                    num = str(i + 1)
                    email = chefs[i].get_email()
                    name = chefs[i].get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, email, name)
                print(Str)
                option = int(input(CookAssist.mensaje('option', False)))
                chef = chefs[(option-1)]
                print(chef.str_chef())
                return chef
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
        menu = {
            '1': CookAssist.see_producto,
            '2': CookAssist.search_producto,
            '3': CookAssist.new_producto,
            '4': CookAssist.edit_producto,
            '5': CookAssist.producto_status_menu,
            '6': CookAssist.producto_status,
            '7': CookAssist.see_low_producto,
            '8': CookAssist.change_quantity
        }
        option = input(CookAssist.mensaje('menu_producto', False))
        return menu.get(option)

    @staticmethod
    def see_producto():
        print(Producto.see_producto())

    @staticmethod
    def search_producto():
        option = input(CookAssist.mensaje('search_producto', False))
        if option == '1':
            code = input(CookAssist.mensaje('code', False))
            producto = Producto.get_producto_by_code(code)
            if producto is not None:
                print(producto)
                return producto
            else:
                CookAssist.mensaje('code_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            producto = Producto.get_producto_by_name(name)
            if len(producto) != 0:
                Str = CookAssist.mensaje('search_producto_header', False)
                for i in range(len(producto)):
                    num = str(i + 1)
                    code = producto[i].get_code().zfill(6)
                    name = producto[i].get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, code, name)
                print(Str)
                option = int(input(CookAssist.mensaje('option', False)))
                producto = producto[(option-1)]
                print(producto)
                return producto
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def new_producto():
        name = input(CookAssist.mensaje('name', False))
        quantity = input(CookAssist.mensaje('quantity', False))
        measurement = input(CookAssist.mensaje('measurement', False))
        if measurement == '1':
            measurement = 'N/A'
        elif measurement == '2':
            measurement = 'ml'
        elif measurement == "3":
            measurement = 'gr'
        unlimited = input(CookAssist.mensaje('unlimited', False))
        if unlimited == '1':
            unlimited = True
        else:
            unlimited = False
        Producto(name, quantity, measurement, unlimited)

    @staticmethod
    def edit_producto():
        producto = CookAssist.search_producto()
        if producto is not None:
            option = input(CookAssist.mensaje('edit_producto', False))
            if option == '1':
                name = input(CookAssist.mensaje('name', False))
                producto.set_name(name)
            elif option == '2':
                quantity = input(CookAssist.mensaje('quantity', False))
                producto.set_quantity(quantity)
            elif option == '3':
                measurement = input(CookAssist.mensaje('measurement', False))
                producto.set_measurement(measurement)
            elif option == '4':
                unlimited = input(CookAssist.mensaje('unlimited', False))
                producto.set_unlimited(unlimited)
    
    @staticmethod
    def producto_status():
        producto = CookAssist.search_producto()
        if producto:
            status = True
            option = input(CookAssist.mensaje('status', False))
            if option == '2':
                status = False
            producto.set_status(status)

    @staticmethod
    def producto_status_menu():
        producto = CookAssist.search_producto()
        if producto:
            status = True
            option = input(CookAssist.mensaje('status_menu', False))
            if option == '2':
                status = False
            producto.set_status_menu(status)

    @staticmethod
    def see_low_producto():
        print(Producto.see_low_producto())
    
    @staticmethod
    def change_quantity():
        producto = CookAssist.search_producto()
        operator = input(CookAssist.mensaje('operator', False))
        if operator == '1':
            operator = '+'
        else:
            operator = '-'
        quantity = input(CookAssist.mensaje('quantity', False))
        producto.change_quantity(quantity, operator)

    
    #Receta
    @staticmethod
    def menu_receta():
        menu = {
            '1': CookAssist.see_receta,
            '2': CookAssist.search_receta,
            '3': CookAssist.new_receta,
            '4': CookAssist.edit_receta,
            '5': CookAssist.receta_status_menu,
            '6': CookAssist.best_recetas
        }
        option = input(CookAssist.mensaje('menu_receta', False))
        return menu.get(option)

    @staticmethod
    def search_receta():
        option = input(CookAssist.mensaje('search_receta', False))
        if option == '1':
            code = input(CookAssist.mensaje('code', False))
            receta = Receta.get_receta_by_code(code)
            if receta is not None:
                print(receta)
                return receta
            else:
                CookAssist.mensaje('code_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            receta = Receta.get_producto_by_name(name)
            if len(receta) != 0:
                CookAssist.mensaje('search_receta_header')
                for i in range(len(receta)):
                    num = str(i + 1)
                    print(num +' '+ receta[i].get_code().zfill(6) +' '+ receta[i].get_name())
                option = int(input(CookAssist.mensaje('option', False)))
                print(receta[(option-1)])
                return receta[(option-1)]
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def new_receta():
        name = input(CookAssist.mensaje('name', False))
        time = int(input(CookAssist.mensaje('time', False)))
        detalle = CookAssist.add_detalle_receta()
        Receta(name, time, detalle)
    
    @staticmethod
    def edit_receta():
        receta = CookAssist.search_receta()
        if receta is not None:
            option = input(CookAssist.mensaje('edit_receta', False))
            valor = None
            if option == '1':
                name = input(CookAssist.mensaje('name', False))
                self.set_name(name)
            elif option == '2':
                time = input(CookAssist.mensaje('time', False))
                self.set_time(time)
            elif option == '3':
                detalle_receta = CookAssist.add_detalle_receta()
                for detalle in detalle_receta:
                    DetalleReceta(detalle.get('quantity'), detalle.get('producto'), self)
            elif option == '4':
                code = input(CookAssist.mensaje('code', False))
                quantity = input(CookAssist.mensaje('quantity', False))
                detalle = self.get_detalle_pedidos.get(code)
                detalle.set_quantity(quantity)
            elif option == '5':
                code = input(CookAssist.mensaje('code', False))
                DetalleReceta.delete_detalle(code)

    @staticmethod
    def add_detalle_receta():
        option = input(CookAssist.mensaje('new_detalle_receta', False))
        detalle = []
        while option != '4':
            if option == '1':
                producto = CookAssist.search_producto()
                if producto is not None:
                    quantity = input(CookAssist.mensaje('quantity', False))
                    detalle.append({'quantity' : quantity, 'producto' : producto})
            elif option == '2':
                CookAssist.mensaje('detalle_receta_header', False)
                for i in range(len(detalle)):
                    num = str(i + 1)
                    print(num +' '+ detalle[i].get('quantity').zfill(7) 
                            +' '+ detalle[i].get('producto').get_name())
                option_detalle = int(input(CookAssist.mensaje('option', False)))
                quantity = input(CookAssist.mensaje('quantity', False))
                detalle[option_detalle-1]['quantity'] = quantity
            elif option == '3':
                for i in range(len(detalle)):
                    num = str(i + 1)
                    print(num +' '+ detalle[i].get('quantity').zfill(7) 
                            +' '+ detalle[i].get('producto').get_name())
                pos_detalle = int(input(CookAssist.mensaje('option', False)))
                detalle.pop(pos_detalle-1)
            
            option = input(CookAssist.mensaje('new_detalle_receta', False))
        return detalle

    #menu
    @staticmethod
    def receta_status_menu():
        producto = CookAssist.search_producto()
        if producto:
            status = True
            option = input(CookAssist.mensaje('status_menu', False))
            if option == '2':
                status = False
            producto.set_status_menu(status)

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

    @staticmethod
    def menu_day():
        pass

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
        CookAssist.user = Chef(True, 'alemandoa@gmail.com', 'Alejandro Jiménez', '12345', '28/10/1999')
        Usuario(False, 'ejemplo@gmail.com', 'NN', '12345', '01/01/1963')
        while True:

            while CookAssist.user is None:
                CookAssist.enter()
            while CookAssist.user is not None:
                CookAssist.main()
                
            

if __name__ == '__main__':
    CookAssist.run()
