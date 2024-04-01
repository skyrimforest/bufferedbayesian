from datetime import datetime
import logging
def get_current_time():
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%m/%d-%H:%M:%S")
    return currentTime

def get_logger(log_name:str):
    logger=logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    log_format = logging.Formatter('%(asctime)s - %(filename)s[%(lineno)d] - %(levelname)s - %(message)s',datefmt="%m/%d-%H:%M:%S")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)

    file_handler = logging.FileHandler(log_name+'.log')
    file_handler.setFormatter(log_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


