#!/usr/bin/env python3

import unittest
from GL import GL
class GLComputesPi(unittest.TestCase):
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

    