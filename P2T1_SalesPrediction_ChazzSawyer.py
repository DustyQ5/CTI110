# Enter in a projected sales dollar amount and it will give you the profit under
# the assumption that a 23% is the profit. - Tutorial assignment
# 9/22/2018
# CTI-110 P2T1 - Sales Prediction
# Chazz Sawyer
#

projected_sales_value = float(input('Enter the projected sales:'))
profit = projected_sales_value * 0.23

print ('The profit is $', format (profit, ',.2f'))
