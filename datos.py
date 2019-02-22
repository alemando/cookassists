import random as r
from producto import Producto
from usuario import Usuario
from chef import Chef
from receta import Receta
from pedido import Pedido
from calificacion import Calificacion

class Datos:

    @staticmethod
    def generate_receta():
        recetas = {
            '1': {
                'code' : 1,
                'name' : 'Arroz con pollo',
                'time' : '9',
                'detalle' : [
                {'key': '1', 'quantity' : 100},
                {'key': '2', 'quantity' : 50},
                {'key': '3', 'quantity' : 300},
                {'key': '4', 'quantity' : 10},
                {'key': '5', 'quantity' : 1},
                {'key': '6', 'quantity' : 70},
                {'key': '7', 'quantity' : 70}
                ],
                'status_menu' : True
            },
            '2': {
                'code' : 2,
                'name' : 'Desayuno tipico',
                'time' : '6',
                'detalle' : [
                {'key': '8', 'quantity' : 1},
                {'key': '4', 'quantity' : 4},
                {'key': '9', 'quantity' : 40},
                {'key': '11', 'quantity' : 1},
                {'key': '12', 'quantity' : 60}
                ],
                'status_menu' : True
            },
            '3': {
                'code' : 3,
                'name' : 'Cafe',
                'time' : '3',
                'detalle' : [
                {'key': '13', 'quantity' : 150},
                {'key': '10', 'quantity' : 15},
                {'key': '3', 'quantity' : 50}
                ],
                'status_menu' : True
            },
            '4': {
                'code' : 4,
                'name' : 'Chocolate',
                'time' : '4',
                'detalle' : [
                {'key': '3', 'quantity' : 200},
                {'key': '14', 'quantity' : 50}
                ],
                'status_menu' : True
            },
            '5': {
                'code' : 5,
                'name' : 'Limonada',
                'time' : '5',
                'detalle' : [
                {'key': '3', 'quantity' : 210},
                {'key': '20', 'quantity' : 100},
                {'key': '16', 'quantity' : 15}
                ],
                'status_menu' : True
            },
            '6': {
                'code' : 6,
                'name' : 'Jugo de maracuya',
                'time' : '5',
                'detalle' : [
                {'key': '3', 'quantity' : 210},
                {'key': '15', 'quantity' : 100},
                {'key': '16', 'quantity' : 15}
                ],
                'status_menu' : True
            },
            '7': {
                'code' : 7,
                'name' : 'Jugo de mora',
                'time' : '5',
                'detalle' : [
                {'key': '3', 'quantity' : 210},
                {'key': '18', 'quantity' : 100},
                {'key': '16', 'quantity' : 15}
                ],
                'status_menu' : True
            },
            '8': {
                'code' : 8,
                'name' : 'Jugo de mango',
                'time' : '5',
                'detalle' : [
                {'key': '3', 'quantity' : 210},
                {'key': '19', 'quantity' : 100},
                {'key': '16', 'quantity' : 15}
                ],
                'status_menu' : True
            },
            '9': {
                'code' : 9,
                'name' : 'Huevos revueltos con pan',
                'time' : '9',
                'detalle' : [
                {'key': '8', 'quantity' : 1},
                {'key': '21', 'quantity' : 70},
                {'key': '22', 'quantity' : 55},
                {'key': '2', 'quantity' : 40},
                {'key': '23', 'quantity' : 100},
                {'key': '12', 'quantity' : 60},
                {'key': '4', 'quantity' : 4}
                ],
                'status_menu' : True
            },
            '10': {
                'code' : 10,
                'name' : 'Huevo con arroz',
                'time' : '8',
                'detalle' : [
                {'key': '1', 'quantity' : 100},
                {'key': '8', 'quantity' : 1},
                {'key': '2', 'quantity' : 40},
                {'key': '4', 'quantity' : 4}
                ],
                'status_menu' : True
            },
            '11': {
                'code' : 11,
                'name' : 'Ensalada de crotones',
                'time' : '7',
                'detalle' : [
                {'key': '23', 'quantity' : 70},
                {'key': '24', 'quantity' : 80},
                {'key': '21', 'quantity' : 60},
                {'key': '25', 'quantity' : 10},
                {'key': '20', 'quantity' : 20},
                {'key': '4', 'quantity' : 4},
                {'key': '26', 'quantity' : 30}
                ],
                'status_menu' : True
            },
            '12': {
                'code' : 12,
                'name' : 'Frijoles',
                'time' : '12',
                'detalle' : [
                {'key': '27', 'quantity' : 100},
                {'key': '3', 'quantity' : 200},
                {'key': '7', 'quantity' : 60},
                {'key': '28', 'quantity' : 50},
                {'key': '4', 'quantity' : 5}
                ],
                'status_menu' : True
            },
            '13': {
                'code' : 13,
                'name' : 'Tomate relleno',
                'time' : '13',
                'detalle' : [
                {'key': '21', 'quantity' : 140},
                {'key': '29', 'quantity' : 40},
                {'key': '30', 'quantity' : 90},
                {'key': '4', 'quantity' : 7},
                {'key': '31', 'quantity' : 55}
                ],
                'status_menu' : True
            },
            '14': {
                'code' : 14,
                'name' : 'Patacon con pollo',
                'time' : '9',
                'detalle' : [
                {'key': '33', 'quantity' : 400},
                {'key': '32', 'quantity' : 150},
                {'key': '29', 'quantity' : 40},
                {'key': '31', 'quantity' : 40},
                {'key': '4', 'quantity' : 5}
                ],
                'status_menu' : True
            },
            '15': {
                'code' : 15,
                'name' : 'Pastas a la carbonara',
                'time' : '10',
                'detalle' : [
                {'key': '34', 'quantity' : 250},
                {'key': '29', 'quantity' : 80},
                {'key': '26', 'quantity' : 50},
                {'key': '35', 'quantity' : 100}
                ],
                'status_menu' : True
            },
            '16': {
                'code' : 16,
                'name' : 'Postre de nata',
                'time' : '9',
                'detalle' : [
                {'key': '13', 'quantity' : 200},
                {'key': '36', 'quantity' : 40},
                {'key': '37', 'quantity' : 15},
                {'key': '38', 'quantity' : 1},
                {'key': '16', 'quantity' : 30}
                ],
                'status_menu' : True
            },
        }
        for receta in recetas.values():
            name = receta.get('name')
            time = receta.get('time')
            code = receta.get('code')
            status_menu = receta.get('status_menu')
            detalle = receta.get('detalle')
            detalle_receta = []
            for item in detalle:
                key = item.get('key')
                producto = Producto.get_producto_by_code(key)
                quantity = item.get('quantity')
                detalle_receta.append({'quantity' : quantity, 'producto' : producto})
            Receta(name, time, detalle_receta, code, status_menu)
       

    @staticmethod
    def generate_user_chef():
        Usuario(True, 'user1@gmail.com', 'Pedro Perez', '12345', '11/01/1999')
        Chef(False, 'chef1@gmail.com', 'Ricardo Arias', '12345', '28/11/1998')
        Chef(False, 'chef2@gmail.com', 'Juan Gomez', '12345', '24/12/1999')
        Usuario(False, 'user2@gmail.com', 'Juan Pablo Ciro', '12345', '09/03/2000')
        Usuario(False, 'user3@gmail.com', 'Juan Jose Sapuyes', '12345', '16/08/2001')
        Usuario(False, 'user4@gmail.com', 'Santiago Jiemenez', '12345', '18/08/1997')
        Usuario(False, 'user5@gmail.com', 'Mariana Gomez', '12345', '22/10/1995')

    @staticmethod
    def generate_productos():
        Producto('Arroz',10000,'gr',1,True,False)
        Producto('Aceite',1000,'ml',2,True,False)
        Producto('Agua',50000,'ml',3,True,False)
        Producto('Sal',2000,'gr',4,True,False)
        Producto('Media pechuga',10,'N/A',5,True,False)
        Producto('Alverja',1000,'gr',6,True,False)
        Producto('Zanahoria',1000,'gr',7,True,False)
        Producto('Huevo',50,'N/A',8,True,False)
        Producto('Mantequilla',1000,'gr',9,True,False)
        Producto('Cafe',1000,'gr',10,True,False)
        Producto('Arepa',50,'N/A',11,True,False)
        Producto('Quesito',1000,'gr',12,True,False)
        Producto('Leche',7000,'ml',13,True,False)
        Producto('Chocolate en polvo',1000,'gr',14,True,False)
        Producto('Pulpa de maracuya',1000,'gr',15,True,False)
        Producto('Azuzar',2000,'gr',16,True,False)
        Producto('Sobre de azuzar',60,'N/A',17,True,True)
        Producto('Pulpa de mora',1000,'gr',18,True,False)
        Producto('Pulpa de mango',1000,'gr',19,True,False)
        Producto('Zumo de limon',1000,'ml',20,True,False)
        Producto('Tomate',1000,'gr',21,True,False)
        Producto('Cebolla',1000,'gr',22,True,False)
        Producto('Pan',1000,'gr',23,True,False)
        Producto('Lechuga',1000,'gr',24,True,False)
        Producto('Cilantro',1000,'gr',25,True,False)
        Producto('Queso Parmessano',500,'gr',26,True,False)
        Producto('Frijoles',1000,'gr',27,True,False)
        Producto('Papa criolla',1000,'gr',28,True,False)
        Producto('Tocineta',1000,'gr',29,True,False)
        Producto('Solomo de res',1000,'gr',30,True,False)
        Producto('Queso Mozarella',1000,'gr',31,True,False)
        Producto('Pollo desmechado',1000,'gr',32,True,False)
        Producto('Platano',2000,'gr',33,True,False)
        Producto('Espagueti',2000,'gr',34,True,False)
        Producto('Crema de leche',1000,'ml',35,True,False)
        Producto('Pasas',1000,'gr',36,True,False)
        Producto('Ron',1000,'ml',37,True,False)
        Producto('Yema de huevo',50,'N/A',38,True,False)
        Producto('Ajo',100,'gr',39,False,False)
        Producto('Botella de agua',30,'N/A',40,True,True)
        Producto('Botella de COCA-COLA',30,'N/A',41,True,True)
        Producto('Jugo HIT',30,'N/A',42,True,True)

        
    @staticmethod
    def generate_pedidos():
        pedidos = {
            '1': {
                'code' : 1,
                'user' : 'user1@gmail.com',
                'chef' : 'alemandoa@gmail.com',
                'description' : 'Sin sal',
                'detalle' : [
                {'para' : 'producto','key': '17', 'quantity' : 2},
                {'para' : 'receta','key': '3', 'quantity' : 1},
                {'para' : 'receta', 'key': '9', 'quantity' : 1}
                ],
                'date' : '19/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '2': {
                'code' : 2,
                'user' : 'user1@gmail.com',
                'chef' : 'alemandoa@gmail.com',
                'description' : 'Sin azucar',
                'detalle' : [
                {'para' : 'receta','key': '5', 'quantity' : 2},
                {'para' : 'receta','key': '7', 'quantity' : 1},
                {'para' : 'receta', 'key': '8', 'quantity' : 1},
                {'para' : 'receta','key': '11', 'quantity' : 1},
                {'para' : 'receta','key': '12', 'quantity' : 1},
                {'para' : 'receta', 'key': '14', 'quantity' : 2},
                {'para' : 'receta', 'key': '16', 'quantity' : 16}
                ],
                'date' : '19/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '3': {
                'code' : 3,
                'user' : 'user2@gmail.com',
                'chef' : 'chef2@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '8', 'quantity' : 2},
                {'para' : 'receta','key': '15', 'quantity' : 1},
                {'para' : 'receta','key': '1', 'quantity' : 1}
                ],
                'date' : '19/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '4': {
                'code' : 4,
                'user' : 'user2@gmail.com',
                'chef' : 'chef1@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '4', 'quantity' : 1},
                {'para' : 'receta','key': '2', 'quantity' : 1}
                ],
                'date' : '20/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '5': {
                'code' : 5,
                'user' : 'user3@gmail.com',
                'chef' : 'chef2@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '4', 'quantity' : 1},
                {'para' : 'receta','key': '10', 'quantity' : 1}
                ],
                'date' : '20/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '6': {
                'code' : 6,
                'user' : 'user3@gmail.com',
                'chef' : 'chef1@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '3', 'quantity' : 1},
                {'para' : 'receta','key': '10', 'quantity' : 1}
                ],
                'date' : '20/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '7': {
                'code' : 7,
                'user' : 'user4@gmail.com',
                'chef' : 'chef1@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'producto','key': '40', 'quantity' : 1},
                {'para' : 'receta','key': '15', 'quantity' : 1}
                ],
                'date' : '20/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '8': {
                'code' : 8,
                'user' : 'user4@gmail.com',
                'chef' : None,
                'description' : '',
                'detalle' : [
                {'para' : 'producto','key': '41', 'quantity' : 1},
                {'para' : 'receta','key': '13', 'quantity' : 1}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            },
            '9': {
                'code' : 9,
                'user' : 'user5@gmail.com',
                'chef' : None,
                'description' : '',
                'detalle' : [
                {'para' : 'producto','key': '42', 'quantity' : 1},
                {'para' : 'receta','key': '1', 'quantity' : 1}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            },
            '10': {
                'code' : 10,
                'user' : 'user5@gmail.com',
                'chef' : 'chef1@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'producto','key': '41', 'quantity' : 2},
                {'para' : 'receta','key': '15', 'quantity' : 2}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            },
            '11': {
                'code' : 11,
                'user' : 'chef1@gmail.com',
                'chef' : 'chef2@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'producto','key': '42', 'quantity' : 1},
                {'para' : 'receta','key': '11', 'quantity' : 1}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            },
            '12': {
                'code' : 12,
                'user' : 'chef2@gmail.com',
                'chef' : 'chef1@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '6', 'quantity' : 2},
                {'para' : 'receta','key': '8', 'quantity' : 2},
                {'para' : 'receta','key': '12', 'quantity' : 4}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            },
            '13': {
                'code' : 13,
                'user' : 'alemandoa@gmail.com',
                'chef' : 'chef2@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '7', 'quantity' : 2},
                {'para' : 'receta','key': '5', 'quantity' : 1},
                {'para' : 'receta','key': '12', 'quantity' : 1},
                {'para' : 'receta','key': '15', 'quantity' : 1},
                {'para' : 'receta','key': '13', 'quantity' : 1}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : True
            },
            '14': {
                'code' : 14,
                'user' : 'alemandoa@gmail.com',
                'chef' : 'chef1@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '7', 'quantity' : 1},
                {'para' : 'receta','key': '1', 'quantity' : 1}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            },
            '15': {
                'code' : 15,
                'user' : 'alemandoa@gmail.com',
                'chef' : 'chef2@gmail.com',
                'description' : '',
                'detalle' : [
                {'para' : 'receta','key': '8', 'quantity' : 1},
                {'para' : 'receta','key': '14', 'quantity' : 1}
                ],
                'date' : '21/02/2019',
                'qualified' : False,
                'ready' : False
            }
        }

        for pedido in pedidos.values():
            code = pedido.get('code')
            user = Usuario.get_user_by_email(pedido.get('user'))
            chef = Chef.get_chef_by_email(pedido.get('chef'))
            description = pedido.get('description')
            detalle = pedido.get('detalle')
            date = pedido.get('date')
            qualified = pedido.get('qualified')
            ready = pedido.get('ready')
            detalle_pedido = []
            for item in detalle:
                key = item.get('key')
                para = item.get('para')
                detalle = None
                if para == 'producto':
                    detalle = Producto.get_producto_by_code(key)
                elif para == 'receta':
                    detalle = Receta.get_receta_by_code(key)
                quantity = item.get('quantity')
                detalle_pedido.append({'quantity' : quantity, 'detalle' : detalle})
            Pedido(user, detalle_pedido, description, date, code, chef, qualified, ready)
        
    @staticmethod
    def generate_calificaciones():
        archive = open('Calificacion_data.txt','r')
        for line in archive.readlines():
            calificacion = line.split(',')
            user = Usuario.get_user_by_email(calificacion[0])
            rating = calificacion[1]
            description = calificacion[2]
            para = calificacion[3]
            if para.find('@') != -1:
                para = Chef.get_chef_by_email(calificacion[3])
            else:
                para = Receta.get_receta_by_code(calificacion[3])
            code = int(calificacion[4])
            Calificacion(user, rating, description, para, code)
        archive.close()
