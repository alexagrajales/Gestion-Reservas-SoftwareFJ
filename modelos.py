from abc import ABC, abstractmethod
from excepciones import ReservaInvalidaError

class Entidad(ABC):
    @abstractmethod
    def mostrar_detalle(self):
        pass

class Cliente(Entidad):
    def __init__(self, id_cliente, nombre, email):
        # Encapsulamiento con validación básica
        if "@" not in email:
            raise ValueError("Email del cliente no tiene formato válido.")
        self.__id = id_cliente  # Privado
        self.nombre = nombre
        self.email = email

    def mostrar_detalle(self):
        return f"Cliente: {self.nombre} (ID: {self.__id})"

class Servicio(ABC):
    def __init__(self, nombre_servicio, costo_base):
        self.nombre_servicio = nombre_servicio
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        # Sobrescritura de método (Polimorfismo)
        if horas <= 0: raise ReservaInvalidaError("Horas deben ser positivas")
        return self.costo_base * horas

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1):
        # Diferente lógica de cálculo
        return (self.costo_base * dias) + 15.0  # + Costo de seguro fijo
