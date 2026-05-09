import logging

def configurar_logger():
    """Configura el sistema de registro de eventos en archivo."""
    logging.basicConfig(
        filename='software_fj.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a' # 'a' para anexar nuevos errores sin borrar los anteriores
    )
    return logging.getLogger("SoftwareFJ")
