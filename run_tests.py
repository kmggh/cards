#!/usr/bin/python
# Tue 2012-03-06 23:14:28 -0500

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
