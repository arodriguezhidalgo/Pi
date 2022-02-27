#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from GL import GL, BB1
from math import pi
from PiComputation import PiComputation

class GLSystemLevel(unittest.TestCase):

    def setUp(self):        
        self.precision = 100; # bits.
        return self

    @parameterized.expand([
       ("GL", lambda x: GL(x), -21),
       ("BB1", lambda x: BB1(x), -21),       
    ])
    def test_computesKnownError(self, name, SUT, expectedError):
        # If I am not wrong, IEEE 754 gives 52 bits for fractions. This means detecting up to 
        # 1.11x10e-16. Using 4 iterations should give a smaller error than that.
        specimen = SUT(self.precision);

        # Setup
        nIterations = 2;         
                
        # Exec
        [dummy, returnedError] = specimen.computePi(nIterations);
        print(dummy)
        print(returnedError)
        # Assertion
        self.assertEqual(returnedError, expectedError);        

    @parameterized.expand([
       ("GL", lambda x: GL(x), pi),
       ("BB1", lambda x: BB1(x), pi),       
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
        
class GLUnitLevel(unittest.TestCase):
    @parameterized.expand([
       ("GL", lambda x: GL(x)),   
       ("BB1", lambda x: BB1(x)),    
    ])
    def test_GLObjectIsOfRightClass(self, name, SUT):
        specimen = SUT(1);
        self.assertIsInstance(specimen, PiComputation);

    def test_canSetPrecision(self):
        expectedPrecision = 1;
        specimen = GL(expectedPrecision);
        returnedPrecision = specimen.getPrecision();
        self.assertEqual(returnedPrecision, expectedPrecision);

    def test_gmpContextHasCustomPrecision(self):
        expectedPrecision = 1;
        specimen = GL(expectedPrecision);
        returnedContext = specimen.getContext();
        self.assertEqual(returnedContext.precision, expectedPrecision);

    def test_returnsCorrectNumberOfDigits(self):
        specimen = GL(5);
        expectedDigits = -1;

        returnedDigits= specimen.getErrorDigits(0.5,0.4);        
        self.assertEqual(returnedDigits, expectedDigits);

if __name__ == '__main__':
    unittest.main()

    