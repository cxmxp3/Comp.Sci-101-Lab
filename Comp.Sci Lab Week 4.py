####################################################################
##
##CS 101 Lab
##Program #3
##Name: Christian Morris
##Email: cxmxp3@mail.umkc.edu
##
##Problem: Need a set of functions that will allow the user to gamble with a set amount of money and see if they win or lose.
##
##Algorithm:1.Import random module
##          2.Create a function that will ask if the user wants to play again                    
##          3.If the user enters Yes or yes, the code will play again. If they enter No or n, program ends. Anything besides Yes/y or No/n then reask the question
##          4.Create a function that will ask for the amount user wants to wager or bet
##          5.Create a function that will generate 3 random numbers between 1 and 10
##          6.Create a function that will see how many matches are in 3 different numbers
##          7.Create a function that will ask the user how many chips they want to begin or start with. Loop or repeat if user input is outside the range of 1-100
##
##Error Handling:
##              Any special error handling to be noted. Wager not less than 0. etc
##Other comments:
##              Any special comments
##
##
####################################################################
import random

def play_again():#Asks the user if they want to play again and returns False if N or NO, and True if Y or YES. Asks repeatedly until user responds yes
    play = 'a'
    while play != 'NO' or play !='N' or play != 'YES' or play != 'Y':#repeats if user input is outside of code
        play = input('Do you want to play again:\n')#Asks for user's input
        play = play.upper()#Puts the string entered in upper case
        if play == 'YES' or play == 'Y':#reads the input to see if user wants to play again
            return True
        elif play == 'NO' or play == 'N':
            return False
        else:
            print('You must enter Y/YES/N/NO. Please try again.')
            continue#restarts loop
        
def get_wager(bank: int):#Asks user for input for wager amount
    amount = int(input('Enter the amount you want to wager:\n'))
    while amount <= 0 or amount > bank:
        if amount <= 0:
            print('The wager cant be less than or equal to 0. Please try again.')
        if amount > bank:
            print('The wager cant be greater than the amount in the bank. Please try again.')
        amount = int(input('Enter the amount you want to wager:\n'))
    return amount

def get_slot_results():#Returns the result of the slot
    a = random.randint(1,10)#pulls random number between 1-10 (same for b and c).
    b = random.randint(1,10)
    c = random.randint(1,10)
    return a,b,c

def get_matches(reela,reelb,reelc):#Returns 3 for all 3 match, 2 for 2 alike, and 0 for none that are alike.
    if reela == reelb and reela == reelc:
        return 3
    if reela == reelb and reela != reelc:
        return 2
    if reela != reelb and reela ==reelc:
        return 2
    if reelb == reelc and reela != reelc:
        return 2
    if reela != reelb and reela != reelc:
        return 0

def get_bank():#Returns how many chips the user wants to bet or play with. Continously loops until program recieves a value greater than 0 and less than 101.
    amount = 0#starts loop
    while amount <=0 or amount > 100:
        amount = int(input('How many chips do you want to play with?\n'))
        if amount <= 0:
            print('Amount too low, the number needs to be between 1-100. Try again.')
            continue
        elif amount > 100:
            print('Amount too high, the number needs to be between 1-100. Try again.')
            continue
    return amount

def get_payout(wager,matches):#Returns how much the payout is 
    if matches == 0:
        payout = wager * -1
    elif matches == 2:
        payout = wager *3 - wager
    elif matches == 3:
        payout = wager * 10 - wager
    return payout

if __name__== "__main__":
    playing = True
    while playing:
        bank = get_bank()
        while bank > 0:
            wager = get_wager(bank)
            reel1,reel2,reel3 = get_slot_results()
            matches = get_matches(reel1,reel2,reel3)
            payout = get_payout(wager,matches)
            bank = bank + payout

            print('Your spin',reel1, reel2,reel3)
            print('You matched',matches, 'reels')
            print('You won/lost',payout)
            print('Current bank',bank)
            print()
        print('You lost all', 0, 'in',0,'spins')
        print('The most chips you had was',0)
        playing = play_again()



