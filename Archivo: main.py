import logging
from modelos import Cliente, ReservaSala, AlquilerEquipo
from excepciones import SoftwareFJError

# Configuración de Logs (Registro de eventos y errores)
logging.basicConfig(
    filename='software_fj.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def ejecutar_sistema():
    print("--- INICIANDO SIMULACIÓN SOFTWARE FJ ---")
    
    # Servicios disponibles
    sala_premium = ReservaSala("Sala de Juntas", 100.0)
    laptop_pro = AlquilerEquipo("Laptop Dell", 25.0)

    # Lista de 10 casos de prueba (Simulando entradas de usuario)
    casos = [
        {"id": "1", "nom": "Juan", "mail": "juan@mail.com", "dur": 2, "serv": sala_premium}, # OK
        {"id": "2", "nom": "Ana", "mail": "ana-error", "dur": 1, "serv": laptop_pro},       # ERROR EMAIL
        {"id": "3", "nom": "Luis", "mail": "luis@mail.com", "dur": -5, "serv": sala_premium}, # ERROR DURACIÓN
        {"id": "4", "nom": "Mafe", "mail": "mafe@mail.com", "dur": 3, "serv": laptop_pro},   # OK
        # ... agrega más casos aquí hasta completar 10
    ]

    for i, datos in enumerate(casos, 1):
        print(f"\nProcesando Operación #{i}...")
        try:
            # Bloque TRY-EXCEPT-ELSE-FINALLY
            cliente = Cliente(datos["id"], datos["nom"], datos["mail"])
            total = datos["serv"].calcular_costo(horas=datos["dur"])
        except (ValueError, SoftwareFJError) as e:
            logging.error(f"Operación #{i} falló: {e}")
            print(f"Resultado: ERROR controlado registrado en log.")
        else:
            logging.info(f"Operación #{i} exitosa. Total: ${total}")
            print(f"Resultado: ÉXITO. Total a pagar: ${total}")
        finally:
            print(f"Operación #{i} finalizada.")

if __name__ == "__main__":
    ejecutar_sistema()
