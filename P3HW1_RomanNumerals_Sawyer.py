# CTI-110 
# P3HW1 - Roman Numerals 
# Chazz Sawyer 
# 9/25/2018
# Program asks for a number 1 through 10
    #Program runs through numbers one through ten checking to see if any are equal to input number
        #If the program finds a number 1 through ten it outputs it's equivilent roman numeral
            #I a number one through 10 is not input then the program will display an unacceptable
            #response message.
    
roman_numeral_conversian_number = int(input(
    'Pleae enter a number between 1 and 10 for roman numeral conversion:'))

if roman_numeral_conversian_number == 1:
    print ('I')
elif roman_numeral_conversian_number == 2:
     print ('II')
elif roman_numeral_conversian_number == 3:
     print ('III')
elif roman_numeral_conversian_number == 4:
     print ('IV')
elif roman_numeral_conversian_number == 5:
     print ('V')
elif roman_numeral_conversian_number == 6:
     print ('VI')
elif roman_numeral_conversian_number == 7:
     print ('VII')
elif roman_numeral_conversian_number == 8:
     print ('VIII')
elif roman_numeral_conversian_number == 9:
     print ('IX')
elif roman_numeral_conversian_number == 10:
     print ('X')
else:
     print ('That is not an acceptable response.')
