#!/usr/bin/env python3

import datetime,os
try:
    import msox3000
except ImportError:
    print("\nmsox3000 library not found.\n\nTry \"pip install msox3000\"\n")
    raise


resource='USB0::2391::6056::MY53041304::INSTR'

"""
I got this resource string by pressing "Utility" button, then "I/O"
softbutton.  

2391 is USB mfgr id (0x0957)
6056 is USB device id (0x17a8)
"""

instr = msox3000.MSOX3000(resource)
instr.open()

# Choosing a filename consistent with gnome-screenshot
t = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
instr.hardcopy(os.path.expanduser('~/Pictures/Scopeshot from %s.png'%t))
