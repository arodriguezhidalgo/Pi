#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from Algs import GL, BB1, BB2, BB4
from math import pi
from PiComputation import PiComputation

class SystemLevel(unittest.TestCase):

    def setUp(self):        
        # Need to implement a mechanism that determines if higher precision
        # is needed.
        self.precision = 4000; # 100 bits.
        return self

    @parameterized.expand([
       ("GL", lambda x: GL(x), -21),
       ("BB1", lambda x: BB1(x), -21),     
       ("BB2", lambda x: BB2(x), -41),       
       ("BB4", lambda x: BB4(x), -694),   
    ])
    def test_computesKnownError(self, name, SUT, expectedError):
        # If I am not wrong, IEEE 754 gives 52 bits for fractions. This means detecting up to 
        # 1.11x10e-16. Using 4 iterations should give a smaller error than that.
        specimen = SUT(self.precision);

        # Setup
        nIterations = 4;        # 4 
                
        # Exec
        [dummy, returnedError] = specimen.computePi(nIterations);
        
        # Assertion
        self.assertEqual(returnedError, expectedError);        

    @parameterized.expand([
       ("GL", lambda x: GL(x), pi),
       ("BB1", lambda x: BB1(x), pi),       
       ("BB2", lambda x: BB2(x), pi),    
       ("BB4", lambda x: BB4(x), pi),    
    ])
    def test_fairlyGoodPiEstimation(self, name, SUT, expectedPi):
        # We compare our estimation against the one in math library. It should have the 52 bits 
        # mentioned in another tests.

        # Setup        
        specimen = SUT(self.precision);
        nIterations = 4;
        
        # Exec
        [returnedPi, returnedError] = specimen.computePi(nIterations);
        
        # Verification
        self.assertAlmostEqual(returnedPi, expectedPi,15);
        
class UnitLevel(unittest.TestCase):
    @parameterized.expand([
       ("GL", lambda x: GL(x)),   
       ("BB1", lambda x: BB1(x)),    
       ("BB2", lambda x: BB2(x)), 
       ("BB4", lambda x: BB4(x)), 
    ])
    def test_GLObjectIsOfRightClass(self, name, SUT):
        specimen = SUT(1);
        self.assertIsInstance(specimen, PiComputation);

    @parameterized.expand([
       ("GL", lambda x: GL(x)),   
       ("BB1", lambda x: BB1(x)),    
       ("BB2", lambda x: BB2(x)), 
       ("BB4", lambda x: BB4(x)), 
    ])
    def test_canSetPrecision(self, name, SUT):
        expectedPrecision = 1;
        specimen = SUT(expectedPrecision);
        returnedPrecision = specimen.getPrecision();
        self.assertEqual(returnedPrecision, expectedPrecision);

    @parameterized.expand([
       ("GL", lambda x: GL(x)),   
       ("BB1", lambda x: BB1(x)),    
       ("BB2", lambda x: BB2(x)), 
       ("BB4", lambda x: BB4(x)), 
    ])
    def test_gmpContextHasCustomPrecision(self, name, SUT):
        expectedPrecision = 1;
        specimen = SUT(expectedPrecision);
        returnedContext = specimen.getContext();
        self.assertEqual(returnedContext.precision, expectedPrecision);

    @parameterized.expand([
       ("GL", lambda x: GL(x),),
       ("BB1", lambda x: BB1(x)),     
       ("BB2", lambda x: BB2(x)),      
       ("BB4", lambda x: BB4(x)),  
    ])
    def test_returnsCorrectNumberOfDigits(self, name, SUT):
        specimen = SUT(5);
        expectedDigits = -1;

        returnedDigits= specimen.getErrorDigits(1,0.4);        
        self.assertEqual(returnedDigits, expectedDigits);

if __name__ == '__main__':
    unittest.main()

    