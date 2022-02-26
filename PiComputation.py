#!/usr/bin/env python3

import gmpy2
from abc import ABC

class PiComputation(ABC):
    def __init__(self, prec):
        self.__precision = prec;
        self.__ctx = gmpy2.get_context();
        self.__ctx.precision = prec;

    def computePi(self, nMax, verbose = 0):        
        pass

    def getErrorDigits(self, outUpper, outLower):
        error = outUpper - outLower;
        return gmpy2.digits(error)[1]-1; # The output is similar to 0.21e-20, so we need to do -1.

    def computeOutput(self, a,s):
        out = div(prod(a,a), s);
        return  out

    def getPrecision(self):
        return self.__precision;

    def getContext(self):
        return self.__ctx;

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
