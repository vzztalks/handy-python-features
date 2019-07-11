from handy_features.decorators.singleton_dec import Singleton


@Singleton
class SingletonLogger:

    def __init__(self):
        print("Logger created")

    def log_info_message(self, message):
        print("INFO: {}".format(message))
