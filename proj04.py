#############################################################################################
#       CSE231 Project #4
#       In This project I will be creating a program to play a name of craps
#       1) Prompt the main function which contains everything
#       2) Use the get_bank_balance function to ask for an initial balance
#       3) Use then use the get_wager_amount function to get a wager amount.
#       3) Check that wager amount is less than balance is_valid_wager_amount.
#       4) Roll_die to return the 2 dice values.
#       5) Add the two dice sum to get a total sum using first_roll_result.
#       6) Check if it is a winner or a loser
#       7) If not winner or loser then return points
#       8) Keep promting new dice rolls to get winner loser or same points
#       9) add or subtract wager from balance
#       10) Ask if they want to play again
#############################################################################################

# Test 1 
VALUES = [3,4,1,2,5,6,2,3,2,2,3,3,1,4,2,4,2,3,4,5,3,4]

# rand is a generator function
# each time you call it you get the next value in the list of numbers
rand = (i for i in VALUES)

# rand is called using the next() function
# we wrap it in our randint() function so we can use it in our program
def randint(a,b):
    '''return the next value in the rand generator.
       for testing the parameters a and b are ignored.'''
    return next(rand)

def display_game_rules():
    print('''A player rolls two dice. Each die has six faces. 
          These faces contain 1, 2, 3, 4, 5, and 6 spots. 
          After the dice have come to rest, 
          the sum of the spots on the two upward faces is calculated. 
          If the sum is 7 or 11 on the first throw, the player wins. 
          If the sum is 2, 3, or 12 on the first throw (called "craps"), 
          the player loses (i.e. the "house" wins). 
          If the sum is 4, 5, 6, 8, 9, or 10 on the first throw, 
          then the sum becomes the player's "point." 
          To win, you must continue rolling the dice until you "make your point." 
          The player loses by rolling a 7 before making the point.''')

def get_bank_balance():
    '''Returns a statement with the inputed bank balance'''
    balance = input("Enter an initial bank balance (dollars):")
    balance_int = int(balance)
    return balance_int

def add_to_bank_balance(balance_int):
    '''Asks player how much they want to add to the balance
    balance: an integer to store into the bank balance'''
    add_question = input("Do you want to add to your balance?")
    if add_question == 'yes':
        add_to_bank = input("Enter how many dollars to add to your balance:")
        add_to_bank_int = int(add_to_bank)
        balance_int += add_to_bank_int
        balance = str(balance_int)
        print("Balance: "+balance)
        balance_int = int(balance)
        return balance_int

def get_wager_amount():
    '''Asks the player for a wager amount'''
    wager = input("Enter a wager amount (dollars):")
    wager_int = int(wager)
    return wager_int

def is_valid_wager_amount(wager_int, balance_int):
    '''Check that wager is less than balance
    wager: an amount determined from the get_wager_amount
    blance: an amount determined from the get_bank_balance'''
    if wager_int > balance_int:
        print("Error: wager > balance. Try again.")
        return False
    if wager_int <= balance_int:
        return True
    
    
def roll_die():
    '''Roll one dice using the function randint(1,6)'''
    return randint(1,6)


def calculate_sum_dice(die1_value, die2_value):
    '''Will add sum of the two die values
    die1_value: from roll_die first value
    die2_value: from roll_die second value'''
    return die1_value + die2_value

def first_roll_result(sum_dice):
    '''This function will return the sum of the dice and print if winner or loser or point returned
    sum_dice: is from the calculate_sum_dice function and will be used to calculate winner or loser'''
    if sum_dice == 7 or sum_dice == 11:
        print("Natural winner.")
        print("You WIN!")
        return 7
    if sum_dice == 2 or sum_dice == 3 or sum_dice == 12:
        print("Craps.")
        print("You lose.")
        return 2
    else:
        point = sum_dice
        point_str = str(point)
        print("*** Point: "+point_str)
        return point
    
def subsequent_roll_result(sum_dice_2, point_value):
    '''Function will be used if not winner or loser first dice throw. Will keep promting until this value equals points
    sum_dice: will be used to calculate weather winner or loser
    point_value: from the function first_roll_result to see if winner if equal'''
    die3_value = roll_die()
    die4_value = roll_die()
    die3 = str(die3_value)
    die4 = str(die4_value)
    print("Die 1: "+die3)
    print("Die 2: "+die4)
    sum_dice_2 = die3_value + die4_value
    sum_dice_2_str = str(sum_dice_2)
    print("Dice Sum: "+sum_dice_2_str)
    if sum_dice_2 == point_value:
        print("You matched your point.")
        print("You WIN!")
        return 7
    if sum_dice_2 == 7 or sum_dice_2 == 11 or sum_dice_2 == 2 or sum_dice_2 == 3 or sum_dice_2 == 12:
        print("You lose.")
        return 2
    

def main():
    #set an initial condition to that the game, this can be changed later w an input
    want_continue = 'yes'
    #display the game rules
    display_game_rules()
    #ask for an inital balance
    balance_int = get_bank_balance()
    #while loop to keep playing the game
    while want_continue != 'no':
        #ask for a wager
        wager_int = get_wager_amount()
        #check that the wager is valid
        valid_wager = is_valid_wager_amount(wager_int, balance_int)
        #if the wager doesn't equal true, keep asking for it.
        while valid_wager != True:
            wager_int = get_wager_amount()
            valid_wager = is_valid_wager_amount(wager_int, balance_int)
        #get die value 1 and 2
        die1_value = roll_die()
        die2_value = roll_die()
        #convert them to string for print
        die1_value_str = str(die1_value)
        die2_value_str = str(die2_value)
        #print the dice values
        print("Die 1: "+die1_value_str)
        print("Die 2: "+die2_value_str)
        #calculate the sum of the dice
        sum_dice = calculate_sum_dice(die1_value, die2_value)
        #make sum_dice a string
        sum_dice_str = str(sum_dice)
        #print the value of sum_dice
        print("Dice sum: "+sum_dice_str)
        #make point equal to the first_roll_result
        point = first_roll_result(sum_dice)
        #set a value for a later while loop
        the_value = 0
        #if the point is winner then add wager from balance
        if point == 7:
            balance_int += wager_int
            balance_str = ''
            balance_str = str(balance_int)
            print("Balance: "+balance_str)
            the_value = 7
        #if the point is loser then subtract wager from balance
        if point == 2:
            balance_int -= wager_int
            balance_str = ''
            balance_str = str(balance_int)
            print("Balance: "+balance_str)
            the_value = 2
        while the_value != 7 and the_value != 2:
            point_value = point
            the_value = subsequent_roll_result(sum_dice,point_value)
            if the_value == 7:
                balance_int += wager_int
                balance_str = ''
                balance_str = str(balance_int)
                print("Balance: "+balance_str)
            if the_value == 2:
                balance_int -= wager_int
                balance_str = ''
                balance_str = str(balance_int)
                print("Balance: "+balance_str)
        want_continue = input("Do you want to continue?")
        if want_continue == 'yes':
            balance_int = add_to_bank_balance(balance_int)
    

if __name__ == "__main__":
    main()