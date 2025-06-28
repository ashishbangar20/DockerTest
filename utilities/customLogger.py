import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        logs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'logs'))
        os.makedirs(logs_dir, exist_ok=True)

        log_path = os.path.join(logs_dir, 'automation.log')

        logger = logging.getLogger("automationLogger")
        logger.setLevel(logging.DEBUG)

        if not logger.handlers:
            file_handler = logging.FileHandler(log_path)
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s',
                                          datefmt='%m/%d/%Y %I:%M:%S %p')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
