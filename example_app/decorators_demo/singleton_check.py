from .singleton_logger import SingletonLogger


def singleton_check():

    logger = SingletonLogger.instance()
    logger.log_info_message("from singleton logger")

    logger_2 = SingletonLogger()
    logger_2.log_info_message("from instance")
