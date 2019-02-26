# -*- coding: utf-8 -*-

"""Top-level package for Python BINlist."""

__author__ = """Patrick Zhang"""
__email__ = 'patdujour@gmail.com'
__version__ = '0.1.1'

from binlist.iin import BIN
from binlist import network

__all__ = [
    'BIN',
    'network',
]
