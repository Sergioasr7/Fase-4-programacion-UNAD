from excepciones import (
    ReservaError,
    DuracionInvalidaError
)


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):

        if self.estado == "Cancelada":
            raise ReservaError(
                "No se puede confirmar una reserva cancelada."
            )

        self.estado = "Confirmada"

    def cancelar(self):

        if self.estado == "Confirmada":
            raise ReservaError(
                "No se puede cancelar una reserva confirmada."
            )

        self.estado = "Cancelada"

    def procesar(self):

        try:

            costo = self.servicio.calcular_costo(
                self.duracion,
                impuesto=0.19,
                descuento=20
            )

        except Exception as e:

            raise ReservaError(
                "Error al procesar la reserva."
            ) from e

        else:

            return costo

        finally:

            print("Proceso de reserva finalizado.")

    def mostrar_reserva(self):

        return (
            f"{self.cliente.get_nombre()} | "
            f"{self.servicio.nombre} | "
            f"Estado: {self.estado}"
        )
