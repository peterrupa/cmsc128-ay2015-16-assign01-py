import unittest
import numLib

class NumLibTesting(unittest.TestCase):
    def test_numToWords(self):
        self.assertEqual(numLib.numToWords(1000001), 'one million one')
        self.assertEqual(numLib.numToWords(0), 'zero')
        self.assertEqual(numLib.numToWords(1), 'one')
        self.assertEqual(numLib.numToWords(11), 'eleven')
        self.assertEqual(numLib.numToWords(25), 'twenty five')
        self.assertEqual(numLib.numToWords(50), 'fifty')
        self.assertEqual(numLib.numToWords(75), 'seventy five')
        self.assertEqual(numLib.numToWords(100), 'one hundred')
        self.assertEqual(numLib.numToWords(1000001), 'one million one')
        self.assertEqual(numLib.numToWords(114), 'one hundred fourteen')
        self.assertEqual(numLib.numToWords(150), 'one hundred fifty')
        self.assertEqual(numLib.numToWords(164), 'one hundred sixty four')
        self.assertEqual(numLib.numToWords(1234), 'one thousand two hundred thirty four')
        self.assertEqual(numLib.numToWords(10000), 'ten thousand')
        self.assertEqual(numLib.numToWords(10050), 'ten thousand fifty')
        self.assertEqual(numLib.numToWords(250000), 'two hundred fifty thousand')
        self.assertEqual(numLib.numToWords(500000), 'five hundred thousand')
        self.assertEqual(numLib.numToWords(256186), 'two hundred fifty six thousand one hundred eighty six')
        self.assertEqual(numLib.numToWords(46250), 'fourty six thousand two hundred fifty')
            
    def test_wordsToNum(self):
        self.assertEqual(numLib.wordsToNum('one million one'), 1000001)
        self.assertEqual(numLib.wordsToNum('zero'), 0)
        self.assertEqual(numLib.wordsToNum('one'), 1)
        self.assertEqual(numLib.wordsToNum('eleven'), 11)
        self.assertEqual(numLib.wordsToNum('twenty five' ), 25)
        self.assertEqual(numLib.wordsToNum('fifty'), 50)
        self.assertEqual(numLib.wordsToNum('seventy five'), 75)
        self.assertEqual(numLib.wordsToNum('one hundred'), 100)
        self.assertEqual(numLib.wordsToNum('one hundred fourteen'), 114)
        self.assertEqual(numLib.wordsToNum('one hundred fifty'), 150)
        self.assertEqual(numLib.wordsToNum('one hundred sixty four'), 164)
        self.assertEqual(numLib.wordsToNum('one thousand two hundred thirty four'), 1234)
        self.assertEqual(numLib.wordsToNum('ten thousand'), 10000)
        self.assertEqual(numLib.wordsToNum('ten thousand fifty'), 10050)
        self.assertEqual(numLib.wordsToNum('two hundred fifty thousand'), 250000)
        self.assertEqual(numLib.wordsToNum('five hundred thousand'), 500000)
        self.assertEqual(numLib.wordsToNum('two hundred fifty six thousand one hundred eighty six'), 256186)
        self.assertEqual(numLib.wordsToNum('fourty six thousand two hundred fifty'), 46250)
        
    def test_wordsToCurrency(self):
        self.assertEqual(numLib.wordsToCurrency('one million one', 'USD'), 'USD1000001')
        self.assertEqual(numLib.wordsToCurrency('zero', 'USD'), 'USD0')
        self.assertEqual(numLib.wordsToCurrency('one', 'JPY'), 'JPY1')
        self.assertEqual(numLib.wordsToCurrency('eleven', 'PHP'), 'PHP11')
        self.assertEqual(numLib.wordsToCurrency('twenty five' , 'PHP'), 'PHP25')
        self.assertEqual(numLib.wordsToCurrency('fifty', 'USD'), 'USD50')
        self.assertEqual(numLib.wordsToCurrency('seventy five', 'JPY'), 'JPY75')
        self.assertEqual(numLib.wordsToCurrency('one hundred', 'JPY'), 'JPY100')
        self.assertEqual(numLib.wordsToCurrency('one hundred fourteen', 'PHP'), 'PHP114')
        self.assertEqual(numLib.wordsToCurrency('one hundred fifty', 'USD'), 'USD150')
        self.assertEqual(numLib.wordsToCurrency('one hundred sixty four', 'USD'), 'USD164')
        self.assertEqual(numLib.wordsToCurrency('one thousand two hundred thirty four', 'JPY'), 'JPY1234')
        self.assertEqual(numLib.wordsToCurrency('ten thousand', 'PHP'), 'PHP10000')
        self.assertEqual(numLib.wordsToCurrency('ten thousand fifty', 'JPY'), 'JPY10050')
        self.assertEqual(numLib.wordsToCurrency('two hundred fifty thousand', 'USD'), 'USD250000')
        self.assertEqual(numLib.wordsToCurrency('five hundred thousand', 'USD'), 'USD500000')
        self.assertEqual(numLib.wordsToCurrency('two hundred fifty six thousand one hundred eighty six', 'PHP'), 'PHP256186')
        self.assertEqual(numLib.wordsToCurrency('fourty six thousand two hundred fifty', 'JPY'), 'JPY46250')
        
    def test_numberDelimited(self):
        self.assertEqual(numLib.numberDelimited(1000021, ',', 3), '1,000,021')
        self.assertEqual(numLib.numberDelimited(100, '!', 2), '1!00')
        self.assertEqual(numLib.numberDelimited(114, '+', 1), '1+1+4')
        self.assertEqual(numLib.numberDelimited(),150, ',', 3,  '150')
        self.assertEqual(numLib.numberDelimited(164, ',', 2), '1,64')
        self.assertEqual(numLib.numberDelimited(1234, ',', 3), '1,234')
        self.assertEqual(numLib.numberDelimited(10000, '-', 4), '1-0000')
        self.assertEqual(numLib.numberDelimited(10050, '|', 1), '1|0|0|5|0')
        self.assertEqual(numLib.numberDelimited(),250000, ',', 3,  '250,000')
        self.assertEqual(numLib.numberDelimited(500000, '~', 5), '5~00000')
        self.assertEqual(numLib.numberDelimited(),256186, ',', 3,  '256,186')
        self.assertEqual(numLib.numberDelimited(46250, '/', 4), '4/6250')
                  
if __name__ == '__main__':
    unittest.main()