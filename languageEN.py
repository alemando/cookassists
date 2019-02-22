class EN:
    '''
    Almacenar en el idioma principal los mensajes 
    para evitar la importacion ciclica
    '''
    men = {}

    english = {
    'language' :'''
    Language:
    1. Spanish
    2. English
    Select an option: ''',
    'sign_off' : 'Closing session',
    'enter' : '''
    Welcome to CookAssist
    are you a?
    1. Registered user
    2. Unregistered user
    3. leave
    Select an option: ''',
    'email' : 'Enter your email: ',
    'password' : 'Enter your password: ',
    'name' : 'Enter your name: ',
    'admin' : '''
    Admin user?
    1. yes
    2. no
    Select an option: ''',
    'born_date' : 'Enter your born date(dd/mm/yyyy): ',
    'user_not_found' : 'User not found',
    'menu_main_admin' : '''
    Menu
    1. Menu of the day
    2. Menu products
    3. Menu recipes
    4. Menu orders
    5. Menu Ratings
    6. Menu Chefs
    7. Menu Users
    8. Menu Language
    9. Menu Data
    10. Sign off
    Select an option: ''',
    'menu_main_chef' : '''
    Menu
    1. Menu of the day
    2. Menu products
    3. Menu recipes
    4. Menu orders
    5. Menu Ratings
    6. Menu Chefs
    7. Menu Users
    8. Menu Language
    9. Sign off
    Select an option: ''',
    'menu_main_user' : '''
    Menu
    1. Menu of the day
    2. Menu orders
    3. Menu ratings
    4. Menu Chefs
    5. Menu Users
    6. Menu Language
    7. Sign off
    Select an option: ''',
    'menu_data' : '''
    Menu data
    1. Add ficticious data
    2. <-back
    Select an option: ''',
    'menu_language' : '''
    Menu language
    1. Change language
    2. <-back
    Select an option: ''',
    'menu_usuario_admin': '''
    Menu User
    1. See users
    2. Search user
    3. New user
    4. Edit my user
    5. Change permits
    6. Active/Inactive user
    7. <-back
    Select an option: ''',
    'menu_usuario_admin_is_chef': '''
    Menu user
    1. See users
    2. Search user
    3. New user
    4. Edit my user
    5. Change permits
    6. Active/Inactive user
    7. Change login way
    8. <-back
    Select an option: ''',
    'menu_usuario_chef': '''
    Menu user
    1. Edit my user
    2. Change login way
    3. <-back
    Select an option: ''',
    'menu_usuario_user': '''
    Menu user
    1. Edit my user
    2. Inactive my user
    3. <-back
    Select an option: ''',
    'menu_usuario_user_is_chef': '''
    Menu user
    1. Edit my user
    2. Inactive my user
    3. Change login way
    4. <-back
    Select an option: ''',
    'search_user' : '''
    Search user by:
    1. email
    2. Nombre
    3. <-back
    Select an option: ''',
    'not_match' : 'No matches were found',
    'yes' : 'Yes',
    'no' : 'NO',
    'str_user' : '''
    Admin: %s
    Name: %s
    email: %s
    Born date: %s
    Status: %s
    ''',
    'str_see_user_header' : 'Name        Email         Status \n',
    'str_see_user' : '%s %s %s \n',
    'active' : 'Active',
    'inactive' : 'Inactive',
    'search_user_header' : '# Email                Name \n',
    'option' : 'Select an option: ',
    'close' : 'Closed program',
    'menu_chef_admin' : '''
    Menu Chef
    1. See Chefs
    2. Search chef
    3. New chef
    4. Active/Inactive chef
    5. Promote a chef
    6. See best chef
    7. <-back
    Select an option: ''',
    'menu_chef_user' : '''
    Menu Chef
    1. See best chef
    2. <-back
    Select an option: ''',
    'menu_producto' : '''
    Menu Products
    1. See products
    2. Search products
    3. New product
    4. Edit product
    5. Active/Inactive product in Menu
    6. Active/Inactive product
    7. See products with few stock
    8. Add/delete stock
    9. <-back
    Select an option: ''',
    'menu_receta' : '''
    Menu recipe
    1. See recipes
    2. Search recipe
    3. Nueva recipe
    4. Edit recipe
    5. Active/Inactive recipe in Menu
    6. See best recipes
    7. <-back
    Select an option: ''',
    'user_duplicated' : 'user duplicated',
    'chef_duplicated' : 'chef duplicated',
    'edit_mi_user' : '''
    Edit:
    1. Name
    2. password
    3. Born date
    4. <-back
    Select an option: ''',
    'old_password' : 'Enter the old password: ',
    'new_password' : 'Enter the new password: ',
    'wrong_password' : 'Wrong password',
    'status' : '''
    Change status:
    1. Active
    2. Inactive
    Select an option: ''',
    'status_inactive' : '''
    Are you sure about inactivate your user?
    1. Yes
    2. No
    Select an option: ''',
    'login_way' : '''
    Login how:
    1. user
    2. Chef
    Select an option: ''',
    'search_chef' : '''
    Search chef by:
    1. email
    2. Name
    3. <-back
    Select an option: ''',
    'chef_not_found' : 'Chef not found',
    'chef_promote' : '''
    Are you sure about promoting the user?
    1. Yes
    2. No
    Select an option: ''',
    'search_producto' : '''
    Search producto by:
    1. Code
    2. Name
    3. <-back
    Select an option: ''',
    'code' : 'Enter the code: ',
    'code_not_found' : 'Code not found',
    'quantity' : 'Enter the quantity: ',
    'measurement' : '''
    Measurement:
    1. N/A
    2. ml
    3. gr
    Select an option: ''',
    'producto_pattern' : '''
    Code: %s
    Name: %s
    Quantity: %s %s
    Status: %s
    Menu: %s
    ''',
    'producto_pattern_user' : '''
    Code: %s
    Name: %s
    ''',
    'search_producto_header' : '# Code Name \n', 
    'edit_producto' : '''
    Edit
    1. Name
    2. Quantity
    3. Measurement
    4. <-back
    Select an option: ''',
    'operator' :'''
    Want:
    1. Add
    2. Substract
    Select an option: ''',
    'receta_pattern' : '''
    Code: %s
    Name: %s
    Time: %d min
    Status: %s
    ''',
    'detalle_receta_pattern_header' : 'Code Name         Quantity \n',
    'detalle_receta_pattern' : '%s %s %d %s \n',
    'search_receta' : '''
    Search recipe by:
    1. Code
    2. Name
    3. <-back
    Select an option: ''',
    'search_receta_header' : '# code name \n', 
    'time' : 'Enter the cooking time in minutes: ',
    'new_detalle_receta' :'''
    1. Add ingredients
    2. Edit Quantitys
    3. Eliminar ingredients
    4. Finish
    Select an option: ''',
    'detalle_receta_header' : '# quantity name \n',
    'edit_receta' : '''
    Edit:
    1. Name
    2. Time
    3. Add ingredients
    4. Edit quantity
    5. Delete ingredients
    6. <-back
    Select an option: ''',
    'str_see_producto_header' : 'Code Name       Status  Menu\n',
    'str_see_producto' : '%s %s %s %s \n',
    'str_menu_producto_header' : 'Code Name \n',
    'str_menu_producto' : '%s %s \n',
    'format_3_str' : '%s %s %s \n',
    'status_menu' : '''
    Active/Inactive in Menu:
    1. Active
    2. Inactive
    Select an option: ''',
    'str_see_low_producto_header' : 'Code Name       quantity \n',
    'str_see_low_producto' : '%s %s %d %s \n',
    'str_see_receta_header' : 'Code Name       Time  Menu \n',
    'str_see_receta' : '%s %s %d %s \n',
    'str_menu_receta_header' : 'Code Name       Time \n',
    'str_menu_receta' : '    %s %s %d \n',
    'str_see_pedido_header' : 'Code Date  Finished  User     Chef    \n',
    'str_see_pedido' : '%s %s %s %s %s \n',
    'str_see_mi_pedido_header' : 'Code Date  Finished     Chef    \n',
    'str_see_mi_pedido' : '%s %s %s %s \n',
    'menu_pedido_chef' : '''
    Menu order
    1. See orders
    2. Search order
    3. Edit order
    4. See pending orders 
    5. Take order
    6. See pending and unfilled orders
    7. Complete order
    8. <-back
    Select an option: ''',
    'menu_pedido_admin' : '''
    Menu Pedido
    1. See orders
    2. See my orders
    3. Search order
    4. New order
    5. Edit order
    6. See pending orders
    7. Generate a report
    8. <-back
    Select an option: ''',
    'menu_pedido_user' : '''
    Menu order
    1. See my orders
    2. New order
    3. <-back
    Select an option: ''',
    'search_pedido' : '''
    Search order by:
    1. Code
    2. Date
    3. <-back
    Select an option: ''',
    'date' : 'Enter the date(dd/mm/yyyy): ',
    'search_pedido_header' : '# Code Date   user \n',
    'format_4_str' : '%s %s %s %s \n',
    'detalle_pedido_pattern_header' : 'Code    Name         quantity \n',
    'detalle_pedido_pattern' : '    %s %s %d \n',
    'pedido_pattern' : '''
    Code: %s
    Date: %s
    User: %s
    Chef: %s
    Finished: %s
    ''',
    'only_unity' : 'Only can order %d',
    'sorry_receta' : "Sorry now you can't order the recipe",
    'description' : 'A comment: \n',    
    'sorry_producto' : "Sorry now you can't order the product",
    'new_detalle_pedido' :'''
    1. Add product
    2. Add recipe
    3. Edit quantitys
    4. Remove from the order
    5. Finish
    Select an option: ''',
    'detalle_pedido_header' : '# quantity name \n',
    'edit_pedido' : '''
    Edit:
    1. Description
    2. Add a product or recipe
    3. <-back
    Select an option: ''',
    'menu_day_chef' : '''
    Menu of the day
    1. See best recipe
    2. See menu
    3. Active/Inactive product in Menu
    4. Active/Inactive recipe in Menu
    5. <-back
    Select an option: ''',
    'menu_day_admin' : '''
    Menu of the day
    1. See best receta
    2. See menu
    3. Active/Inactive product in Menu
    4. Active/Inactive recipe in Menu
    5. <-back
    Select an option: ''',
    'menu_day_user' : '''
    Menu of the day
    1. See best receta
    2. See menu
    3. <-back
    Select an option: ''',
    'menu_day_select' : '''
    1. See menu of products
    2. See menu of recipes
    3. <-back
    Select an option: ''',
    'menu_calificacion_admin' : '''
    Menu Ratings
    1. See ratings
    2. Search rating
    3. Remove rating
    4. See best recetas
    5. See best chef
    6. Rate an order
    7. Edit my ratings
    8. Remove my rating
    9. <-back
    Select an option: ''',
    'menu_calificacion_chef' : '''
    Menu ratings
    1. See ratings
    2. See best recetas
    3. See best chef
    4. <-back
    Select an option: ''',
    'menu_calificacion_user' : '''
    Menu Calificaciónes
    1. See ratings
    2. See best recetas
    3. See best chef
    4. Rate an order
    5. Edit my ratings
    6. Remove my rating
    7. <-back
    Select an option: ''',
    'str_see_calificacion_header' : 'Code  For     user    rating\n',
    'str_see_calificacion' : '%s %s %s %d \n',
    'str_see_mi_calificacion_header' : 'Code  Para         rating\n',
    'str_see_mi_calificacion' : '%s %s %d \n',
    'receta_pattern_user' : '''
    Code: %s
    Name: %s
    ''',
    'rating' : 'Enter the rating(1 a 5): ',
    'delete_calificacion' : '''
    Are you sure about remove a rating?
    1. Yes
    2. No
    Select an option: ''',
    'edit_calificacion' : '''
    Edit
    1. Rating
    2. Description
    3. <-back
    Select an option: ''',
    'search_calificacion' : '''
    See raings of:
    1. Recipe
    2. <-back
    Select an option: ''',
    'calificacion_pattern': '''
    Code: %s
    For: %s
    Rating: %d
    Description: %s
    ''',
    'date_start' : 'Enter the start date(dd/mm/yyyy): ',
    'date_end' : 'Enter the end date(dd/mm/yyyy): ',
    'str_summary' : 'Name      quantity \n',
    'new_calificacion' : '''
    1. See orders that have not been qualified
    2. Rate order
    3. <-back
    Select an option: ''',
    'average' : 'Rating: '
    }