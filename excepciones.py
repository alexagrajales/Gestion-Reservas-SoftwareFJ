class SoftwareFJError(Exception):
    """Excepción base para el sistema."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Se lanza cuando los parámetros de la reserva no cumplen las reglas."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Se lanza cuando un equipo o sala ya está ocupado."""
    pass
