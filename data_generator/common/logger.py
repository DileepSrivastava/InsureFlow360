import logger
import os

def get_logger(name:str):

    log_folder = "data_generator/logs"

    os.makedirs(log_folder, exist_ok=True)
    