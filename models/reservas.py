from .dataBase import conection
from .padre import TablaBase


# models/reservas.py

class Reservas(TablaBase):
    campos = ["nombre cliente", "propiedad_id", "fecha_reserva_inicio", "fecha_reserva_fin"]
    @staticmethod
    def crear_tabla():
        conexion = conection()
        cursor = conexion.cursor()
    
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reservas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_cliente TEXT NOT NULL,
                propiedad_id INTEGER NOT NULL,
                fecha_reserva_inicio TEXT NOT NULL,
                fecha_reserva_fin TEXT NOT NULL,
                FOREIGN KEY (propiedad_id) REFERENCES propiedades(id)
            )
        """)
    
        conexion.commit()
        conexion.close()

    @staticmethod
    def insertar(nombre_cliente, propiedad_id, fecha_reserva_inicio, fecha_reserva_fin):
        conexion = conection()
        cursor = conexion.cursor()
    
        cursor.execute("""
            INSERT INTO reservas (
                propiedad_id,
                nombre_cliente,
                fecha_reserva_inicio,
                fecha_reserva_fin
            )
            VALUES (?, ?, ?, ?)
        """, (
            propiedad_id,
            nombre_cliente,
            fecha_reserva_inicio,
            fecha_reserva_fin
        ))
    
        conexion.commit()
        conexion.close()

    @staticmethod
    def leer():
        conexion = conection()
        cursor = conexion.cursor()
        
        cursor.execute("""
            SELECT id, nombre_cliente, fecha_reserva_inicio, fecha_reserva_fin,propiedad_id
            FROM reservas
        """)
        
        registros = cursor.fetchall()
        
        conexion.close()
        
        return registros

    @staticmethod
    def actualizar(id, nombre_cliente, propiedad_id, fecha_reserva_inicio, fecha_reserva_fin):
        conexion = conection()
        cursor = conexion.cursor()

        cursor.execute("""
            UPDATE reservas
            SET nombre_cliente = ?,
            propiedad_id = ?,
            fecha_reserva_inicio = ?,
            fecha_reserva_fin = ?
            WHERE id = ?
        """, (
            nombre_cliente,
            propiedad_id,
            fecha_reserva_inicio,
            fecha_reserva_fin,
            id
        ))

        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_registro):
        conexion = conection()
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM reservas WHERE id = ?",
            (id_registro,)
        )
        conexion.commit()
        conexion.close()