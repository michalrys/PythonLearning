# 2018-06-18
# InfoShare: day 08.
# M. Ryś
#
# odrobaczanie

def is_a_number(number):
    msg = 'Is a number'
    try:
        int(number)
    except ValueError:
        msg = 'Not a number'
    print(msg)

import pdb;pdb.set_trace()
is_a_number(8)
