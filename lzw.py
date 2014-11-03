#!/bin/python3

import string
from collections import OrderedDict

code="bananenanbau"
#code="ballaballa"

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
    puffer=""
    new_entries_counter=256
    while toEncode!="":
        k=toEncode[0]
        if puffer+k in dictionary:
            print("%s + %s in Tabelle gefunden, puffer erweitern"%(puffer,k))
            puffer+=k
        else:
            print("%s + %s in Tabelle hinzufuegen"%(puffer,k))
            dictionary.update({puffer+k:new_entries_counter})
            print("output: <%s : %s>"%(new_entries_counter, puffer))
            new_entries_counter+=1
            puffer=k
            print("neuer puffer: <%s>\n"%puffer)

        toEncode=toEncode[1:]

dictionary=genASCIIdict()
encode(code)
print(dictionary)
