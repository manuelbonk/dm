#!/bin/python3

from collections import OrderedDict
import ctypes

code="EGHEGFGGEF"

# [$symbol, $left, $right]
interval=[]

# occurrences of each symbol in a dict
occurrences={x: code.count(x) for x in code}
print("occurrences as dict: %s" % occurrences)

# sort occurrences and transformation to a tuple array
occurrences=sorted({x: code.count(x) for x in code}.items())
print("occurrences converted as array of tuples: %s" % occurrences)

def genInitInterval():
    propabilities=[(x,(o/len(code))) for (x,o) in occurrences]
    print("\nsymbols are now sorted alphabetically:")
    l=0
    for (s,p)  in propabilities:
        print("symbol: %s propability: %s" % (s,p))
        interval.append([s,l,l+p])
        l+=p
    print("\n",interval,"\n")

def decode(l,r,toDecode):
    if toDecode=="":
        return l
    # interval width
    i_width=r-l
    for i in interval:
        if i[0]==toDecode[0]:
            print("symbol: %s"%i)
            l_new=l+i_width*i[1]
            r_new=l_new+i_width*i[2]
            if i_width==1:
                r_new=i[2]

            print("l_new [dec]: %s  l_new[bin]: %s  r_new[dec]: %s  r_new[bin]: %s  i_width: %s\n" %(l_new,binary(l_new),r_new,binary(r_new),i_width))
            decode(l_new,r_new,toDecode[1:])
#            decode(l+i_width*i[1],r+i_width*i[2],toDecode[1:])

def binary(num):
    return bin(ctypes.c_int.from_buffer(ctypes.c_float(num)).value)

genInitInterval()
decode(0,1,code)
