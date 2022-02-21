#!/usr/bin/env python3
import numpy as np
import gmpy2
from decimal import Decimal
gmpy2.local_context(gmpy2.context(), precision=100);
def GL(nMax, precision, verbose = 0):
    
    with gmpy2.local_context(gmpy2.context(), precision=100) as ctx:
        ctx.precision += precision
        a = gmpy2.mpfr('1.0');
        b = gmpy2.mpfr(1.0/gmpy2.sqrt(2));
        s = gmpy2.mpfr(1/4.0);

        for i in range(nMax+1 ):
            out, error = computeOutput(a, s, precision);        
            aNew = arMean(a,b);
            c = sub(a,aNew);

            if verbose:
               print(prod(a,a)/s, prod(aNew,aNew)/s)           
            
            bNew = geoMean(a,b);           

            s = sub(s, prod(gmpy2.exp2(i),prod(c,c)));            
            b = bNew;
            a = aNew;        
        
        return out, error


def computeOutput(a,s, precision):
    out = div(prod(a,a), s);
    error = sub(out, gmpy2.const_pi(10000));
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

out, error = GL(8, 2000);

#print(f'The value of pi is approximately {out:.64f}. {out-np.pi:.64f}')
print(out)
print(error)