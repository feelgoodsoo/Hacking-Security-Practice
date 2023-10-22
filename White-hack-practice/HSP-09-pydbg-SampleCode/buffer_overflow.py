from ctypes import *
import os
import time

msvcrt = cdll.msvcrt

# Give the debugger time to attach, then hit a button
pid = os.getpid()
raw_input("My PID = %d. Once the debugger is attached, press any key." % pid)

# Create the 5-byte destination buffer
buffer = c_char_p("AAAAA")

# The overflow string
overflow = "A" * 100

# Run the overflow
msvcrt.strcpy(buffer, overflow)

