# Yearly three percent tuition increase program
# 10/4/2018
# CTI-110 P4HW3 - Tuition Increase
# Chazz Sawyer
#


#Tuition initial value
tuition = 8000

print ('Tuition is currently $8000.')
print ('It will increase by three percent ech year for the next five years.')
#Loop tracks tuition and adds three percent each loop
for year in range(0,5):
    tuition = tuition + (tuition *3/100)
    print ('Tuition after year',year+1, 'will be', format(tuition,',.2f'))










