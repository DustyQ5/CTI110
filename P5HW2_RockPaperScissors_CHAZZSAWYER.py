# Program to play rock paper scissors with yourself.
# 10/30/2018
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# CHAZZ SAWYER
#

#imports the best part
import random
#GLOBAL CONSTANTS
ROCK = 1
PAPER = 2
SCISSORS = 3
DISPLAY = 4
QUIT = 5
#global variables
player_total = 0
computer_total = 0
draw_total = 0

def main():
    #imports global variables
    global player_total
    global computer_total
    global draw_total
    #sets choice to an option that is not interacted with
    choice = 0
    display_menu()
    #loop that allows player to continue entering choices until they quit
    while choice != QUIT:
        #each loop the computers choice is made randomly
        computer_choice = random.randint(1,3)
        #each loop the player enters their choice
        choice = int(input('WHAT IS YOUR CHOICE?'))
        #if\elif for each rock/paper/scissors variation possible
        if choice == ROCK and computer_choice == ROCK:
            print('PLAYER CHOICE IS ROCK', '\t', 'COMPUTER CHOICE IS ROCK')
            print('\t','\t','DRAW')
            print('ROCK IS ROCK')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            draw_total = draw_total + 1
            
            #rock
        elif choice == ROCK and computer_choice == PAPER:
            print('PLAYER CHOICE IS ROCK', '\t', 'COMPUTER CHOICE IS PAPER')
            print('\t','\t','PLAYER LOSS')
            print('PAPER WRAPS ROCK')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            computer_total = computer_total + 1
            
            
        elif choice == ROCK and computer_choice == SCISSORS:
            print('PLAYER CHOICE IS ROCK', '\t', 'COMPUTER CHOICE IS SCISSORS')
            print('\t','\t','PLAYER WIN')
            print('ROCK SMASHES SCISSORS')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            player_total = player_total + 1
            
            #pAPER
        elif choice == PAPER and computer_choice == PAPER:
            print('PLAYER CHOICE IS PAPER', '\t', 'COMPUTER CHOICE IS PAPER')
            print('\t','\t','DRAW')
            print('PAPER IS PAPER')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            draw_total = draw_total + 1
            
        elif choice == PAPER and computer_choice == SCISSORS:
            print('PLAYER CHOICE IS PAPER', '\t', 'COMPUTER CHOICE IS SCISSORS')
            print('\t','\t','PLAYER LOSS')
            print('SCISSORS CUTS PAPER')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            computer_total = computer_total + 1
            
        elif choice == PAPER and computer_choice == ROCK:
            print('PLAYER CHOICE IS PAPER', '\t', 'COMPUTER CHOICE IS ROCK')
            print('\t','\t','PLAYER WIN')
            print('PAPER WRAPS ROCK')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            player_total = player_total + 1
            #scissors
        elif choice == SCISSORS and computer_choice == SCISSORS:
            print('PLAYER CHOICE IS SCISSORS', '\t', 'COMPUTER CHOICE IS SCISSORS')
            print('\t','\t','DRAW')
            print('SCISSORS IS SCISSORS')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            draw_total = draw_total + 1
            
        elif choice == SCISSORS and computer_choice == ROCK:
            print('PLAYER CHOICE IS SCISSORS', '\t', 'COMPUTER CHOICE IS ROCK')
            print('\t','\t','PLAYER LOSS')
            print('\t','\t','ROCK SMASHES SCISSORS')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            computer_total = computer_total + 1
            
        elif choice == SCISSORS and computer_choice == PAPER:
            print('PLAYER CHOICE IS SCISSORS', '\t', 'COMPUTER CHOICE IS PAPER')
            print('\t','\t','PLAYER WIN')
            print('SCISSORS CUTS PAPER')
            print("WOULD YOU LIKE TO PLAY AGAIN?")
            player_total = player_total + 1
        elif choice == QUIT:
            print('PLAYER TOTAL WIN:',player_total, 'TOTAL DRAWS:',draw_total,
                  'COMPUTER TOTAL WIN:',computer_total,)
        elif choice == DISPLAY:
            display_menu()
            
        


#line for copy and paste
#print('PLAYER CHOICE IS SCISSORS', '\t', 'COMPUTER CHOICE IS PAPER')









#MENU FUNCTION 
def display_menu():
    print('WELCOME TO ROCK, PAPER, SCISSORS!')
    print('WE ARE GOING TO PLAY THE GAME!')
    print("1) ROCK")
    print("2) PAPER")
    print("3) SCISSORS")
    print("4) DISPLAY MENU")
    print("5) QUIT")
    
    







main()
