print('Welcome to Flarsheim Guesser!')
user_choice = 'y'

while(user_choice == 'Y' or user_choice == 'y'):
    print('\nPlease think of a number between and including 1 and 100.')

    Remain_three = 0
    Remain_five = 0
    Remain_seven = 0

    Remain_three = int(input('\nWhat is the remainder when your number is divided by 3 ?'))
    while(Remain_three < 0 or Remain_three >= 3):
        if Remain_three < 0:
            print('The value entered must be 0 or greater')
        elif Remain_three >= 3:
            print('The value entered must be less than 3')

        Remain_three = int(input('What is the remainder when your number is divided by 3 ?'))
        
    Remain_five = int(input('\nWhat is the remainder when your number is divided by 5 ?'))
    while(Remain_five < 0 or Remain_five >= 5):
        if Remain_five < 0:
            print('The value entered must be 0 or greater')
        elif Remain_five >= 5:
            print('The value entered must be less than 5')

        Remain_five = int(input('What is the remainder when your number is divided by 5?'))
        
    Remain_seven = int(input('\nWhat is the remainder when your number is divided by 7 ?'))
    while(Remain_seven <0 or Remain_seven >= 7):
        if Remain_seven < 0:
            print('The value entered must be 0 or greater')
        elif Remain_seven >=7:
            print('The value entered must be less than 7')

        Remain_seven = int(input('What is the remainder when your number is divided by 7 ?'))

    for i in range(1,101):
        if(i%3 == Remain_three and i%5 == Remain_five and i%7 == Remain_seven):
             print('Your number was', i)
             print('How amazing is that?\n')
                
    user_choice = input('Do you want to play again? Y to continue, N to quit -->')
    while(user_choice != 'Y' and user_choice != 'N' and user_choice != 'y' and user_choice != 'n'):
        user_choice = input('Do you want to play again? Y to continue, N to quit -->')
            
            
