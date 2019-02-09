class EN:
    '''
    Almacenar en el idioma principal los mensajes 
    para evitar la importacion ciclica
    '''
    men = {}

    english = {
    'language' : '''
    Language:
    1. Spanish
    2. English
    Select an option: 
    ''',
    'menu' : '''
    Menu
    1. Menu Users
    2. Menu Chefs
    3. Menu Ratings
    4. Menu Data
    5. Menu Language
    6. Exit
    ''',
    'menu_usuario' : '''
    Menu Users
    1. View user
    2. Add user
    3. Update user
    4. Delete user
    5. <-Back
    ''',
    'menu_chef' : '''
    Menu Chefs
    1. View chef
    2. Add chef
    3. Update chef
    4. Delete chef
    5. <-Back
    ''',
    'menu_calificacion' : '''
    Menu Ratings
    1. View rating
    2. Add rating
    3. Update rating
    4. Delete rating
    5. <-Back
    ''',
    'menu_datos' : '''
    Menu Data
    1. Add ficticious data
    2. <-Back
    ''',
    'menu_idioma' : '''
    Menu Languages
    1. Change Language
    2. <-Back
    ''',
    'opcion' : 'Enter an option: ',
    'opcionNoValida' : '{0} is not a correct option',
    'salir' : 'Bye Bye',
    'id' : 'Enter the identification number: ',
    'userNotFound' : 'User not found',
    'formatoUsuario' : '''
    User type: %s
    Name: %s
    identification: %d
    Born date: %s
    ''',
    'formatoProducto' : '''
    Code: %s
    Name: %s
    Category: %s
    Quantity: %d %s
    Required: %s
    ''',
    'nombre' : 'Enter the name: ',
    'fecha_nac' : 'Enter the born date(dd/mm/yyyy): ',
    'contrasena' : 'Enter the password: ',
    'idFound' : 'Identification found',
    'editar_usuario' : '''
    Options
    1. Change name
    2. Change born date
    3. Change password
    4. <-Back
    ''',
    'oldContrasena' : 'Enter the old password: ',
    'newContrasena' : 'Enter the new password: ',
    'wrongContrasena' : 'Wrong password',
    'yesNo' : '''
    Are you sure?
    1. Yes
    2. No
    ''',
    'ver_receta' :'''
    1. Search by code
    2. Search by name
    3. <-Back
    ''',
    'tiempo': 'Enter the preparation time: '
    }
