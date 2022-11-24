"""
----------------------------------------------------------
  Python - Try to solve

  Sum of v0w3ls

  Made by Mustofa Kodirov
----------------------------------------------------------
 Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers.
   Vowel	Number
     A	      4
     E	      3
     I	      1
     O	      0
     U	      0
 sum_of_vowels("Let\'s test this function.") ➞ 8

 sum_of_vowels("Do I get the correct output?") ➞ 10

 sum_of_vowels("I love edabit!") ➞ 12
"""
# sum_of_vowels
str = "Let\'s test this function."

vowels = { 
    "A": 4, 
    "E": 3, 
    "I": 1, 
    "O": 0, 
    "U": 0 
}

sum = 0;
for x in str:
    if vowels.get(x.upper()):
        sum = sum + vowels.get(x.upper())
return sum