from .dataBase import conection
from .padre import TablaBase

class Propiedades(TablaBase):
    campos = ["nombre", "direccion", "precio"]
    @staticmethod
    def crear_tabla():
        conexion = conection()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS propiedades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                direccion TEXT NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conexion.commit()
        conexion.close()

    @staticmethod
    def insertar(nombre, direccion, precio):
        conexion = conection()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO propiedades (nombre, direccion, precio) VALUES (?, ?, ?)",
            (nombre, direccion, precio)
        )
        conexion.commit()
        conexion.close()

    @staticmethod
    def leer():
        conexion = conection()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM propiedades")
        registros = cursor.fetchall()
        conexion.close()
        return registros
    @staticmethod
    def actualizar(id, nombre, direccion, precio):
        conexion = conection()
        cursor = conexion.cursor()

        cursor.execute("""
        UPDATE propiedades
        SET nombre = ?,
            direccion = ?,
            precio = ?
        WHERE id = ?
        """, (nombre, direccion, precio, id))

        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_registro):
        conexion = conection()
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM propiedades WHERE id = ?",
            (id_registro,)
        )
        conexion.commit()
        conexion.close()