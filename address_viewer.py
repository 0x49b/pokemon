import sys
import functools


def printValues(addr, values):
    
    valstr = ""

    for val in values:
        valstr = valstr + val #.rstrip("L").lstrip("0x") + " " or "00"
    
    print(addr, " = ", valstr)

with open(sys.argv[1], 'rb+') as f:
    ram = bytearray(f.read())

    addr = hex(int(sys.argv[2], 16))

    values = []

    for k, i in enumerate(ram):
        if hex(k) == addr:
            
            values.append(hex(ram[k])  )
            values.append(hex(ram[k+1]))
            values.append(hex(ram[k+2]))
            values.append(hex(ram[k+3]))
            values.append(hex(ram[k+4]))
            values.append(hex(ram[k+5]))
            values.append(hex(ram[k+6]))
            values.append(hex(ram[k+7]))

            #print(hex(k-1), '=', hex(ram[k])  )
            #print(hex(k),   '=', hex(ram[k+1]))
            #print(hex(k+1), '=', hex(ram[k+2]))
            #print(hex(k+2), '=', hex(ram[k+3]))    
    
    printValues(addr, values)


