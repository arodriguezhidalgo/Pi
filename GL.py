#!/usr/bin/env python3
import numpy as np
from decimal import Decimal
def GL(nMax):
    a = Decimal(1.0);
    b = Decimal(1.0/np.sqrt(2));
    s = Decimal(1/4.0);

    for i in range(nMax-1):
        aNew = arMean(a,b);
        c = a - aNew;
       # print(a**2/s, aNew**2/s)
        
        bNew = geoMean(a,b);
        s = s - 2**i*c**2;

        b = bNew;
        a = aNew;
    return aNew**2/s

def arMean(a,b):
    return (a+b)/2;

def geoMean(a,b):
    return np.sqrt(a*b);

out = GL(10000);

#print(f'The value of pi is approximately {out:.64f}. {out-np.pi:.64f}')
print(out*Decimal(1e6))