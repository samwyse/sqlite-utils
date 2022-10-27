# Insure maximum compatibility between Python 2 and 3
from __future__ import absolute_import, division, print_function

from .db import Database
from .utils import suggest_column_types

__all__ = ["Database", "suggest_column_types"]
