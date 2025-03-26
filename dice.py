import random

numbers=[]

def roll_dice(dice_roll_number):
    Num_fives=0

    for dice_roll_number in range(0,dice_roll_number):
        dice_value=random.randint(1,6)
        if dice_value==5:
            Num_fives+=1
    remaining_dice=dice_roll_number-Num_fives
    print(f"Number of dice remaining is:{remaining_dice}\n")

    # this negates the possibility of negative numbers
    if remaining_dice<=0:
        return 0
    else:
        numbers.append(remaining_dice)

        # this is the recursive part of the function
        if Num_fives==0 or remaining_dice<=0:
            return 0
        else:
            return roll_dice(remaining_dice)

def print_results():
    global numbers
    higher_end=int(input("Enter the higher end of the range: "))
    for i in range(0,higher_end):
        
        dice_roll_number=100

        roll_dice(dice_roll_number)
        with open("Exponential decay points.txt", "+a") as file:
            file.write(str(numbers)+ "\n")
        numbers=[]    
    
print_results()