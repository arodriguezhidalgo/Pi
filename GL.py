#!/usr/bin/env python3

from http.client import PRECONDITION_FAILED
from operator import inv
import gmpy2
from PiComputation import PiComputation

class GL(PiComputation):        
    def computePi(self, nMax, verbose = 0):        
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
                error = self.getErrorDigits(out, outLower);
                
            return out, error
   
class BB1(PiComputation):
    # Algorithm 2.1 in chapter 2.
    def computePi(self, nMax, verbose = 0):   
        x = sqrt(gmpy2.mpfr('2'));
        
        outLower = x;
        outUpper = add(x, gmpy2.mpfr('2'));        
        
        y = sqrt(x);
        x = gmpy2.div_2exp(1,1)*(sqrt(x)+rec_sqrt(x));

        for n in range( 0, nMax):
            outLower =  gmpy2.mpfr('2')*outUpper/add(y,1);            
            outUpper = outLower*add(x,1)/gmpy2.mpfr('2');
            xNew = gmpy2.div_2exp(1,1)*(sqrt(x)+rec_sqrt(x));
            y = div((y*sqrt(x)+rec_sqrt(x)),(y+1));
            x = xNew;
        
        return outLower, self.getErrorDigits(outLower, outUpper);

class BB2(PiComputation):
    def computePi(self, nMax):        
        alpha = number(6) - number(4)*sqrt(2);
        k = number(3)-number(2)*sqrt(2);
        piOut = 1/alpha;

        for n in range(nMax+1):            
            piOut = div(1, alpha);
                            
            kFake = sqrt(1-prod(k,k));
            k = div(sub(1,kFake), add(1,kFake));
            alpha = square(1+k)*alpha-pow2(n+2)*k;
        piNew = div(1, alpha);
        
        # We compare our pi digits with the next iteration, which tells
        # us what digits are correct. Then, return the old value.
        return piOut, self.getErrorDigits(piNew, piOut)


class BB4(PiComputation):
    def computePi(self, nMax, verbose = 0):        
        y = sqrt(2)-number(1);
        z = square(y)*number(2);        
        
        piOld = 1/z;  
        for n in range(nMax+1):
            piOld = 1/z;            
                 
            aux = root(1-pow4(y),4);
            y = (1-aux)/(1+aux);
            z = z*(1+y)**4-pow2(2*n+3)*y*(1+y+y**2);

        piNew = 1/z;                        
        return piOld, self.getErrorDigits(piOld, piNew);

def pi():
    return gmpy2.const_pi();

def root(x,n):
    return gmpy2.root(x,n);

def pow2(n):
    return gmpy2.exp2(n);

def pow4(x):
    return square(x)*square(x);

def square(x):
    return prod(x,x);

def number(x):
    return gmpy2.mpfr(x);

def rec_sqrt(a):
    return gmpy2.rec_sqrt(a);

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
