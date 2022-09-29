################################################################################
##
## CS 101 Lab
## Program 5
## Christian Morris
## cxmxp3@mail.umkc.edu
##
## Problem: Write a program for the Linda Hall library that correctly identifies if a student has an invalid or valid
##          library card number. If valid, then the program should output or produce the school and grade level for that
##          particular student's card number. The first 5 characters of the student's card must be letters A-Z. The next
##          character at index 5 must be a string value either 1,2, or 3 to represent the different schools: SCE, School of Law, or
##          College of arts and sciences. The character at index 6 must be either 1,2,3, or 4. These will represent the grade level of the student.
##          The next 2 characters after index 6 must be 0-9 and the last character at index 9,which is the check digit to verify the previous values, is
##          also 0-9.
##
## Algorithm:
##          1. Ask User to enter library card number
##          2. Define a function get_school that gets student's specific school to their library card
##          3. Define a function get_grade that gets student's specifc grade level(Freshman,Sophomore,Junior,Senior)
##          4. Define a function character_value to take a single character as a string parameter and return an interger representation of that value
##          5. Define a function get_check_digit to take the library card and return an integer with the value of check digit from a string parameter
##          6. Define a function verify_check_digit to verify if library_card is valid or invalid and retu
##          7. Repeat/loop unless User hits enter to exit program
##
##
################################################################################

def get_school(library_card):
    if library_card[5] == '1':
        return "School of Computing and Engineering SCE"
    elif library_card[5] == '2':
        return "School of Law"
    elif library_card[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"  
    
def get_grade(library_card):
    if library_card[6] == '1':
        return 'Freshman'
    elif library_card[6] == '2':
        return 'Sophomore'
    elif library_card[6] == '3':
        return 'Junior'
    elif library_card[6] == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'

def character_value (c):
    value = ord(c)
    if(value >= 48 and value <=57):
        return value - 48
    elif(value >= 65 and value <=90):
        return value - 65

def get_check_digit(library_card):
    sum = 0
    for i in range(len(library_card)):
        value = character_value(library_card[i])
        sum += value * (i+1)
    return sum % 10

def verify_check_digit(library_card):
    if len(library_card) != 10:
        return(False,'The length of the number given must be 10')
    for i in range(5):
        if library_card[i] < 'A' or library_card[i] > 'Z':
            msg = 'The first 5 characters must be A-Z, the invalid character is at ' + str(i) + " is " + library_card[i]
            return(False,msg)
        
    for i in range(7,10):
        if library_card[i] < '0' or library_card[i] > '9':
            msg = 'The last 3 characters must be 0-9, the invalid character is at index' \
                  + str(i) + 'is' + library_card[i]
            return(False,msg)    
    if(library_card[5] != '1' and library_card[5] != '2' and library_card[5] != '3'):
        return(False, 'The sixth character must be 1,2 or 3')
    
    if(library_card[6] != '1' and library_card[6] != '2' and library_card[6] != '3' and library_card[6] != '4'):
        return(False, 'The seventh character must be 1,2,3 or 4')
    calculated_value = get_check_digit(library_card)
    given_value = int(library_card[9])
    
    if given_value != calculated_value:
        msg = 'Check digit ' + str(given_value) + ' does not match calculated value ' + str(calculated_value)
        return(False,msg)
    return(True,'Library card is valid.')
   
def main():
        while(1):
            library_card = input('Enter Library Card. Hit Enter to Exit ==>')
            (is_valid,msg) = verify_check_digit(library_card)
            if is_valid == True:
                print(msg)
                print('The card belongs to a student in ' + get_school(library_card))
                print('The card belongs to a ' + get_grade(library_card))
            else:
                print('Library card is invalid.')
                print(msg)
                
if __name__== "__main__":
    main()














                
           
    






















                  
