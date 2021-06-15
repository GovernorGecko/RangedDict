"""
    _test.py
"""

from src.rangeddict import RangedDict


rd = RangedDict()
rd[(3, 4)] = 12
print(rd[4])
