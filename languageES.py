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
    'id_type' : '''
    Tipo de identificación: 
    1. CC
    2. TI
    Ingrese la opcion: ''',
    'id' : 'Ingrese su identificación: ',
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
    5. Menu Usuarios
    6. Menu Chefs
    7. Menu Idiomas
    8. Menu Datos
    9. Cerrar Sesión
    Seleccione una opción: ''',
    'menu_main_chef' : '''
    Menú
    1. Menu Productos
    2. Menu Recetas
    3. Menu Pedidos
    4. Menu Calificaciones
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
    1. Buscar usuario
    2. Nuevo usuario
    3. Editar mi usuario
    4. Editar usuarios
    5. Activar/Desactivar usuario
    Seleccione una opción: ''',
    'menu_usuario_admin_is_chef': '''
    Menú Usuario
    1. Buscar usuario
    2. Nuevo usuario
    3. Editar mi usuario
    4. Editar usuarios
    5. Activar/Desactivar usuario
    6. Cambiar modo de inicio
    Seleccione una opción: ''',
    'menu_usuario_chef': '''
    Menú Usuario
    1. Editar mi usuario
    2. Cambiar modo de inicio
    Seleccione una opción: ''',
    'menu_usuario_user': '''
    Menú Usuario
    1. Editar mi usuario
    2. Desactivar mi usuario
    Seleccione una opción: ''',
    'menu_usuario_user_is_chef': '''
    Menú Usuario
    1. Editar mi usuario
    2. Desactivar mi usuario
    3. Cambiar modo de inicio
    Seleccione una opción: ''',
    'user_not_found' : 'Usuario no encontrado',
    'search_user' : '''
    Buscar usuario por:
    1. Identifaciòn
    2. Nombre
    3. <-Atras
    Seleccione una opción: ''',
    'not_match' : 'Nó se encontraron coincidencias',
    'yes' : 'Si',
    'no' : 'NO',
    'str_user' : '''
    Usuario: %s
    Nombre: %s
    Identificación: %s %s
    Fecha nacimiento: %s
    Estado: %s
    ''',
    'active' : 'Activo',
    'inactive' : 'Inactivo'
    'search_user_header' : '# Tipo ID         Nombre'
    'option' : 'Seleccione una opción: ',
    'close' : 'Programa Cerrado',



    'menu_producto' : '''
    Menú Productos
    1. Ver producto
    2. Agregar producto
    3. Modificar producto
    4. <-Atras
    ''',
    'ver_producto' : '''
    1. Buscar producto por código
    2. Buscar producto por nombre
    3. <-Atras
    ''',
    'menu_chef' : '''
    Menú Chefs
    1. Ver chef
    2. Agregar chef
    3. Modificar chef
    4. Eliminar chef
    5. <-Atras
    ''',
    'menu_calificacion' : '''
    Menú Calificaciónes
    1. Ver calificación
    2. Agregar calificación
    3. Modificar calificación
    4. Eliminar calificación
    5. <-Atras
    ''',
    
    'opcionNoValida': '{0} no es una opcion valida',
    
    
    #Mensajes de producto
    'opcionesProducto' : '# codigo nombre', 
    'codigo' : 'Ingrese el codigo: ',
    'editar_producto' : '''
    Escoja una opcion a modificar:
    1. Nombre
    2. Categoria
    3. cantidad
    4. necesario
    5. edicion
    6. ilimitado
    7. <-Atras
    ''',
    'categoria' : '''
    Categoria:
    Escoja una opcion
    1. Basicos
    2. Pastas
    3. Liquidos
    4. Snacks
    5. Bebidas
    Seleccione una opción: 
    ''',
    'cantidad' : 'Ingrese la cantidad: ',
    'necesario' : '''
    Es necesario?
    1. Si
    2. No
    ''',
    'medicion' : '''
    Tipo de medicion:
    Escoja una opcion
    1. N/A
    2. ml
    3. gr
    Seleccione una opción: 
    ''',
    'ilimitado' : '''
    Ilimitado?
    1. Si
    2. No
    ''',
    'codeNotFound' : 'codigo no encontrado',
    'formatoProducto' : '''
    Código: %s
    Nombre: %s
    Categoria: %s
    Cantidad: %s %s
    Necesario: %s
    ''',
    #Receta
    'editar_receta' : '''
    Escoja una opcion a modificar:
    1. Nombre
    2. Tiempo
    3. Agregar Ingrediente
    4. Modificar cantidad
    5. Eliminar Ingrediente
    6. <-Atras
    ''',
    'opcionesReceta' : '# codigo nombre', 
    'menu_receta' : '''
    Menú Receta
    1. Ver receta
    2. Agregar receta
    3. Modificar receta
    4. <-Atras
    ''',
    'cabeceraDetalle' : '# cantidad nombre',
    'formatoDetalleReceta' : '''
    Código: %s Nombre: %s Cantidad: %s %s
    ''',
    'formatoReceta' : '''
    Código: %s
    Nombre: %s
    Tiempo: %d
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
    'formatoDetallePedido' : '''
    Código: %s Nombre: %s Cantidad: %d
    ''',
    'formatoPedido' : '''
    Código: %s
    fecha: %s
    descripcion: %s
    usuario: %s
    chef: %s
    ''',
    #Mensaje, producto
    'nombre' : 'Digite el nombre: ',
    'fecha_nac' : 'Digite la fecha de nacimiento(dd/mm/yyyy): ',
    'contrasena' : 'Digite la contraseña: ',
    'idFound' : 'Identificación existente',
    'oldContrasena' : 'Ingrese la vieja contraseña: ',
    'newContrasena' : 'Ingrese la nueva contraseña: ',
    'wrongContrasena' : 'Contraseña incorrecta',
    'yesNo' : '''
    Esta seguro?
    1. Si
    2. No
    ''',
    'ver_receta' : '''
    1. Buscar por código
    2. Buscar por nombre
    3. <-Atras
    ''',
    'tiempo' : 'Ingrese el tiempo de preparacion: ',
    'detalleReceta' :'''
    1. Agregar Ingredientes
    2. Editar cantidades
    3. Eliminar Ingredientes
    4. Finalizar
    '''
    }