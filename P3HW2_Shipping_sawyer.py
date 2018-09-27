# CTI-110 
# P3HW2 - Shipping Charges 
# Chazz Sawyer
# 9/27/2018
# Program asks for the weight of an object going to be shipped.
# Calculates rate per pound by the weight of object
# outputs the cost of the object based weight and rate per pound 
# $1.50 per pund if weight 2 or less
# 3.00 per pund if weight is over 2 and under or equal 6
# 4.00 per pound if weight is over 6 and under or equal 10
# 4.75 per pound if weight is over 10

weight = float(input('How much does the object weigh?'))
if weight <= 2 :
    weight_cost = weight * 1.50
    print ('The price to ship this object is: $', format(weight_cost,'.2f'))
elif weight > 2 and weight <= 6 :
    weight_cost = weight * 3.00
    print ('The price to ship this object is: $', format(weight_cost,'.2f'))
elif weight >6 and weight <= 10 :
    weight_cost = weight * 4.00
    print ('The price to ship this object is: $', format(weight_cost,'.2f'))
elif weight > 10 :
    weight_cost = weight * 4.75
    print ('The price to ship this object is: $', format(weight_cost,'.2f'))
