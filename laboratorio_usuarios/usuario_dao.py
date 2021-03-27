from usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import logger

class UsuarioDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad Usuario
    '''
    __SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s,%s)'
    __ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    __ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
       with CursorDelPool() as cursor:  
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)   
            return usuarios   
    
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'usuario a insertar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
            
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'usuario a actualizar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password(), usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
       
            
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor: 
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'usuario a eliminar: {usuario}')
            valores = (usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount              
    
if __name__ == '__main__':
    #Listado de usuarios
    #usuarios = UsuarioDao.seleccionar()    
    #for usuario in usuarios:
    #    logger.debug(usuario)
    
    #Insertamos un nuevo registro
    #usuario = Usuario(username='Elyta', password='Elynda')
    #usuarios_insertadas = UsuarioDao.insertar(usuario)
    #logger.debug(f'usuarios insertados: {usuarios_insertadas}')
    
    #Actualizar un registro existente
    #usuario = Usuario(1,'Jorge','cokkin')
    #usuarios_actualizadas = UsuarioDao.actualizar(usuario)
    #logger.debug(f'usuarios actualizadas: {usuarios_actualizadas}')
    
    #eliminar un registro existente
    usuario = Usuario(id_usuario=1)
    usuarios_eliminadas = UsuarioDao.eliminar(usuario)
    logger.debug(f'usuarios eliminadas: {usuarios_eliminadas}')