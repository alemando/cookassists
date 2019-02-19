class ES:

    spanish = {
    'language' :'''
    Idioma:
    1. Español
    2. Ingles
    Seleccione: ''',
    'sign_off' : 'Cerrando sesion',
    'enter' : '''
    Bienvenido a CookAssist
    es usted un?
    1. Usuario registrado
    2. Usuario sin registrar
    3. Salir
    Seleccione una opcion: ''',
    'email' : 'Ingrese su email: ',
    'password' : 'Ingrese su contraseña: ',
    'name' : 'Ingrese su nombre: ',
    'admin' : '''
    Usuario administrador?
    1. Si
    2. No
    Ingrese la opcion: ''',
    'born_date' : 'Ingrese su fecha de nacimiento(dd/mm/yyyy): ',
    'user_not_found' : 'Usuario no encontrado',
    'menu_main_admin' : '''
    Menú
    1. Menu del día
    2. Menu Productos
    3. Menu Recetas
    4. Menu Pedidos
    5. Menu Calificación
    6. Menu Chefs
    7. Menu Usuario
    8. Menu Idiomas
    9. Menu Datos
    10. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_chef' : '''
    Menú
    1. Menu del día
    2. Menu Productos
    3. Menu Recetas
    4. Menu Pedidos
    5. Menu Calificación
    6. Menu Chefs
    7. Menu Usuario
    8. Menu Idiomas
    9. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_user' : '''
    Menú
    1. Menu del día
    2. Menu Pedidos
    3. Menu Calificación
    4. Menu Chefs
    5. Menu Usuario
    6. Menu Idiomas
    7. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_data' : '''
    Menú Datos
    1. Agregar datos ficticios
    2. <-Atras
    Seleccione una opción: ''',
    'menu_language' : '''
    Menú Idiomas
    1. Cambiar idioma
    2. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_admin': '''
    Menú Usuario
    1. Ver usuarios
    2. Buscar usuario
    3. Nuevo usuario
    4. Editar mi usuario
    5. Cambiar permisos
    6. Activar/Desactivar usuario
    7. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_admin_is_chef': '''
    Menú Usuario
    1. Ver usuarios
    2. Buscar usuario
    3. Nuevo usuario
    4. Editar mi usuario
    5. Cambiar permisos
    6. Activar/Desactivar usuario
    7. Cambiar modo de inicio
    8. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_chef': '''
    Menú Usuario
    1. Editar mi usuario
    2. Cambiar modo de inicio
    3. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_user': '''
    Menú Usuario
    1. Editar mi usuario
    2. Desactivar mi usuario
    3. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_user_is_chef': '''
    Menú Usuario
    1. Editar mi usuario
    2. Desactivar mi usuario
    3. Cambiar modo de inicio
    4. <-Atras
    Seleccione una opción: ''',
    'search_user' : '''
    Buscar usuario por:
    1. email
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'not_match' : 'Nó se encontraron coincidencias',
    'yes' : 'Si',
    'no' : 'NO',
    'str_user' : '''
    Administrador: %s
    Nombre: %s
    email: %s
    Fecha nacimiento: %s
    Estado: %s
    ''',
    'str_see_user_header' : 'Nombre        Email         Estado \n',
    'str_see_user' : '%s %s %s \n',
    'active' : 'Activo',
    'inactive' : 'Inactivo',
    'search_user_header' : '# Email                Nombre \n',
    'option' : 'Seleccione una opción: ',
    'close' : 'Programa Cerrado',
    'menu_chef_admin' : '''
    Menú Chef
    1. Ver Chefs
    2. Buscar chef
    3. Nuevo chef
    4. Activar/Desactivar chef
    5. Promover a chef
    6. Ver mejor chef
    7. <-Atras
    Seleccione una opción: ''',
    'menu_chef_user' : '''
    Menú Chef
    1. Ver mejor chef
    2. <-Atras
    Seleccione una opción: ''',
    'menu_producto' : '''
    Menú Productos
    1. ver productos
    2. Buscar producto
    3. Nuevo producto
    4. Editar producto
    5. Activar/Desactivar producto en menú
    6. Activar/Desactivar producto
    7. Ver productos con pocas existencias
    8. Añadir/eliminar existencias
    9. <-Atras
    Seleccione una opción: ''',
    'menu_receta' : '''
    Menú Receta
    1. Ver recetas
    2. Buscar receta
    3. Nueva receta
    4. Editar receta
    5. Activar/Desactivar receta en menú
    6. Ver mejores recetas
    7. <-Atras
    Seleccione una opción: ''',
    'menu_pedio_chef' : '''
    Menú Pedido
    1. ver pedidos a mi cargo
    2. Buscar pedidos
    3. Editar pedido
    4. Eliminar Pedido
    5. Tomar pedido
    6. <-Atras
    Seleccione una opción: ''',
    'menu_pedio_admin' : '''
    Menú Pedido
    1. ver mis pedidos
    2. Buscar pedidos
    3. Nuevo Pedido
    4. Editar pedido
    5. Eliminar Pedido
    6. Tomar pedido
    7. <-Atras
    Seleccione una opción: ''',
    'menu_pedio_user' : '''
    Menú Pedido
    1. ver mis pedidos
    2. Nuevo Pedido
    3. <-Atras
    Seleccione una opción: ''',
    'user_duplicated' : 'Usuario existente',
    'chef_duplicated' : 'Chef existente',
    'edit_my_user' : '''
    Modificar:
    1. Nombre
    2. Contraseña
    3. Fecha nacimiento
    4. <-Atras
    Seleccione una opción: ''',
    'old_password' : 'Ingrese la vieja contraseña: ',
    'new_password' : 'Ingrese la nueva contraseña: ',
    'wrong_password' : 'Contraseña incorrecta',
    'status' : '''
    Cambiar estado:
    1. Activar
    2. Desactivar
    Seleccione una opción: ''',
    'status_inactive' : '''
    Esta seguro de querer desactivar su usuario?
    1. Si
    2. No
    Seleccione una opción: ''',
    'login_way' : '''
    Iniciar como:
    1. Usuario
    2. Chef
    Seleccione una opción: ''',
    'search_chef' : '''
    Buscar chef por:
    1. email
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'chef_not_found' : 'Chef no encontrado',
    'chef_promote' : '''
    Esta seguro de querer promover al usuario?
    1. Si
    2. No
    Seleccione una opción: ''',
    'search_producto' : '''
    Buscar producto por:
    1. Código
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'code' : 'Ingrese el codigo: ',
    'code_not_found' : 'Codigo no encontrado',
    'quantity' : 'Ingrese la cantidad: ',
    'measurement' : '''
    Tipo de medicion:
    1. N/A
    2. ml
    3. gr
    Seleccione una opción: ''',
    'unlimited' : '''
    Ilimitado?
    1. Si
    2. No
    Seleccione una opción: ''',
    'producto_pattern' : '''
    Código: %s
    Nombre: %s
    Cantidad: %s %s
    Estado: %s
    Menú:
    ''',
    'producto_pattern_user' : '''
    Código: %s
    Nombre: %s
    ''',
    'text_unlimited': 'Ilimitado',
    'search_producto_header' : '# codigo nombre', 
    'edit_producto' : '''
    Modificar
    1. Nombre
    2. cantidad
    3. medicion
    4. ilimitado
    5. <-Atras
    Seleccione una opción: ''',
    'operator' :'''
    Desea:
    +. Sumar
    -. Restar
    Seleccione una opción: ''',
    'receta_pattern' : '''
    Código: %s
    Nombre: %s
    Tiempo: %d min
    Estado: %s
    ''',
    'detalle_receta_pattern' : 'Código: %s Nombre: %s Cantidad: %d %s',
    'search_receta' : '''
    Buscar receta por:
    1. Código
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'search_receta_header' : '# codigo nombre', 
    'time' : 'Ingrese el tiempo de preparacion: ',
    'new_detalle_receta' :'''
    1. Agregar Ingredientes
    2. Editar cantidades
    3. Eliminar Ingredientes
    4. Finalizar
    Seleccione una opción: ''',
    'detalle_receta_header' : '# cantidad nombre',
    'edit_receta' : '''
    Modificar:
    1. Nombre
    2. Tiempo
    3. Agregar Ingrediente
    4. Modificar cantidad
    5. Eliminar Ingrediente
    6. <-Atras
    Seleccione una opción: ''',
    'str_see_producto_header' : 'Codigo Nombre       Estado  Menú\n',
    'str_see_producto' : '%s %s %s %s \n',
    'format_3_str' : '%s %s %s \n'
    'status_menu' : '''
    Activar/Desactivar en menú:
    1. Activar
    2. Desactivar
    Seleccione una opción: ''',
    'str_see_low_producto_header' : 'Codigo Nombre       cantidad \n',
    'str_see_low_producto' : '%s %s %d %s \n',
    'str_see_receta_header' : 'Codigo Nombre       Estado  Menú\n',
    'str_see_receta' : '%s %s %s %s \n',




    'menu_calificacion' : '''
    Menú Calificaciónes
    1. Ver calificación
    2. Agregar calificación
    3. Modificar calificación
    4. Eliminar calificación
    5. <-Atras
    ''',
    
    
    
    
    
    
    
    #Pedido
    'editar_pedido' : '''
    Escoja una opcion a modificar:
    1. Descripcion
    2. Agregar Ingrediente
    3. Cambiar Contraseña
    4. <-Atras
    ''',
    'detallePedido' : '''
    1. Agregar producto
    2. Agregar receta
    3. Editar cantidades
    4. Eliminar del pedido
    5. Finalizar
    ''',
    'descripcion' : 'Ingrese la descripción',
    'ver_pedido' : '''
    1. Buscar por código
    2. <-Atras
    ''',
    'formatoPedido' : '''
    Código: %s
    fecha: %s
    descripcion: %s
    usuario: %s
    chef: %s
    ''',
    'yesNo' : '''
    Esta seguro?
    1. Si
    2. No
    ''',
    
    
    
    }