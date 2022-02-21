#!/usr/bin/env python3
import numpy as np
import gmpy2
from decimal import Decimal
gmpy2.local_context(gmpy2.context(), precision=100);
def GL(nMax, precision, verbose = 0):
    
    with gmpy2.local_context(gmpy2.context(), precision=100) as ctx:
        ctx.precision += precision
        a = gmpy2.mpfr(float('1.0'));
        b = gmpy2.mpfr(float(1.0/gmpy2.sqrt(2)));
        s = gmpy2.mpfr(float(1/4.0));
        
        

        for i in range(nMax ):
            out, error = computeOutput(a, s);        
            aNew = arMean(a,b);
            c = sub(a,aNew);

            if verbose:
               print(a**2/s, aNew**2/s)
            
            
            bNew = geoMean(a,b);
            out, error = computeOutput(a, s);

            s = sub(s, 2**i*c**2);            
            b = bNew;
            a = aNew;        
        
        return out, error


def computeOutput(a,s):
    out = div(a**2, s);
    error = sub(out, gmpy2.const_pi());
    return  out, error

def add(a,b):
    return gmpy2.add(a,b);

def sub(a,b):
    return gmpy2.sub(a,b);

def div(a,b):
    return gmpy2.div(a,b);

def prod(a,b):
    return gmpy2.mul(a,b);

def sqrt(a):
    return gmpy2.sqrt(a);

def arMean(a,b):
    return div(add(a,b),2);
    

def geoMean(a,b):
    return sqrt(prod(a, b));

out, error = GL(1, 57, 1);

#print(f'The value of pi is approximately {out:.64f}. {out-np.pi:.64f}')
print(out)
print(error)