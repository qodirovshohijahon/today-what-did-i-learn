"""
----------------------------------------------------------
  Python - Try to solve

  Last Digit Ultimate

  Made by Mustofa Kodirov
  
  Date: 24.11.2022
----------------------------------------------------------
 Your job is to create a function, that takes 3 numbers: a, b, c and returns True if the last digit of a * b = the last digit of c. Check the examples below for an explanation.
  Examples
  last_dig(25, 21, 125) ➞ True
  # The last digit of 25 is 5, the last digit of 21 is 1, and the last
  # digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
  # to the last digit of 125(5).

  last_dig(55, 226, 5190) ➞ True
  # The last digit of 55 is 5, the last digit of 226 is 6, and the last
  # digit of 5190 is 0, and the last digit of 5*6 = 30 is 0, which is
  # equal to the last digit of 5190(0).

  last_dig(12, 215, 2142) ➞ False
  # The last digit of 12 is 2, the last digit of 215 is 5, and the last
  # digit of 2142 is 2, and the last digit of 2*5 = 10 is 0, which is
  # not equal to the last digit of 2142(2)
"""

# return the last digit
def last_digit(num):
  num = abs(num)
  while num >=0:
    remainder = num % 10
    return remainder

def last_dig(a, b, c):
  if last_digit(a) * last_digit(b):
    if (last_digit(last_digit(a) * last_digit(b))) == last_digit(c):
      return True
    else:
	    return False

print(last_dig(-25, 21, 125))
print(last_dig(55, 226, 5190))
print(last_dig(12, 215, 2142))


# [Last Digit Ultimate](https://edabit.com/challenge/7PtLRCT5aL9uiqxPs)