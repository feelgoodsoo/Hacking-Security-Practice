from pydbg import *
from pydbg.defines import *

import struct
import random

# This is our user defined callback function
def printf_randomizer(dbg):
    
    # kssohn 20220303
    # print('ESP=0x%016x' % dbg.context.Esp)
    # print('EBP=0x%016x' % dbg.context.Ebp)
    # print('EAX=0x%016x' % dbg.context.Eax)
    # offset = 0
    # while offset <= 0xc:
        # stack = dbg.read_process_memory(dbg.context.Esp + offset, 4)
        # stack = struct.unpack("L", stack)[0]
        # print('Stack[0x%016x]=0x%08x' % (dbg.context.Esp + offset, int(stack)))
        # offset += 4
    # Read in the value of the counter at ESP + 0x8 as a DWORD
    parameter_addr = dbg.context.Esp + 0x8
    counter = dbg.read_process_memory(parameter_addr,4)
    
    # When using read_process_memory, it returns a packed binary
    # string, we must first unpack it before we can use it further
    counter = struct.unpack("L",counter)[0]
    print "Counter: %d" % int(counter)
    
    # Generate a random number and pack it into binary format
    # so that it is written correctly back into the process
    random_counter = random.randint(1,100)
    random_counter = struct.pack("L",random_counter)
        
    # Now swap in our random number and resume the process
    # for i in random_counter:
        # print("%02xd," % ord(i))
    dbg.write_process_memory(parameter_addr,random_counter, 4)
        
    return DBG_CONTINUE

# Instantiate the pydbg class
dbg = pydbg()

# Now enter the PID of the printf_loop.py process
pid = raw_input("Enter the printf_loop.py PID: ")

# Attach the debugger to that process
dbg.attach(int(pid))

# Set the breakpoint with the printf_randomizer function
# defined as a callback
printf_address = dbg.func_resolve("msvcrt","printf")
dbg.bp_set(printf_address,description="printf_address",handler=printf_randomizer)

# Resume the process
dbg.run()
