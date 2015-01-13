#!/bin/python3

import math

symbols={
        0.08:'1101',
        0.07:'1100',
        0.4:'0',
        0.12:'1111',
        0.1:'1110',
        0.23:'10'
        }

entropy=sum([(p*math.log(1/p,2)) for p in symbols])

avglen=sum([(p*len(code)) for p,code in symbols.items()])

redundancy=avglen-entropy

print("entropy:             %f\naverage code length: %f\nredundancy:          %f" % (entropy,avglen,redundancy))
