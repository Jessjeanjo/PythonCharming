#!C:/Python27/python.exe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Programmer: JESSICA JOSEPH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Sums the values that are multiples
of 3 from 0 to 10,00 inclusively
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from __future__ import print_function

def main():
  total = 0; upperBound = 10000;
  for i in range(upperBound +1):
    if i%3 == 0:
    	total += i    # "total += i" is shorthand for "total = total + i"
  
  print("Sum of the numbers that are multiples of 3 from [0,%i): %i" %(upperBound, total))
  
if __name__ == '__main__':
  main()
