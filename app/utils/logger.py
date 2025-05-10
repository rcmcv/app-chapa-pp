import logging

def inicializar_log():
    logging.basicConfig(
        filename="app_chapa_pp.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Sistema iniciado.")
