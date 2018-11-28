#!/usr/bin/env /usr/bin/python3
import sys
from luxon.core.handlers.cmd import Cmd
import tradius.cmd


def main(argv):
    tradius = Cmd('tradius', path='/tmp')
    tradius()

def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))

if __name__ == '__main__':
    entry_point()
