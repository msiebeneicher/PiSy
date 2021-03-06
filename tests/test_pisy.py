import unittest
import sys
import os

from pisy.main import PiSy


class PiSyTestCase(unittest.TestCase):

    def setUp(self):
        self.source_path = '%s/source' % self._get_mock_folder_dir()
        self.target_path = '/tmp/pisy_test_target'

        if not os.path.isdir(self.target_path):
            os.mkdir(self.target_path)

        sys.argv = ['pisy_path', self.source_path, self.target_path]

    def tearDown(self):
        os.remove('%s/foo/bar.sls' % self.target_path)
        os.remove('%s/foo.sls' % self.target_path)
        os.rmdir('%s/foo' % self.target_path)

    def test_pisy_run(self):
        pisy = PiSy()
        pisy.run()

        self.assertEqual(True, os.path.isfile('%s/foo/bar.sls' % self.target_path))
        self.assertEqual(True, os.path.isfile('%s/foo.sls' % self.target_path))

    @staticmethod
    def _get_mock_folder_dir():
        base_path =  os.path.abspath(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )

        return os.path.join(base_path, 'mocks')


if __name__ == '__main__':
    unittest.main()
