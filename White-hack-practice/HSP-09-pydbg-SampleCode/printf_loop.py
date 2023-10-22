# printf_loop.py
# this module print out a sentence "Loop iteration <counter value>" on stdout every 2 seconds.
from ctypes import *
import time
import os

msvcrt = cdll.msvcrt
counter = 0
print("[printf_loop]: PID=%d\n" % os.getpid())
while 1:
    # msvcrt.printf("Loop iteration %d!\n" % counter)
    msvcrt.printf("Loop iteration %d!\n", counter)
    time.sleep(2)
    counter += 1
