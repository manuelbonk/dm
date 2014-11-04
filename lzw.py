#!/bin/python3

import string
from collections import OrderedDict

code="0012230331130121"
#code="bananenanbau"
#code="ballaballa"

dictionary={}
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
            print("<%s+%s> in Tabelle gefunden, puffer erweitern"%(puffer,k))
            puffer+=k
        else:
            print("<%s+%s> in Tabelle an Stelle <%s> hinzufuegen"%(puffer,k,new_entries_counter))
            dictionary.update({puffer+k:new_entries_counter})
            print("output: <%s:%s>"%(new_entries_counter, puffer))
            new_entries_counter+=1
            puffer=k

        print("neuer puffer: <%s>\n"%puffer)
        toEncode=toEncode[1:]

def printDict(d):

    for key,value in sorted(d.items(), key=lambda x:x[1]):
        print("key: %5s value: %3s"%(key,value))

#dictionary=genASCIIdict()
encode(code)
printDict(dictionary)
