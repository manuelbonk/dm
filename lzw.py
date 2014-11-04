#!/bin/python3

import string
from collections import OrderedDict

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

def encode(toEncode,init_dictionary,new_entries_counter):
    dictionary=init_dictionary
    puffer=""
    nec=new_entries_counter
    while toEncode!="":
        k=toEncode[0]
        if str(puffer)+str(k) in dictionary:
            print("<%s+%s> in Tabelle gefunden, puffer erweitern"%(puffer,k))
            puffer+=str(k)
            print("PUFFFFFFER %s"%puffer)
        else:
            print("<%s+%s> in Tabelle an Stelle <%s> hinzufuegen"%(puffer,k,nec))
            dictionary.update({str(puffer)+str(k):nec})
            print("output: <%s:%s>"%(dictionary[puffer], puffer))
            nec+=1
            puffer=k

        print("neuer puffer: <%s>\n"%puffer)
        toEncode=toEncode[1:]
    printDict(dictionary)

def printDict(d):

    for key,value in sorted(d.items(), key=lambda x:x[1]):
        print("key: %5s value: %3s"%(key,value))

encode("bananenanbau",genASCIIdict(),256)
#encode("ballaballa",genASCIIdict(),256)
#encode("0012230331130121",{},0)
