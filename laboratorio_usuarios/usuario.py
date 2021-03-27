from logger_base import logger

class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password
        
    def __str__(self):
        return (
            f'Id Usuario: {self.__id_usuario}, '
            f'username: {self.__username}, '
            f'password: {self.__password} '
                    )

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_id_usuario(self):
        return self.__id_usuario

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario


if __name__ == '__main__':
    Usuario1 = Usuario(1, 'Juan', 'Perez', 'email')
    logger.debug(Usuario1)
    # simulando un objeto a insertar de tipo Usuario
    Usuario2 = Usuario(username='Karla', password='Gomez',
                       email='kgomez@mail.com')
    logger.debug(Usuario2)
    # simular el caso de eliminar un objeto de tipo Usuario
    Usuario3 = Usuario(id_usuario=3)
    logger.debug(Usuario3)
