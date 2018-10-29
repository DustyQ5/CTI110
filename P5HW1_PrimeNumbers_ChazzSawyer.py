# input a number and the program will tell you if it is prime or not prime
# 10/29/2018
# CTI-110 P5HW1 - Prime Numbers
# Chazz Sawyer
#


#mainf function
def main():
    #intoduction sentence
    print('Hello, welcome to prime number checker.')
    #prime number to check for input
    number_search_prime = int(input('What number would you like to check to see if it is a prime number?'))
    print('This program will now check to see if',number_search_prime,'is a prime number')
    #activates prime number checker 
    isprime(number_search_prime)





#function checks to see if number is prime
def isprime(number):
    #if number is one or less it is not a rime number
    if number <= 1:
        print(number,'Is not a prime number')

    else:
        #range 2-input number
        for fwop in range (1+1,number):
            #fwop represents each loop number- number is divided by fwop each loop - if = 0 then not prime
            if (number % fwop) == 0:
                print(number,'not prime.')
                #this breaks the program if it is not a prime number because it would repeat print the not prime statement
                #everytime the number was detected to not be a prime number and then it would print the else statement as well
                break

        else:
            print(number, 'is Prime.')
            #is prime print





    
main()
