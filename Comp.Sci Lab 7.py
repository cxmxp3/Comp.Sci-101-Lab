########################################################################
# Comp.Sci 101 Lab
# Program 7
# Name: Christian Morris
# Email: cxmxp3@mail.umkc.edu
#
# PROBLEM: Find cars in a file that are above a certain mpg.
#
#
# ALGORITHM: 
#           1) Create a min_mpg function.
#           2) Create a function that asks the user to enter vehicle file.
#           3) Create a function that asks the user for the file they want to output. If IOERROR then repeat function
#           4) Create a function that takes the file from 2) and read each line of file as a list
#           5) Create a function that outputs the file.
#           6) For main code run function 1, 2, 3, 4, and 5.
#
#
# ERROR HANDLING:
#           Any special error handling to be note. Wager not less than 0.etc
#
#OTHER COMMENTS:
#           Any special comments
#
#
#
#
#########################################################################



def min_mpg(): #Gets the minimum fuel economy from user and checks for errors
    a = True
    while a == True: #loop to run entire program as long as mpg is not returned
        try:
            while a == True: #loop to run as long as no error but value is out of bounds
                mpg = float(input('Enter the minimum mpg: '))
                if mpg <= 0:
                    print('Fuel economy given must be greater than 0\n')
                elif mpg > 100:
                    print('Fuel economy must be less than 100\n')
                else:
                    a = False #ends the loop
                    return mpg #returns mpg
        except ValueError:
            print('You must enter a number for the fuel economy')
            
def get_file(): #Opens the file the user enters and will continue to ask until valid file is inputed
    a = True
    while a == True:#loop to run code if no errors are present
        try:
            file = input('Enter the name of the input vehicle file: ')
            myfile = open(file)
            a = False
            return myfile #returns file
        except FileNotFoundError:
            print('Could not open file {}'.format(file))

def get_outputfile(): #Creates the output file and will repeat until valid file is inputed
    a = True 
    while a == True: #loop to run code
        try:
            file = input('Enter the name of the file to output to: ')
            myfile = open(file, 'a')
            a = False #ends loop after iteration
            return myfile #returns file
        except IOError:
            print('There is an IO Error{}'.format(file))

def file_split_list(myfile): #Creates a nested list of the lines of the file entered. /t is the separtor
    file1 = myfile.readlines()
    file2 = []
    for i in range(len(file1)):
        file2.append(file1[i].split('\t'))
    return file2

def file_output(lst, mpg, outfile): #Outputs the file
    for i in range(1, len(lst)):
        try:
            combinded = float(lst[i][7])
            if combinded >= mpg:
                outfile.write('{:<5}{:<20}{:<40}{:>10.3f}\n'.format(lst[i][0], lst[i][1],lst[i][2],combinded))
        except ValueError:
            print('Could not convert value {} for vehicle {} {} {}'.format(lst[i][7], lst[i][0], lst[i][1],lst[i][2]))

if __name__ == "__main__":
    mpg = min_mpg()
    infile = get_file()
    lst = file_split_list(infile)
    outfile = get_outputfile()
    file_output(lst, mpg, outfile)
    infile.close()
    outfile.close()
        

















        
