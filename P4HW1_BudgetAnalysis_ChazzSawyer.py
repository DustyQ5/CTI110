# Ask for user budget and exspense cost and outputs the end result
# 10/4/2018
# CTI-110 P4HW1 - Budget Analysis
# Chazz Sawyer
#

total_exspense = float(0.0)
#Ask for user starting budget and how many exspenses they have
budget = float(input('How much lucre do you possess for your budget?'))
budget_exspense = int(input('How many exspense payments do you have to make?'))

#Collects and adds exspenses togethor
for exspense in range (1, budget_exspense +1):
    exspense_cost = float(input('What is the cost of this exspense?'))
    total_exspense = total_exspense + exspense_cost

#Subtracts exspense total from budget and prints the result 
end_result = budget - total_exspense
print ('With a budget of,$',budget)
print ('A total exspense of,$',total_exspense)
print ('Your end lucre value will be $', format (end_result, ',.2f'))


