#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""PiSy Test Suite."""

import unittest
import tests
import sys

if __name__ == '__main__':
    # Load all tests frmo the test module.
    suite = unittest.TestLoader().loadTestsFromModule(tests)
    # Kick off the actual testing.
    ret = not unittest.TextTestRunner(verbosity=3).run(suite).wasSuccessful()
    sys.exit(ret)