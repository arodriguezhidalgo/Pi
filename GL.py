#!/usr/bin/env python3

from http.client import PRECONDITION_FAILED
from operator import inv
import gmpy2
from PiComputation import PiComputation

class GL(PiComputation):        
    def computePi(self, nMax, verbose = 0):        
            a = number(1.0);
            b = 1.0/sqrt(2);
            s = number(1/4.0);

            for i in range(nMax+1 ):
                out = self.computeOutput(a, s);        
                aNew = arMean(a,b);
                c = a-aNew;

                if verbose:
                    print(a**2/s, aNew**2/s)           
                
                bNew = geoMean(a,b);           

                s = (s- ((2**i)*(c**2)));            
                b = bNew;
                a = aNew; 

                outLower = self.computeOutput(a, s);       
                error = self.getErrorDigits(out, outLower);
                
            return out, error
   
class BB1(PiComputation):
    # Algorithm 2.1 in chapter 2.
    def computePi(self, nMax, verbose = 0):   
        x = sqrt(number(2));
        
        outLower = x;
        outUpper = x+number(2);        
        
        y = sqrt(x);
        x = 1/2*(sqrt(x)+rec_sqrt(x));

        for n in range( 0, nMax):
            outLower = number(2)*outUpper/(y+1);            
            outUpper = outLower*(x+1)/number(2);
            xNew = 1/2*(sqrt(x)+rec_sqrt(x));
            y = (y*sqrt(x)+rec_sqrt(x))/(y+1);
            x = xNew;
        
        return outLower, self.getErrorDigits(outLower, outUpper);

class BB2(PiComputation):
    def computePi(self, nMax):        
        alpha = number(6) - number(4)*sqrt(2);
        k = number(3)-number(2)*sqrt(2);
        piOut = 1/alpha;

        for n in range(nMax+1):            
            piOut = 1/alpha;
                            
            kFake = sqrt(1-k**2);
            k = (1-kFake)/(1+kFake);
            alpha = ((1+k)**2)*alpha-pow2(n+2)*k;
        piNew = 1/alpha;
        
        # We compare our pi digits with the next iteration, which tells
        # us what digits are correct. Then, return the old value.
        return piOut, self.getErrorDigits(piNew, piOut)


class BB4(PiComputation):
    def computePi(self, nMax, verbose = 0):        
        y = sqrt(2)-number(1);
        z = (y**2)*number(2);        
        
        piOld = 1/z;  
        for n in range(nMax+1):
            piOld = 1/z;            
                 
            aux = root(1-y**4,4);
            y = (1-aux)/(1+aux);
            z = z*(1+y)**4-pow2(2*n+3)*y*(1+y+y**2);

        piNew = 1/z;                        
        return piOld, self.getErrorDigits(piOld, piNew);

def root(x,n):
    return gmpy2.root(x,n);

def pow2(n):
    return gmpy2.exp2(n);

def number(x):
    return gmpy2.mpfr(x);

def rec_sqrt(a):
    return gmpy2.rec_sqrt(a);

def sqrt(a):
    return gmpy2.sqrt(a);

def arMean(a,b):
    return (a+b)/2;    

def geoMean(a,b):
    return sqrt(a*b);
