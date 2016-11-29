import unittest
import sys
from io import BytesIO

from pisy.logger import Logger


class LoggerTestCase(unittest.TestCase):

    def setUp(self):
        self.sys_stdout = sys.stdout
        self.out = BytesIO()
        sys.stdout = self.out

    def tearDown(self):
        """ restore sys.stdout """
        sys.stdout = self.sys_stdout


    def test_info(self):
        # with verbosity level 0
        logger = Logger(0)
        self.assertEquals(None, logger.info('message'))

        output = self.out.getvalue().strip()
        self.assertEquals('', output)

        # with verbosity level 1
        logger = Logger(1)
        self.assertEquals(None, logger.info('message'))

        output = self.out.getvalue().strip()
        self.assertEquals('INFO: message', output)

    def test_warn(self):
        logger = Logger(0)
        self.assertEquals(None, logger.warn('message'))

        output = self.out.getvalue().strip()
        self.assertEquals('WARNING: message', output)

    def test_error(self):
        logger = Logger(0)
        self.assertEquals(None, logger.error('message'))

        output = self.out.getvalue().strip()
        self.assertEquals('ERROR: message', output)


if __name__ == '__main__':
    unittest.main()
