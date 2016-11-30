#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import glob
import os
from os.path import isdir, join
import yaml
import six
import re

from cli import Cli
from logger import Logger


def main():
    pisy = PiSy()
    pisy.run()


class PiSy(object):
    """
    PiSy main class
    """
    def __init__(self):
        self.cli = Cli()
        self.logger = Logger(
            self.cli.get_arg('verbosity_level')
        )

    def run(self):
        self._remove_deprecated_target_files()

        sources = self._read_source_files()
        self._write_target_files(sources)

    def _remove_deprecated_target_files(self):
        """
        remove sls files on target side
        :return: void
        """
        args = self.cli.get_args()
        dir_path = args.get('target')

        files = self._get_sls_files(dir_path)

        for file_path in files:
            self.logger.info('remove "%s"' % file_path)
            os.remove(file_path)

    def _write_target_files(self, sources):
        """
        write sls files on target side with replaced values
        :param sources:
        :return:  void
        """
        args = self.cli.get_args()
        dir_path = args.get('target')

        for key, content in sources.items():
            content = self._replace_secret_values(content)
            target_file = "%s/%s" % (dir_path, key)
            target_file_dir = os.path.dirname(target_file)

            # create directory
            if not os.path.isdir(target_file_dir):
                os.makedirs(target_file_dir)

            # write pillar file
            self.logger.info('adding "%s"' % target_file)
            if content:
                with open(target_file, 'w') as stream:
                    yaml.dump(content, stream, default_flow_style=False, indent=2)
            else:
                with open(target_file, 'w') as stream:
                    stream.write('# no values')
                    stream.close()

    def _replace_secret_values(self, dictionary, replace='PiSy_DUMMY_SECRET_MOCK'):
        """
        loop through dict and replace final string values recursively
        :param dictionary:dict
        :param replace:string
        :return: dict
        """
        if dictionary is None:
            return dictionary

        result = dict()
        for key, value in dictionary.iteritems():
            if isinstance(value, dict):
                result[key] = self._replace_secret_values(value)
            elif isinstance(value, list):
                result[key] = []
                for _ in value:
                    result[key].append(replace)
            elif isinstance(value, tuple):
                result[key] = tuple(replace for n in value)
            elif isinstance(value, six.string_types):
                result[key] = replace
            else:
                result[key] = value

        return result

    def _read_source_files(self):
        """
        read sls files on source side
        :return: dict
        """
        args = self.cli.get_args()
        dir_path = args.get('source')

        files = self._get_sls_files(dir_path)
        result_dict = {}

        for file_path in files:
            file_key = file_path.replace(dir_path, '')

            with open(file_path, 'r') as stream:
                content = stream.read()
                replaced = self._replace_jinja(content)

                try:
                    result_dict[file_key] = yaml.load(replaced)
                except yaml.YAMLError as exc:
                    print(exc)

        return result_dict

    def _get_sls_files(self, path):
        """
        get all sls files recursively by glob
        :param path:
        :return: list
        """
        sls_files = glob.glob("%s/*.sls" % path)

        for f in os.listdir(path):
            sub_path = join(path, f)
            if isdir(sub_path):
                sls_files.extend(self._get_sls_files(sub_path))

        return sls_files

    @staticmethod
    def _replace_jinja(string):
        """
        remove jinja settings to keep yaml valid
        :param string:
        :return: string
        """
        regex = '{%.*?%}'
        replaced = re.sub(regex, '', string, flags=re.DOTALL)

        return replaced


# init main
if __name__ == '__main__':
   main()