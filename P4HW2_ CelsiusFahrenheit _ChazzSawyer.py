# Prints a table showing fahrenheit values converted to celcious 
# 10/4/
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Chazz Sawyer
#

#Table titles
print ('Fahrenheit\tCelsious')
print ('_________________________')
#Loop that starts at fagrenheit value 32, celsious equivalent of 0
#Loops until the set range of 68 when celsious equals 20
for fahrenheit in range(31, 68):
    print (fahrenheit + 1,'\t\t',(fahrenheit + 1 - 32)*5/9 )


