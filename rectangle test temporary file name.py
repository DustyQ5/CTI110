# CTI-110 
# P3HW1 - Roman Numerals 
# Chazz Sawyer 
# 9/25/2018
#Program welcomes user
    #Progames ask for rectangle legnth and width. Then repeats.
        #programs states the area of both rectangles
            #programs announces which rectangle has a larger area or if
            #they are equal
print ('Welcome to rectangle creation and comparison area.')

rectangle_one_length = float(input('Please enter the first rectangles length:'))
rectangle_one_width = float(input('Please enter the first rectangles width:'))
rectangle_one_area = rectangle_one_length * rectangle_one_width

rectangle_two_length = float(input('Please enter the second rectangles length:'))
rectangle_two_width = float(input('Please enter the second rectangles width:'))
rectangle_two_area = rectangle_two_length * rectangle_two_width

print ('The first rectangle has an area of:', rectangle_one_area)
print ('The second rectangle has an area of:', rectangle_two_area)

if rectangle_one_area == rectangle_two_area:
    print ('Both rectangles have the same area!')
elif rectangle_one_area > rectangle_two_area:
    print ('The first rectangle has a larger area than the second.')
elif rectangle_one_area < rectangle_two_area:
        print ('The second rectangle has a larger area than the first.')
else:
    print ("I don't know how we got here but something went wrong.")
