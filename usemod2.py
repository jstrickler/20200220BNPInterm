#!/usr/bin/env python
# import assets
import sys
from bnp.bank.assets import debit, Spam
# from assets import *

debit()

s = Spam()

for path in sys.path:
    print(path)
