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
    'producto_pattern' : '''
    Código: %s
    Nombre: %s
    Cantidad: %s %s
    Estado: %s
    Menú: %s
    ''',
    'producto_pattern_user' : '''
    Código: %s
    Nombre: %s
    ''',
    'search_producto_header' : '# codigo nombre \n', 
    'edit_producto' : '''
    Modificar
    1. Nombre
    2. cantidad
    3. medicion
    4. <-Atras
    Seleccione una opción: ''',
    'operator' :'''
    Desea:
    1. Sumar
    2. Restar
    Seleccione una opción: ''',
    'receta_pattern' : '''
    Código: %s
    Nombre: %s
    Tiempo: %d min
    Estado: %s
    ''',
    'detalle_receta_pattern_header' : 'Código Nombre         Cantidad \n',
    'detalle_receta_pattern' : '%s %s %d %s \n',
    'search_receta' : '''
    Buscar receta por:
    1. Código
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'search_receta_header' : '# codigo nombre \n', 
    'time' : 'Ingrese el tiempo de preparacion en minutos: ',
    'new_detalle_receta' :'''
    1. Agregar Ingredientes
    2. Editar cantidades
    3. Eliminar Ingredientes
    4. Finalizar
    Seleccione una opción: ''',
    'detalle_receta_header' : '# cantidad nombre \n',
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
    'str_menu_producto_header' : 'Codigo Nombre \n',
    'str_menu_producto' : '%s %s \n',
    'format_3_str' : '%s %s %s \n',
    'status_menu' : '''
    Activar/Desactivar en menú:
    1. Activar
    2. Desactivar
    Seleccione una opción: ''',
    'str_see_low_producto_header' : 'Codigo Nombre       cantidad \n',
    'str_see_low_producto' : '%s %s %d %s \n',
    'str_see_receta_header' : 'Codigo Nombre       Tiempo  Menú \n',
    'str_see_receta' : '%s %s %d %s \n',
    'str_menu_receta_header' : 'Codigo Nombre       Tiempo \n',
    'str_menu_receta' : '    %s %s %d \n',
    'str_see_pedido_header' : 'Codigo Fecha  Entregado  Usuario     Chef    \n',
    'str_see_pedido' : '%s %s %s %s %s \n',
    'str_see_my_pedido_header' : 'Codigo Fecha  Entregado     Chef    \n',
    'str_see_my_pedido' : '%s %s %s %s \n',
    'menu_pedido_chef' : '''
    Menú Pedido
    1. Ver pedidos
    2. Buscar pedido
    3. Editar pedido
    4. Ver pedidos pendientes
    5. Tomar pedido
    6. Ver pedidos tomados y sin completar
    7. Completar pedido
    8. <-Atras
    Seleccione una opción: ''',
    'menu_pedido_admin' : '''
    Menú Pedido
    1. Ver pedidos
    2. Ver mis pedidos
    3. Buscar pedido
    4. Nuevo Pedido
    5. Editar pedido
    6. Ver pedidos pendientes
    7. Generar reporte
    8. <-Atras
    Seleccione una opción: ''',
    'menu_pedido_user' : '''
    Menú Pedido
    1. Ver mis pedidos
    2. Nuevo Pedido
    3. <-Atras
    Seleccione una opción: ''',
    'search_pedido' : '''
    Buscar pedido por:
    1. Código
    2. Fecha
    3. <-Atras
    Seleccione una opción: ''',
    'date' : 'Ingrese la fecha(dd/mm/yyyy): ',
    'search_pedido_header' : '# Codigo Fecha   Usuario \n',
    'format_4_str' : '%s %s %s %s \n',
    'detalle_pedido_pattern_header' : 'Código    Nombre         Cantidad \n',
    'detalle_pedido_pattern' : '    %s %s %d \n',
    'pedido_pattern' : '''
    Código: %s
    Fecha: %s
    Usuario: %s
    Chef: %s
    Entregado: %s
    ''',
    'only_unity' : 'Solo puede pedir %d',
    'sorry_receta' : 'Disculpe ya no puede pedir esta receta',
    'description' : 'Algun comentario o descripcion adicional: \n',    
    'sorry_producto' : 'Disculpe ya no puede pedir esta producto',
    'new_detalle_pedido' :'''
    1. Agregar producto
    2. Agregar receta
    3. Editar cantidades
    4. Eliminar del pedido
    5. Finalizar
    Seleccione una opción: ''',
    'detalle_pedido_header' : '# cantidad nombre \n',
    'edit_pedido' : '''
    Modificar:
    1. Descripcion
    2. Agregar producto o receta
    3. <-Atras
    Seleccione una opción: ''',
    'menu_day_chef' : '''
    Menú del día
    1. Ver mejor receta
    2. Ver menu
    3. Activar/Desactivar producto en menú
    4. Activar/Desactivar receta en menú
    5. <-Atras
    Seleccione una opción: ''',
    'menu_day_admin' : '''
    Menú del día
    1. Ver mejor receta
    2. Ver menu
    3. Activar/Desactivar producto en menú
    4. Activar/Desactivar receta en menú
    5. <-Atras
    Seleccione una opción: ''',
    'menu_day_user' : '''
    Menú del día
    1. Ver mejor receta
    2. Ver menu
    3. <-Atras
    Seleccione una opción: ''',
    'menu_day_select' : '''
    1. Ver menu de productos
    2. Ver menu de recetas
    3. <-Atras
    Seleccione una opción: ''',
    'menu_calificacion_admin' : '''
    Menú Calificaciónes
    1. Ver calificaciones
    2. Buscar calificación
    3. Eliminar calificación
    4. Ver mejor recetas
    5. Ver mejor chef
    6. Calificar un pedido
    7. Editar mis calificaciones
    8. Eliminar mis calificaciones
    9. <-Atras
    Seleccione una opción: ''',
    'menu_calificacion_chef' : '''
    Menú Calificaciónes
    1. Ver calificaciones
    2. Ver mejor recetas
    3. Ver mejor chef
    4. <-Atras
    Seleccione una opción: ''',
    'menu_calificacion_user' : '''
    Menú Calificaciónes
    1. Ver calificaciones
    2. Ver mejor recetas
    3. Ver mejor chef
    4. Calificar un pedido
    5. Editar mis calificaciones
    6. Eliminar mis calificaciones
    7. <-Atras
    Seleccione una opción: ''',
    'str_see_calificacion_header' : 'Codigo  Para     Usuario    puntaje\n',
    'str_see_calificacion' : '%s %s %s %d \n',
    'str_see_my_calificacion_header' : 'Codigo  Para         puntaje\n',
    'str_see_my_calificacion' : '%s %s %d \n',
    'receta_pattern_user' : '''
    Código: %s
    Nombre: %s
    ''',
    'rating' : 'Ingrese el puntaje(1 a 5): ',
    'delete_calificacion' : '''
    Esta seguro de borrar calificación?
    1. Si
    2. No
    Seleccione una opción: ''',
    'edit_calificacion' : '''
    Modificar
    1. Puntaje
    2. Descripcion
    3. <-Atras
    Seleccione una opción: ''',
    'search_calificacion' : '''
    Ver calificacion de:
    1. Receta
    2. <-Atras
    Seleccione una opción: ''',
    'calificacion_pattern': '''
    Código: %s
    Para: %s
    Puntaje: %d
    Descripcion: %s
    ''',
    'date_start' : 'Ingrese la fecha de partida(dd/mm/yyyy): ',
    'date_end' : 'Ingrese la fecha de llegada(dd/mm/yyyy): ',
    'str_summary' : 'Nombre      Cantidad \n',
    'new_calificacion' : '''
    1. Ver pedidos que no han sido calificados
    2. Calificar pedido
    3. <-Atras
    Seleccione una opción: ''',
    }