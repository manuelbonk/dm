#!/bin/python3

from collections import OrderedDict
import ctypes

message="EGHEGFGGEF"

interval=[]

# occurrences of each symbol in a dict
occurrences={x: message.count(x) for x in message}
# print("occurrences as dict:\n%s" % occurrences)

# sort occurrences and transformation to a tuple array
occurrences=sorted({x: message.count(x) for x in message}.items())
# print("occurrences converted as array of tuples:\n%s" % occurrences)

def genInitInterval():
    # generates the initial interval [0,1]
    propabilities=[(x,(o/len(message))) for (x,o) in occurrences]
#    print("\nsymbols are now sorted alphabetically:\n\nsymbol propability")
    l=0
    for (s,p)  in propabilities:
        print('{0:1s}      {1:f}'.format(s,p))
        interval.append([s,l,l+p])
        l+=p
    print("\n%s\n" % interval)

def encode(l,r,toEncode):
    if toEncode=="":
        print('\nresult:\nmessage:       %s\nencoded [dec]: %s\nencoded [bin]: %s'%(message,l,binary(l)))
        return l
    # interval width
    i_width=r-l
    for i in interval:
        if i[0]==toEncode[0]:
            print("symbol: %s"%i)
            l_new=l+i_width*i[1]
            r_new=l_new+i_width*i[2]
            if i_width==1:
                r_new=i[2]

            print('         [dec]    [bin]\ni_width: {4:7f}\nl_new:   {0:7f} {1:33s}\nr_new:   {2:7f} {3:33s}\n'.format(l_new,binary(l_new),r_new,binary(r_new),i_width))
            encode(l_new,r_new,toEncode[1:])

def binary(num):
    return bin(ctypes.c_int.from_buffer(ctypes.c_float(num)).value)

genInitInterval()
encode(0,1,message)
