#python 3.7.1

import random as rd

chars = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J" ,
 "K" , "L" , "M" , "N" , "O" , "P" , "Q" , "R" , "S" , "T" , "U" , "V" ,
  "W" , "X" , "Y" , "Z" , "a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" ,
   "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" ,
    "u" , "v" , "w" , "x" , "y" , "z" , "1" , "2" , "3" , "4" , "5" , "6" ,
     "7" , "8" , "9" , "0" , "@" , "$" , "&"]

i = 0
character = 0
generated = ""

charactersNumber = int(input("Enter length of the required password \n"))

while i < charactersNumber :
  character = chars[rd.randint(0 , len(chars)-1)]
  generated = generated + character
  i = i+1
  
print ("\n" + generated)

#print(rd.randint(0, len(chars)))

#Credits : Youssef Moataz
#Date : 2/7/2021