#!/bin/python3

import string

def genASCIIdict():
    # Ja, ich weiss, das ist keine vollstaendige ASCII-Tabelle, aber zumindest sind alle Buchstaben und Ziffern abgedeckt
    dictionary={}
    i=0
    for uc in string.ascii_uppercase:
        dictionary.update({uc:65+i})
        i+=1

    j=0
    for lc in string.ascii_lowercase:
        dictionary.update({lc:97+j})
        j+=1

    for k in range(10):
        dictionary.update({str(k):48+k})

    return dictionary

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

        print("neuer puffer: <%s>\n"%puffer)
        toEncode=toEncode[1:]
    printDict(dictionary)
    print("\nmessage: <%s>\nLZW encoded message: <%s>\nbinary LZW encoded message: <%4s>\n" %(message,encoded,['{0:04b}'.format(x) for x in encoded]))
    # returns LZW encoded message in binary code
    return ['{0:8b}'.format(x) for x in encoded]

def printDict(d):

    print("dictionary:")
    for key,value in sorted(d.items(), key=lambda x:x[1]):
        print("key: %5s value: %3s"%(key,value))

def convertToASCII(toConvert):
    result=''.join([str(ord(c)) for c in toConvert])
    resultHex =[ord(c) for c in toConvert]
    resultBin =['{0:08b}'.format(ord(c)) for c in toConvert]
    print("input: <%s>\nhex ASCII codes:    <%s>\nbinary ASCII codes: <%s>"%(toConvert,resultHex,resultBin))
    return resultBin

# Anfangsalphabet darf nicht leer sein. (Keine Ahnung, ob das allgemein für LZW gilt oder nur für meinen Code)
#encode("bananenanbau",genASCIIdict(),256)
#encode("ballaballa",genASCIIdict(),256)

# Aufgabe 1 a) und 1 c)
print("Aufgabe 1 a) und 1 c):\n")
encode("0012230331130121",{'0':0,'1':1,'2':2,'3':3},4)


# Aufgabe 2 a)
task_2a=encode("bobobobowebewe",genASCIIdict(),256)
print("Aufgabe 2a):\n",task_2a,"\n\n")
# Aufgabe 2 b)
print("Aufgabe 2b):")
task_2b=convertToASCII("bobobobowebewe")
print("\nplain (binary) ASCII encoded message: <%s>\n(binary) LZW encoded message: <%s>\nreduction: <%s>"%(task_2b,task_2a,len(task_2a)*9/(len(task_2b)*8)))
