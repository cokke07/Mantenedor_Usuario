from logger_base import logger
from psycopg2 import pool
import sys

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None
  
    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                                            cls.__MIN_CON,
                                            cls.__MAX_CON,
                                            host=cls.__HOST,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
                logger.debug(f'Creación pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.error(f'Error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls.__pool
  
    @classmethod
    def obtenerConexion(cls):
        #Obtener una conexion del pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        #Regresar el objeto conexion al pool
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexion al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')

    @classmethod
    def cerrarConexiones(cls):
        #Cerrar el pool y todas sus conexiones
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__pool}')

if __name__ == '__main__':
    #Obtener una conexion a partir del pool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    #Regresamos las conexiones al pool
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    #Cerramos el pool
    Conexion.cerrarConexiones()
    #Si intentamos pedir una conexion de un pool cerrado manda error 
    #conexion3 = Conexion.obtenerConexion()
    