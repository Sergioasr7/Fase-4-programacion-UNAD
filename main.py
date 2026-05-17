from cliente import Cliente
from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import *
from utils import registrar_error


def separador():
    print("\n" + "=" * 60 + "\n")


print("\nSISTEMA SOFTWARE FJ\n")

# OPERACIÓN 1
try:

    cliente1 = Cliente("Juan Pérez", "juan@gmail.com")
    print(cliente1.mostrar_info())

except Exception as e:
    registrar_error(e)
    print(e)

separador()

# OPERACIÓN 2 - Cliente inválido
try:

    cliente2 = Cliente("", "correo@gmail.com")

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 3 - Correo inválido
try:

    cliente3 = Cliente("Ana", "correo_invalido")

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 4 - Servicio válido
try:

    sala = ReservaSala("Sala VIP", 100)

    print(sala.descripcion())

except Exception as e:
    registrar_error(e)
    print(e)

separador()

# OPERACIÓN 5 - Servicio inválido
try:

    servicio_invalido = AlquilerEquipo(
        "Equipo dañado",
        -50
    )

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 6 - Reserva válida
try:

    reserva1 = Reserva(cliente1, sala, 3)

    reserva1.confirmar()

    costo = reserva1.procesar()

    print(reserva1.mostrar_reserva())

    print(f"Costo total: {costo}")

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 7 - Duración inválida
try:

    reserva2 = Reserva(cliente1, sala, -2)

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 8 - Cancelar reserva
try:

    reserva3 = Reserva(
        cliente1,
        AsesoriaEspecializada(
            "Asesoría Python",
            200
        ),
        2
    )

    reserva3.cancelar()

    print(reserva3.mostrar_reserva())

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 9 - Confirmar cancelada
try:

    reserva3.confirmar()

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

# OPERACIÓN 10 - Polimorfismo
try:

    servicios = [

        ReservaSala("Sala Ejecutiva", 120),

        AlquilerEquipo("Computadores", 80),

        AsesoriaEspecializada(
            "Consultoría IA",
            300
        )
    ]

    for servicio in servicios:

        print(servicio.descripcion())

        print(
            "Costo:",
            servicio.calcular_costo(
                2,
                impuesto=0.19,
                descuento=10
            )
        )

        print()

except Exception as e:
    registrar_error(e)
    print("Error:", e)

separador()

print("El sistema continúa funcionando correctamente.")
