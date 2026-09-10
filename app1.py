import tkinter as tk
from tkinter import ttk

from models.propiedades import Propiedades
from models.reservas import Reservas

Propiedades.crear_tabla()
ventana = tk.Tk()
ventana.title("gestor de reservas !!")

TABLAS = {
    "Propiedades": Propiedades,
    "Reservas": Reservas
}

# Pestañas para seleccionar tabla
tabs = ttk.Notebook(ventana)
tabs.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

for nombre_tabla in TABLAS.keys():
    frame = tk.Frame(tabs)
    tabs.add(frame, text=nombre_tabla)

tabs.bind("<<NotebookTabChanged>>", lambda evento: habilitar_formulario())

def obtener_tabla_seleccionada():
    indice = tabs.index(tabs.select())
    return tabs.tab(indice, "text")

# Crear la tabla visual
tree = ttk.Treeview(ventana)
tree.grid(row=10, column=0, columnspan=2, padx=2, pady=10)

entradas = []


def habilitar_formulario():
    for widget in ventana.grid_slaves():
        if int(widget.grid_info()["row"]) > 1 and widget != tree:
            widget.destroy()

    entradas.clear()

    tabla = obtener_tabla_seleccionada()
    clase = TABLAS[tabla]
    campos = clase.campos

    for i, campo in enumerate(campos):
        etiqueta = tk.Label(ventana, text=campo)
        etiqueta.grid(row=i + 2, column=0, padx=10, pady=5)

        entrada = tk.Entry(ventana)
        entrada.grid(row=i + 2, column=1, padx=10, pady=5)

        entradas.append(entrada)

    boton_submit = tk.Button(ventana, text="Guardar", command=submit)
    boton_submit.grid(row=len(campos) + 2, column=0, pady=10)

    boton_actualizar = tk.Button(ventana, text="Modificar", command=actualizar)
    boton_actualizar.grid(row=len(campos) + 2, column=0, columnspan=2, pady=10)

    boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_registro)
    boton_eliminar.grid(row=len(campos) + 2, column=1, pady=10)

    mostrar_registros()


def limpiar_entradas():
    for entrada in entradas:
        entrada.delete(0, tk.END)


def submit():
    tabla = obtener_tabla_seleccionada()
    valores = [entrada.get() for entrada in entradas]

    clase = TABLAS[tabla]
    clase.insertar(*valores)

    limpiar_entradas()
    mostrar_registros()
    print("Registro insertado correctamente")


def mostrar_registros():
    tabla = obtener_tabla_seleccionada()
    clase = TABLAS[tabla]
    registros = clase.leer()

    tree.delete(*tree.get_children())

    columnas = ["id"] + clase.campos
    identificadores = [f"col{i}" for i in range(len(columnas))]

    tree["columns"] = identificadores
    tree["show"] = "headings"

    for identificador, nombre in zip(identificadores, columnas):
        tree.heading(identificador, text=nombre)
        tree.column(identificador, width=120)

    for registro in registros:
        tree.insert("", tk.END, values=registro)


def actualizar():
    seleccion = tree.selection()

    if not seleccion:
        print("No seleccionaste ningún registro")
        return

    item = tree.item(seleccion[0])
    id_registro = item["values"][0]

    tabla = obtener_tabla_seleccionada()
    clase = TABLAS[tabla]

    valores = [entrada.get() for entrada in entradas]
    clase.actualizar(id_registro, *valores)

    limpiar_entradas()
    mostrar_registros()
    print("Registro actualizado correctamente")


def eliminar_registro():
    seleccion = tree.selection()

    if not seleccion:
        print("No hay ningún registro seleccionado")
        return

    valores = tree.item(seleccion[0], "values")
    id_registro = valores[0]

    tabla = obtener_tabla_seleccionada()
    TABLAS[tabla].eliminar(id_registro)

    mostrar_registros()


habilitar_formulario()
ventana.mainloop()
