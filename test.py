import unittest
from main import decoder

class Test01(unittest.TestCase):
    def test_decoder_1(self):
        '''
        Here we'll test the decoder function for a single element coded list
        '''
        data = ["A", 1, "B", 1]
        result = decoder(data)
        self.assertEqual(["A", "B"], result)

class Test02(unittest.TestCase):
    def test_decoder_2(self):
        '''
        Here we'll test the decoder function for a multiple element coded list
        '''
        data = ["A", 12, "B", 4, "A", 6, "B", 1]
        result = decoder(data)
        self.assertEqual(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B","B","A","A","A","A","A","A","B"], result)

class Test03(unittest.TestCase):
    def test_decoder_3(self):
        '''
        Here we'll test another case with multiple elements
        '''
        data = ["A", 15, "B", 5, "Z", 10, "F", 1]
        result = decoder(data)
        self.assertEqual(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "B", "Z", "Z", "Z", "Z", "Z", "Z", "Z", "Z", "Z", "Z", "F"], result)