#!/usr/bin/env python3

import gmpy2

class GL:
    def __init__(self, prec):
        self.precision = prec;
        self.ctx = gmpy2.get_context();
        self.ctx.precision = prec;

    def computePi(self, nMax, precision, verbose = 0):        
            a = gmpy2.mpfr('1.0');
            b = gmpy2.mpfr(1.0/gmpy2.sqrt(2));
            s = gmpy2.mpfr(1/4.0);

            for i in range(nMax+1 ):
                out = self.computeOutput(a, s);        
                aNew = arMean(a,b);
                c = sub(a,aNew);

                if verbose:
                    print(prod(a,a)/s, prod(aNew,aNew)/s)           
                
                bNew = geoMean(a,b);           

                s = sub(s, prod(gmpy2.exp2(i),prod(c,c)));            
                b = bNew;
                a = aNew; 

                outLower = self.computeOutput(a, s);       
                error = out-outLower;
            return out, error
    def computeOutput(self, a,s):
        out = div(prod(a,a), s);
        return  out

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
