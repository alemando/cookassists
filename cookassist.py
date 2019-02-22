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
from detalleReceta import DetalleReceta
from detallePedido import DetallePedido

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
        Datos.generate_productos()
        Datos.generate_user_chef()
        Datos.generate_receta()
        Datos.generate_pedidos()
        Datos.generate_calificaciones()

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
    def search_producto_menu():
        option = input(CookAssist.mensaje('search_producto', False))
        if option == '1':
            code = input(CookAssist.mensaje('code', False))
            producto = Producto.get_producto_by_code_menu(code)
            if producto is not None:
                print(producto)
                return producto
            else:
                CookAssist.mensaje('code_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            producto = Producto.get_producto_by_name_menu(name)
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
        Producto(name, quantity, measurement)

    @staticmethod
    def edit_producto():
        producto = CookAssist.search_producto()
        if producto:
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
        if producto:
            operator = input(CookAssist.mensaje('operator', False))
            if operator == '1':
                operator = '+'
            else:
                operator = '-'
            quantity = int(input(CookAssist.mensaje('quantity', False)))
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
            '6': CookAssist.see_best_recetas
        }
        option = input(CookAssist.mensaje('menu_receta', False))
        return menu.get(option)

    @staticmethod
    def see_receta():
        print(Receta.see_receta())

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
            receta = Receta.get_receta_by_name(name)
            if len(receta) != 0:
                Str = CookAssist.mensaje('search_receta_header', False)
                for i in range(len(receta)):
                    num = str(i + 1)
                    code = receta[i].get_code().zfill(6)
                    name = receta[i].get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, code, name)
                print(Str)
                option = int(input(CookAssist.mensaje('option', False)))
                receta = receta[(option-1)]
                print(receta)
                return receta
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def search_receta_menu():
        option = input(CookAssist.mensaje('search_receta', False))
        if option == '1':
            code = input(CookAssist.mensaje('code', False))
            receta = Receta.get_receta_by_code_menu(code)
            if receta is not None:
                print(receta)
                return receta
            else:
                CookAssist.mensaje('code_not_found')
                return None
            
        elif option == '2':
            name = input(CookAssist.mensaje('name', False))
            receta = Receta.get_receta_by_name_menu(name)
            if len(receta) != 0:
                Str = CookAssist.mensaje('search_receta_header', False)
                for i in range(len(receta)):
                    num = str(i + 1)
                    code = receta[i].get_code().zfill(6)
                    name = receta[i].get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, code, name)
                print(Str)
                option = int(input(CookAssist.mensaje('option', False)))
                receta = receta[(option-1)]
                print(receta)
                return receta
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
        if receta:
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
                receta.add_more_detalle_receta(detalle_receta)
            elif option == '4':
                code = input(CookAssist.mensaje('code', False))
                quantity = input(CookAssist.mensaje('quantity', False))
                detalle = self.get_detalle_recetas.get(code)
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
                if producto:
                    quantity = input(CookAssist.mensaje('quantity', False))
                    detalle.append({'quantity' : quantity, 'producto' : producto})
            elif option == '2':
                Str = CookAssist.mensaje('detalle_receta_header', False)
                for i in range(len(detalle)):
                    num = str(i + 1)
                    quantity = str(detalle[i].get('quantity')).zfill(7) 
                    name = detalle[i].get('producto').get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, quantity, name)
                print(Str)
                option_detalle = int(input(CookAssist.mensaje('option', False)))
                quantity = input(CookAssist.mensaje('quantity', False))
                detalle[option_detalle-1]['quantity'] = quantity
            elif option == '3':
                Str = CookAssist.mensaje('detalle_receta_header', False)
                for i in range(len(detalle)):
                    num = str(i + 1)
                    quantity = str(detalle[i].get('quantity')).zfill(7) 
                    name = detalle[i].get('producto').get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, quantity, name)
                print(Str)
                pos_detalle = int(input(CookAssist.mensaje('option', False)))
                detalle.pop(pos_detalle-1)
            
            option = input(CookAssist.mensaje('new_detalle_receta', False))
        return detalle

    @staticmethod
    def receta_status_menu():
        receta = CookAssist.search_receta()
        if receta:
            status = True
            option = input(CookAssist.mensaje('status_menu', False))
            if option == '2':
                status = False
            receta.set_status_menu(status)

    #Pedido
    @staticmethod
    def menu_pedido():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.see_pedido,
                '2': CookAssist.search_pedido,
                '3': CookAssist.edit_pedido,
                '4': CookAssist.see_pending_pedido,
                '5': CookAssist.take_pedido,
                '6': CookAssist.see_take_pedido,
                '7': CookAssist.ready_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.see_pedido,
                '2': CookAssist.see_my_pedido,
                '3': CookAssist.search_pedido,
                '4': CookAssist.new_pedido,
                '5': CookAssist.edit_pedido,
                '6': CookAssist.see_pending_pedido,
                '7': CookAssist.generate_a_summary_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_admin', False))
        else:
            menu = {
                '1': CookAssist.see_my_pedido,
                '2': CookAssist.new_pedido
            }
            option = input(CookAssist.mensaje('menu_pedido_user', False))
        return menu.get(option)
    
    @staticmethod
    def see_pedido():
        print(Pedido.see_pedido())

    @staticmethod
    def search_pedido():
        option = input(CookAssist.mensaje('search_pedido', False))
        if option == '1':
            code = input(CookAssist.mensaje('code', False))
            pedido = Pedido.get_pedido_by_code(code)
            if pedido:
                print(pedido)
                return pedido
            else:
                CookAssist.mensaje('code_not_found')
                return None
            
        elif option == '2':
            date = input(CookAssist.mensaje('date', False))
            pedido = Pedido.get_pedido_by_date(date)
            if len(pedido) != 0:
                Str = CookAssist.mensaje('search_pedido_header', False)
                for i in range(len(pedido)):
                    num = str(i + 1)
                    code = pedido[i].get_code().zfill(6)
                    date = pedido[i].get_date()
                    user = pedido[i].get_usuario().get_name()
                    Str += CookAssist.mensaje('format_4_str', False) % (
                        num, code, date, user)
                print(Str)
                option = int(input(CookAssist.mensaje('option', False)))
                pedido = pedido[(option-1)]
                print(pedido)
                return pedido
            else:
                CookAssist.mensaje('not_match')

    @staticmethod
    def new_pedido():
        usuario = CookAssist.user
        detalle = CookAssist.add_detalle_pedido()
        description = input(CookAssist.mensaje('description', False))
        Pedido(usuario, detalle, description)

    @staticmethod
    def edit_pedido():
        pedido = CookAssist.search_pedido()
        if pedido:
            option = input(CookAssist.mensaje('edit_pedido', False))
            if option == '1':
                description = input(CookAssist.mensaje('description', False))
                Pedido.set_description(description)
            elif option == '2':
                detalle_pedido = CookAssist.add_detalle_pedido()
                pedido.add_more_detalle_pedido(detalle_pedido)

    @staticmethod
    def add_detalle_pedido():
        option = input(CookAssist.mensaje('new_detalle_pedido', False))
        detalle = []
        while option != '5':
            if option == '1':
                producto = CookAssist.search_producto_menu()
                if producto:
                    quantity = int(input(CookAssist.mensaje('quantity', False)))
                    check = producto.check_producto(quantity)
                    if check is True:
                        detalle.append({'quantity' : quantity, 'detalle' : producto})
                    else:
                        print(check)
            elif option == '2':
                receta = CookAssist.search_receta_menu()
                if receta:
                    quantity = int(input(CookAssist.mensaje('quantity', False)))
                    check = receta.check_receta(quantity)
                    if check is True:
                        detalle.append({'quantity' : quantity, 'detalle' : receta})
                    else:
                        print(check)
            elif option == '3':
                Str = CookAssist.mensaje('detalle_pedido_header', False)
                for i in range(len(detalle)):
                    num = str(i + 1)
                    quantity = str(detalle[i].get('quantity')).zfill(7) 
                    name = detalle[i].get('detalle').get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, quantity, name)
                print(Str)
                option_detalle = int(input(CookAssist.mensaje('option', False)))
                quantity = int(input(CookAssist.mensaje('quantity', False)))
                detalle = detalle[option_detalle-1].get('detalle')
                check = False
                if isinstance(detalle, Producto):
                    check = producto.check_producto(quantity)
                else:
                    check = receta.check_receta(quantity)
                if check is True:
                    detalle[option_detalle-1]['quantity'] = quantity
                else:
                    print(check)
            elif option == '4':
                Str = CookAssist.mensaje('detalle_pedido_header', False)
                for i in range(len(detalle)):
                    num = str(i + 1)
                    quantity = str(detalle[i].get('quantity')).zfill(7) 
                    name = detalle[i].get('detalle').get_name()
                    Str += CookAssist.mensaje('format_3_str', False) % (
                        num, quantity, name)
                print(Str)
                posicionDetalle = int(input(CookAssist.mensaje('option', False)))
                detalle.pop(posicionDetalle-1)
            
            option = input(CookAssist.mensaje('new_detalle_pedido', False))
        return detalle


    @staticmethod
    def see_pending_pedido():
        print(Pedido.see_pedido_pending())
    
    @staticmethod
    def take_pedido():
        pedido = CookAssist.search_pedido()
        if pedido:
            pedido.set_chef(CookAssist.user)

    @staticmethod
    def see_take_pedido():
        print(Pedido.see_take_pedido(CookAssist.user))

    @staticmethod
    def ready_pedido():
        pedido = CookAssist.search_pedido()
        if pedido:
            pedido.set_ready(True)

    @staticmethod
    def generate_a_summary_pedido():
        date_start = input(CookAssist.mensaje('date_start', False))
        date_end = input(CookAssist.mensaje('date_end', False))
        print(Pedido.summary(date_start, date_end))

    @staticmethod
    def see_my_pedido():
        print(Pedido.see_my_pedido(CookAssist.user))


    @staticmethod
    def menu_day():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.see_best_recetas,
                '2': CookAssist.see_menu,
                '3': CookAssist.producto_status_menu,
                '4': CookAssist.receta_status_menu
            }
            option = input(CookAssist.mensaje('menu_day_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.see_best_recetas,
                '2': CookAssist.see_menu,
                '3': CookAssist.producto_status_menu,
                '4': CookAssist.receta_status_menu
            }
            option = input(CookAssist.mensaje('menu_day_admin', False))
        else:
            menu = {
                '1': CookAssist.see_best_recetas,
                '2': CookAssist.see_menu,
            }
            option = input(CookAssist.mensaje('menu_day_user', False))
        return menu.get(option)
    
    @staticmethod
    def see_menu():
        option = input(CookAssist.mensaje('menu_day_select', False))
        if option == '1':
            print(Producto.see_menu())
        else:
            print(Receta.see_menu())
        
    @staticmethod
    def menu_calificacion():
        menu = {}
        option = None
        if CookAssist.chef:
            menu = {
                '1': CookAssist.search_calificacion,
                '2': CookAssist.see_best_recetas,
                '3': CookAssist.see_best_chef
            }
            option = input(CookAssist.mensaje('menu_calificacion_chef', False))
        elif CookAssist.user.get_admin():
            menu = {
                '1': CookAssist.see_calificacion,
                '2': CookAssist.search_calificacion,
                '3': CookAssist.delete_calificacion,
                '4': CookAssist.see_best_recetas,
                '5': CookAssist.see_best_chef,
                '6': CookAssist.new_calificacion,
                '7': CookAssist.edit_my_calificacion,
                '8': CookAssist.delete_my_calificacion
            }
            option = input(CookAssist.mensaje('menu_calificacion_admin', False))
        else:
            menu = {
                '1': CookAssist.search_calificacion,
                '2': CookAssist.see_best_recetas,
                '3': CookAssist.see_best_chef,
                '4': CookAssist.new_calificacion,
                '5': CookAssist.edit_my_calificacion,
                '6': CookAssist.delete_my_calificacion
            }
            option = input(CookAssist.mensaje('menu_calificacion_user', False))
        return menu.get(option)
        
    @staticmethod
    def see_best_chef():
        print(Calificacion.best_chef())
    
    @staticmethod
    def see_best_recetas():
        print(Calificacion.best_recetas())

    @staticmethod
    def see_calificacion():
        print(Calificacion.see_calificacion())

    @staticmethod
    def search_calificacion():
        option = input(CookAssist.mensaje('search_calificacion', False))
        if option == '1':
            receta = CookAssist.search_receta_menu()
            if receta:
                print(Calificacion.see_average(receta))
            else:
                CookAssist.mensaje('code_not_found')
                

    @staticmethod
    def delete_calificacion():
        code = input(CookAssist.mensaje('code', False))
        calificacion = Calificacion.get_calificacion_by_code(code)
        if calificacion:
            print(calificacion)
            option = input(CookAssist.mensaje('delete_calificacion', False))
            if option == '1':
                calificacion.delete()
        else:
            CookAssist.mensaje('code_not_found')
                

    @staticmethod
    def new_calificacion():
        option = input(CookAssist.mensaje('new_calificacion', False))
        if option == '1':
            print(Pedido.see_my_pedido_calificacion(CookAssist.user))
        elif option == '2':
            code = input(CookAssist.mensaje('code', False))
            pedido = Pedido.get_pedido_by_code(code)
            if pedido:
                pedido.set_qualified(True)
                print(pedido)
                print (pedido.get_chef().get_name())
                rating = input(CookAssist.mensaje('rating', False))
                description = input(CookAssist.mensaje('description', False))
                Calificacion(CookAssist.user, rating, description, pedido.get_chef())
                for detalle in pedido.get_detalle_pedidos().values():
                    aux = detalle.get_receta()
                    if isinstance(aux, Receta):
                        print(aux.str_user())
                        rating = input(CookAssist.mensaje('rating', False))
                        description = input(CookAssist.mensaje('description', False))
                        Calificacion(CookAssist.user, rating, description, aux)

            else:
                CookAssist.mensaje('code_not_found')

    @staticmethod
    def edit_my_calificacion():
        print(Calificacion.see_my_calificacion(CookAssist.user))
        code = input(CookAssist.mensaje('code', False))
        calificacion = Calificacion.get_calificacion_by_code_user(CookAssist.user, code)
        if calificacion:
            print(calificacion)
            option = input(CookAssist.mensaje('edit_calificacion', False))
            if option == '1':
                rating = input(CookAssist.mensaje('rating', False))
                calificacion.set_rating(rating)
            elif option == '2':
                description = input(CookAssist.mensaje('description', False))
                calificacion.set_description(description)
        else:
            CookAssist.mensaje('code_not_found')

    @staticmethod
    def delete_my_calificacion():
        print(Calificacion.see_my_calificacion(CookAssist.user))
        code = input(CookAssist.mensaje('code', False))
        calificacion = Calificacion.get_calificacion_by_code_user(CookAssist.user, code)
        if calificacion:
            print(calificacion)
            option = input(CookAssist.mensaje('delete_calificacion', False))
            if option == '1':
                calificacion.delete()
        else:
            CookAssist.mensaje('code_not_found')

    @staticmethod
    def run():

        EN.men = ES.spanish
        #Usuario admin, y primer usuario del sistema
        Chef(True, 'alemandoa@gmail.com', 'Alejandro Jiménez', '12345', '28/10/1999')
        while True:

            while CookAssist.user is None:
                CookAssist.enter()
            while CookAssist.user is not None:
                CookAssist.main()
                
            

if __name__ == '__main__':
    CookAssist.run()
