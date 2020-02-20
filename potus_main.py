#!/usr/bin/env python
from potus import get_info

for i in 42, 43, 45:
    result = get_info(i)
    print(result['first_name'], result['last_name'], result['dob'])

