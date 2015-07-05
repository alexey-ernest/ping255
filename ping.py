"""
Scans ip addresses.
"""

import os
import sys

def main(mask):
    """Prints all hosts which are up in ip range.
    """

    for addr in scan(mask):
        print addr, 'is up!' 

def scan(mask):
    """Scans ip range replacing * by 0-255 values.

    Args:
        mask: 192.168.1.*

    Returns:
        Yields addresses which is up.
    """

    for i in range(0, 256):
        address = mask.replace('*', str(i))
        response = os.system('ping -c 1 -t 1 ' + address + ' >/dev/null 2>&1')
        if response == 0:
            yield address

if __name__ == '__main__':
    MASK = '192.168.1.*'
    if len(sys.argv) > 1:
        MASK = sys.argv[1]
    main(MASK)
