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
    message=toEncode
    dictionary=init_dictionary
    puffer=""
    encoded=[]
    nec=new_entries_counter
    while toEncode!="":
        k=toEncode[0]
        print("puffer: <%s>"%puffer)
        print("k: <%s>"%k)
        if str(puffer)+str(k) in dictionary:
            print("<%s+%s> in Tabelle gefunden, puffer erweitern"%(puffer,k))
            puffer+=str(k)
        else:
            print("<%s+%s> in Tabelle an Stelle <%s> hinzufuegen"%(puffer,k,nec))
            dictionary.update({str(puffer)+str(k):nec})
#            print("dictionary: <%s>\n\npuffer: <%s>\n\n"%(dictionary,puffer))
            encoded.append(dictionary[puffer])
            print("output: %s"%dictionary[puffer])
            nec+=1
            puffer=k

        print("neuer puffer: <%s>\n\n"%puffer)
        toEncode=toEncode[1:]
    printDict(dictionary)
    print("\nmessage: <%s>\nLZW encoded message: <%s>\nbinary LZW encoded message: <%4s>" %(message,encoded,['{0:04b}'.format(x) for x in encoded]))

def printDict(d):

    for key,value in sorted(d.items(), key=lambda x:x[1]):
        print("key: %5s value: %3s"%(key,value))

# Anfangsalphabet darf nicht leer sein. (Keine Ahnung, ob das allgemein für LZW gilt oder nur für meinen Code)
#encode("bananenanbau",genASCIIdict(),256)
#encode("ballaballa",genASCIIdict(),256)
encode("0012230331130121",{'0':0,'1':1,'2':2,'3':3},4)
