#!/usr/bin/env python3

import unittest
from GL import GL

class GLSystemLevel(unittest.TestCase):
    def test_computesKnownError(self):
        # If I am not wrong, IEEE 754 gives 52 bits for fractions. This means detecting upt to 
        # 1.11x10e-16. Using 4 iterations should give a smaller error than that.
        # Setup
        nIterations = 4; 
        precision = 100;  # bits.
        expectedError = 3.72*1e-21;
        specimen = GL(precision);
        
        # Exec
        [dummy, returnedError] = specimen.computePi(nIterations);
        
        # Assertion
        self.assertAlmostEqual(returnedError, expectedError, 23);        

    def test_returnsNumberOfCorrectDigits(self):
        self.assertTrue(1);
    
    def test_fairlyGoodPiEstimation(self):
        self.assertTrue(1);

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

if __name__ == '__main__':
    unittest.main()

    