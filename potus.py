#!/usr/bin/env python

KEYS = ['last_name', 'first_name', 'dob']

def get_info(term_num):
    with open('DATA/presidents.txt') as pres_in:
        for raw_line in pres_in:
            line = raw_line.rstrip()
            fields = line.split(':')
            if int(fields[0]) == term_num:
                # print("fields:", fields)
                # build dictionary
                d = dict(zip(KEYS, fields[1:4]))

                return d

