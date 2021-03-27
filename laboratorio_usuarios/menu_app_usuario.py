from usuario_dao import UsuarioDao
from usuario import Usuario
from logger_base import logger

opcion = None
while opcion != "5":
    print('********MENU APP USUARIO********* ')
    print('Opcion 1: Listar Usuarios')
    print('Opcion 2: Agregar Usuario')
    print('Opcion 3: Actualizar Usuario')
    print('Opcion 4: Eliminar Usuario')
    print('Opcion 5: Salir')
    opcion = input("Escribe tu opción (1-5): ")
    if opcion == "1":
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            logger.info(usuario)
    elif opcion == "2":
        username_var = input('Escribe el username: ')
        password_var = input('Escribe el password: ')
        usuario = Usuario(username=username_var, password=password_var)
        usuarios_insertadas = UsuarioDao.insertar(usuario)
        logger.info(f'Usuarios insertados: {usuarios_insertadas}')    
    elif opcion == "3":
        id_usuario_var = int(input('Escribe el id_usuario a modificar: '))
        username_var = input('Escribe el nuevo username: ')
        password_var = input('Escribe el nuevo password: ')
        
        usuario = Usuario(id_usuario_var, username_var, password_var)
        usuarios_actualizadas = UsuarioDao.actualizar(usuario)
        logger.info(f'Usuarios actualizadas: {usuarios_actualizadas}')
    elif opcion == "4":
        id_usuario_var = int(input('Escribe el id_usuario a eliminar: '))
        usuario = Usuario(id_usuario_var)
        usuarios_eliminadas = UsuarioDao.eliminar(usuario)
        logger.info(f'Usuarios eliminadas: {usuarios_eliminadas}')
else:
    print("Salimos del programa...")