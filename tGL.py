#!/usr/bin/env python3

import unittest
from GL import GL

class GLSystemLevel(unittest.TestCase):
    def setUp(self):        
        precision = 100;  # bits.
        specimen = GL(precision);
        self.specimen = specimen;
        return self

    def test_computesKnownError(self):
        # If I am not wrong, IEEE 754 gives 52 bits for fractions. This means detecting up to 
        # 1.11x10e-16. Using 4 iterations should give a smaller error than that.

        # Setup
        nIterations = 4; 
        expectedError = -21; # Number of correct digits.
                
        # Exec
        [dummy, returnedError] = self.specimen.computePi(nIterations);
        
        # Assertion
        self.assertEqual(returnedError, expectedError);        

    
    def test_fairlyGoodPiEstimation(self):
        # We compare our estimation against the one in math library. It should have the 52 bits 
        # mentioned in another tests.

        # Setup
        from math import pi
        nIterations = 4;
        expectedPi = pi;

        # Exec
        [returnedPi, returnedError] = self.specimen.computePi(nIterations);
        
        # Verification
        self.assertAlmostEqual(returnedPi, expectedPi,15)
        

class GLUnitLevel(unittest.TestCase):
    def test_GLObjectIsOfRightClass(self):
        specimen = GL(1);
        self.assertIsInstance(specimen, GL);

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
        self.assertTrue(0);

if __name__ == '__main__':
    unittest.main()

    