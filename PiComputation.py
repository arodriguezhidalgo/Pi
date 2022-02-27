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

    def getPrecision(self):
        return self.__precision;

    def getContext(self):
        return self.__ctx;
