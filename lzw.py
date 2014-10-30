#!/bin/python3

import string
from collections import OrderedDict

code="ballaballa"

def genASCIIdict():
    dictionary={}
    i=0
    for uc in string.ascii_uppercase:
        dictionary.update({uc:65+i})
        i+=1

    j=0
    for lc in string.ascii_lowercase:
        dictionary.update({lc:97+j})
        j+=1
    return OrderedDict(sorted(dictionary.items()))

def encode(toEncode):
    muster=""
    new_entries_counter=256
    while toEncode!="":
        zeichen=toEncode[0]
        toEncode=toEncode[1:]
        print("PENISPENIS %s"%zeichen)
        if muster+zeichen in dictionary:
            print("muster+zeichen sind in dictionary")
            muster=muster+zeichen
        else:
            dictionary.update({muster+zeichen:new_entries_counter})
            new_entries_counter+=1
            print(muster)
            muster=zeichen
        if muster!="":
            print(muster)
dictionary=genASCIIdict()
encode(code)
print(dictionary)
