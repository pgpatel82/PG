import unittest
from Chal4fibonacci import *
from Chal4convertNumToString import *

class challenge4(unittest.TestCase):

   def test_challenge4(self):
     ### Fibonacci number output
     print(str(fibonacci(3)) + ": " + convertNumToString(fibonacci(3)))
     print(str(fibonacci(7)) + ": " + convertNumToString(fibonacci(7)))
     print(str(fibonacci(12)) + ": " + convertNumToString(fibonacci(12)))
     print(str(fibonacci(15)) + ": " + convertNumToString(fibonacci(15)))
     print(str(fibonacci(18)) + ": " + convertNumToString(fibonacci(18)))
     print(str(fibonacci(20)) + ": " + convertNumToString(fibonacci(20)))
     print(str(fibonacci(21)) + ": " + convertNumToString(fibonacci(21)))
     print(str(fibonacci(22)) + ": " + convertNumToString(fibonacci(22)))
     print(str(fibonacci(23)) + ": " + convertNumToString(fibonacci(23)))
     print(str(fibonacci(24)) + ": " + convertNumToString(fibonacci(24)))
     print(str(fibonacci(25)) + ": " + convertNumToString(fibonacci(25)))
     print(str(fibonacci(28)) + ": " + convertNumToString(fibonacci(28)))
     print(str(fibonacci(30)) + ": " + convertNumToString(fibonacci(30)))
     print(str(fibonacci(32)) + ": " + convertNumToString(fibonacci(32)))  #more than 1 million, return invalid number
     ### Number to word conversion checking
     print("0 --> " + convertNumToString(0))
     print("8 --> " + convertNumToString(8))
     print("19 --> " + convertNumToString(19))
     print("20 --> " + convertNumToString(20))
     print("99 --> " + convertNumToString(99))
     print("100 --> " + convertNumToString(100))
     print("550 --> " + convertNumToString(550))
     print("200 --> " + convertNumToString(200))
     print("999 --> " + convertNumToString(999))
     print("220 --> " + convertNumToString(220))
     print("110000 --> " + convertNumToString(110000))
     print("431999 --> " + convertNumToString(431999))
     print("2200 --> " + convertNumToString(2200))
     print("1000 --> " + convertNumToString(1000))
     print("1001 --> " + convertNumToString(1001))
     print("1021 --> " + convertNumToString(1021))
     print("1019 --> " + convertNumToString(1019))
     print("2202 --> " + convertNumToString(2202))
     print("999999 --> " + convertNumToString(999999))
     print("100000 --> " + convertNumToString(100000))
     print("20999 --> " + convertNumToString(20999))
     print("19999 --> " + convertNumToString(19999))
     print("21999 --> " + convertNumToString(21999))
     print("1000000 --> " + convertNumToString(1000000))
     print("99999 --> " + convertNumToString(99999))
     print("1000001 --> " + convertNumToString(1000001))   #more than 1 million, return invalid number

if __name__ == '__main__':
    unittest.main()