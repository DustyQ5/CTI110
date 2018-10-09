# Loop counter that then displays the total number
# Date
# CTI-110 P4T2 - Bug Collector
# Chazz Sawyer
#



total = 0.0
#Greets user and introduces the priogram concept
print ('I heard you like bugs! Lets count how many you can catch in five days!')

#loop asks user how many bugs caught that day
for day in range(0,5):
    print("It's day", day+1,'!')
    bugs_today = int(input('How many buds did you catch today?'))
    total += bugs_today

#If statement that displays bug total outcome
if total > 10:
    print("Wow!", total,"Bugs! That's some amzing bug catching skills")
else:
    print('Only', total,'bugs?')
