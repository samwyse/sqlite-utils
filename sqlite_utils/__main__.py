# Insure maximum compatibility between Python 2 and 3
from __future__ import absolute_import, division, print_function

from .cli import cli

if __name__ == "__main__":
    cli()
