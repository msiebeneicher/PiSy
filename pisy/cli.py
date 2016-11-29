import argparse
import os


class Cli(object):

    def __init__(self):
        self.parser = self._init_parser()

    def get_arg(self, key, sys_args=None):
        """
        get arg by key
        :param key: string
        :param sys_args: list
        :return: mixed
        """
        args = self.get_args(sys_args)
        return args.get(key)

    def get_args(self, sys_args=None):
        parser_args = self.parser.parse_args(sys_args)

        verbosity_level = 1 if parser_args.v else 0

        args = {
            'source': parser_args.source[0],
            'target': parser_args.target[0],
            'verbosity_level': verbosity_level,
        }

        self._validate_args(args)

        return args

    def _init_parser(self):
        """
        init the parser
        :return: void
        """
        parser = argparse.ArgumentParser(
            description='synchronise pillars from source to destination folder with dummy values'

        )
        parser.add_argument('source', type=self._is_dir, nargs=1,
                            help='Pillar source path')

        parser.add_argument('target', type=self._is_dir, nargs=1,
                            help='Pillar target path')

        parser.add_argument('-v', action='store_true', default=False,
                            help='Verbosity')

        return parser

    @staticmethod
    def _is_dir(path):
        """
        Checks if a path is an actual directory
        :param path: string
        :return: string
        """
        if not os.path.isdir(path):
            msg = "{0} is not a directory".format(path)
            raise argparse.ArgumentTypeError(msg)
        else:
            return path

    @staticmethod
    def _validate_args(args):
        """
        Validate arguments
        :param args: dict
        :return: void
        """
        if args.get('source') == args.get('target'):
            msg = "Source and target paths can not be the same directory"
            raise argparse.ArgumentTypeError(msg)
