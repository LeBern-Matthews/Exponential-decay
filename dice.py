import random

def roll_dice(dice_roll_number, numbers:list):
    num_fives = 0

    for _ in range(0, dice_roll_number):
        dice_value = random.randint(1, 6)
        if dice_value == 5:
            num_fives += 1

    remaining_dice = dice_roll_number - num_fives
    print(f"Number of dice remaining is: {remaining_dice}\n")

    # Base case to terminate recursion
    if remaining_dice <= 0:
        return 0
    else:
        numbers.append(remaining_dice)
        return roll_dice(remaining_dice, numbers)

def print_results():
    higher_end = int(input("Enter the higher end of the range: "))
    for _ in range(0, higher_end):
        dice_roll_number = 100
        numbers = []  # Use a local variable instead of global

        roll_dice(dice_roll_number, numbers)
        number_of_points = len(numbers)
        with open("Exponential decay points.txt", "a") as file:
            file.write(f"{number_of_points}: {numbers}\n")

print_results()