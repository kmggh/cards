#!/usr/bin/python
# Copyright (C) 2013 by Ken Guyton.  All Rights Reserved.

"""Run all tests."""

import os

TESTS = ('cards', 'player', 'hand')


def run_test(test_name):
  """Run a particular test."""

  print 'Running %s_test...' % test_name
  os.system('./test_%s.py' % test_name)
  print


def main():
  """Run all tests."""

  for test_name in TESTS:
    run_test(test_name)


if __name__ == '__main__':
  main()
