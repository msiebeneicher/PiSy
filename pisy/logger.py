class Logger(object):
    def __init__(self, verbosity_level = 0):
        self.verbosity_level = verbosity_level

    def info(self, message):
        if self.verbosity_level > 0:
            self._print(message, prefix='INFO:')

    def warn(self, message):
        self._print(message, prefix='WARNING:')

    def error(self, message):
        self._print(message, prefix='ERROR:')

    @staticmethod
    def _print(message, prefix=''):
        final_msg = "%s %s" % (prefix, message)

        print (final_msg.strip())