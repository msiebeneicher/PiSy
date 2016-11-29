import unittest

from pisy.cli import Cli

class CliTestCase(unittest.TestCase):

    def test_parser__help(self):
        cli = Cli()
        with self.assertRaises(SystemExit):
            cli.get_args(sys_args=['-h'])

    def test_get_args(self):
        cli = Cli()
        parser_args = cli.get_args(sys_args=['/tmp', '/'])

        self.assertEqual(parser_args.get('source'), '/tmp')
        self.assertEqual(parser_args.get('target'), '/')

    def test_get_arg(self):
        cli = Cli()

        self.assertEqual(cli.get_arg('source', sys_args=['/tmp', '/']), '/tmp')
        self.assertEqual(cli.get_arg('target', sys_args=['/tmp', '/']), '/')

    def test_get_verbosity_level(self):
        cli = Cli()

        self.assertEqual(cli.get_arg('verbosity_level', sys_args=['/tmp', '/']), 0)
        self.assertEqual(cli.get_arg('verbosity_level', sys_args=['/tmp', '/', '-v']), 1)

    def test_get_args__invalid(self):
        from argparse import ArgumentTypeError

        cli = Cli()
        with self.assertRaises(ArgumentTypeError):
            cli.get_args(sys_args=['/tmp', '/tmp'])

    def test_get_args__no_directory(self):
        cli = Cli()
        with self.assertRaises(SystemExit):
            cli.get_args(sys_args=['/fooBar', '/tmp'])


if __name__ == '__main__':
    unittest.main()
