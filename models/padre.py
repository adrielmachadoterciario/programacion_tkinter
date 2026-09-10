# models/base.py
from abc import ABC, abstractmethod

class TablaBase(ABC):
    campos: list[str] = []
    @staticmethod
    @abstractmethod
    def crear_tabla():
        ...

    @staticmethod
    @abstractmethod
    def insertar(*args):
        ...

    @staticmethod
    @abstractmethod
    def leer():
        ...

    @staticmethod
    def actualizar(*args):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def eliminar(*args):
        raise NotImplementedError
