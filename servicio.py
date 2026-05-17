from abc import ABC, abstractmethod
from excepciones import ServicioNoDisponibleError


class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        if precio_base <= 0:
            raise ServicioNoDisponibleError(
                "El precio debe ser mayor que cero."
            )

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass


# Servicio 1
class ReservaSala(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        subtotal = self.precio_base * duracion
        total = subtotal + (subtotal * impuesto) - descuento

        return total

    def descripcion(self):
        return "Servicio de reserva de salas."


# Servicio 2
class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        subtotal = (self.precio_base * duracion) + 50
        total = subtotal + (subtotal * impuesto) - descuento

        return total

    def descripcion(self):
        return "Servicio de alquiler de equipos."


# Servicio 3
class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, impuesto=0, descuento=0):

        subtotal = (self.precio_base * duracion) + 100
        total = subtotal + (subtotal * impuesto) - descuento

        return total

    def descripcion(self):
        return "Servicio de asesoría especializada."
