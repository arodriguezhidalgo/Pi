#!/usr/bin/env python3

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
