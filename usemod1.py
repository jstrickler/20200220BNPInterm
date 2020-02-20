#!/usr/bin/env python

# from pkg.pkg import module
from bnp.bank import assets

assets.credit("wombat", "weasel")
assets.debit()
assets.check_owner()

s = assets.Spam()
print(s)

assets.debit()
