#Roman Gofman
#11/4/2019
#This is a program that takes in the starting age the amount saved and the ointerest rate to calculate the final
#amount of money by the time they retire at 70.

#This function gets the age amount saved each year and percentage of interset and calculates the final retirnement
#balance once the input age is 70. Age is changed yearly by one. The yearly amount saved is added every year to the
#total.And interest is changed into a decimal and then multiplied by the total every year before adding.
def calc_final_balance( age, amt_saved, interest ):
    interest = interest/100
    bal = 0
    while age < 70:# age loop
        age = age + 1
        bal = (bal + amt_saved) + ((bal + amt_saved)*interest)
    return(bal)#returns alue at 70

#Main function
def main():
    #print('$' + format(calc_final_balance( 70, 2000, 10 ), '.2f')) examples used in test cases
    #print('$' + format(calc_final_balance( 20, 0 , 10 ), '.2f'))
    print('$' + format(calc_final_balance( 15, 2000, 0 ), '.2f'))


#Runs the program
main()

# Documented Test Cases:

# Test 1

# Inputs:
# Age = 70
# Amount Saved Each Year = 2000
# Interest Percentage = 10

# Outputs:
# Ending Balance At 70 = $0

# Simple logic if you don't get a chance to put money in how do you get money.

# Test 2

# Inputs:
# Age = 20
# Amount Saved Each Year = 0
# Interest Percentage = 10

# Outputs:
# Ending Balance At 70 = $0

#Same type of logic no money in no money out.

#Test 3

# Inputs:
# Age = 15
# Amount Saved Each Year = 2000
# Interest Percentage = 0

# Outputs:
# Ending Balance At 70 = $110000.00

# Agrees with hand calculations.
