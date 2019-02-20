import logging


class Log:

    def __init__(self, name, filepath='log.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('%(asctime)s -> %(levelname)s %(name)s: %(message)s')
        self.file_handler = logging.FileHandler(filepath)
        self.file_handler.setFormatter(self.formatter)
        self.logger.addHandler(self.file_handler)

    def log(self, level, message):
        self.logger.log(level, message)

    def debug(self, message):
        return self.log(logging.DEBUG, message)

    def info(self, message):
        return self.log(logging.INFO, message)

    def warning(self, message):
        return self.log(logging.WARNING, message)

    def error(self, message):
        return self.log(logging.ERROR, message)

    def critical(self, message):
        return self.log(logging.CRITICAL, message)


if __name__ == '__main__':
    logger = Log('test', 'self.log')
    logger.debug('Test')
