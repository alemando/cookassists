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
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Calificaciones
    5. Menu Chefs
    6. Menu Usuarios
    7. Menu Idiomas
    8. Menu Datos
    9. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_chef' : '''
    Menú
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Chefs
    5. Menu Usuario
    6. Menu Idiomas
    7. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_user' : '''
    Menú
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Calificaciones
    5. Menu Chefs
    6. Menu Usuario
    7. Menu Idiomas
    8. Cerrar Sesión
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
    1. Buscar usuario
    2. Nuevo usuario
    3. Editar mi usuario
    4. Cambiar permisos
    5. Activar/Desactivar usuario
    6. <-Atras
    Seleccione una opción: ''',
    'menu_usuario_admin_is_chef': '''
    Menú Usuario
    1. Buscar usuario
    2. Nuevo usuario
    3. Editar mi usuario
    4. Cambiar permisos
    5. Activar/Desactivar usuario
    6. Cambiar modo de inicio
    7. <-Atras
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
    'active' : 'Activo',
    'inactive' : 'Inactivo',
    'search_user_header' : '# Email                Nombre',
    'option' : 'Seleccione una opción: ',
    'close' : 'Programa Cerrado',
    'menu_chef_admin' : '''
    Menú Chef
    1. Buscar chef
    2. Nuevo chef
    3. Activar/Desactivar chef
    4. Promover a chef
    5. Ver mejor chef
    6. <-Atras
    Seleccione una opción: ''',
    'menu_chef_user' : '''
    Menú Chef
    1. Ver mejor chef
    2. <-Atras
    Seleccione una opción: ''',
    'menu_producto_chef' : '''
    Menú Productos
    1. Buscar producto
    2. Nuevo producto
    3. Editar producto
    4. Activar/Desactivar producto
    5. Añadir/eliminar existencias
    6. <-Atras
    Seleccione una opción: ''',
    'menu_producto_admin' : '''
    Menú Productos
    1. Buscar producto
    2. Nuevo producto
    3. Editar producto
    4. Activar/Desactivar producto
    5. Añadir/eliminar existencias
    6. <-Atras
    Seleccione una opción: ''',
    'menu_producto_user' : '''
    Menú Productos
    1. Buscar producto
    2. <-Atras
    Seleccione una opción: ''',
    'menu_receta_chef' : '''
    Menú Receta
    1. Buscar receta
    2. Nueva receta
    3. Editar receta
    4. Activar/Desactivar receta
    5. Ver mejores recetas
    6. <-Atras
    Seleccione una opción: ''',
    'menu_receta_admin' : '''
    Menú Receta
    1. Buscar receta
    2. Nueva receta
    3. Editar receta
    4. Activar/Desactivar receta
    5. Ver mejores recetas
    6. <-Atras
    Seleccione una opción: ''',
    'menu_receta_user' : '''
    Menú Receta
    1. Buscar receta
    2. Ver mejores recetas
    3. <-Atras
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
    'important' : '''
    Es necesario?
    1. Si
    2. No
    Seleccione una opción: ''',
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
    Necesario: %s
    Estado: %s
    ''',
    'producto_pattern_user' : '''
    Código: %s
    Nombre: %s
    ''',
    'text_unlimited': 'Ilimitado',
    'search_prducto_header' : '# codigo nombre', 
    'edit_producto' : '''
    Modificar
    1. Nombre
    2. cantidad
    3. necesario
    4. medicion
    5. ilimitado
    6. <-Atras
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
    'detalle_receta_pattern' : '''
    Código: %s Nombre: %s Cantidad: %d %s''',
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