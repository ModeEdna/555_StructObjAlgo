# import random module
import random

# define the function for the game
def game(n, switchOrKeep):
    # initiate count variable to know how many times the player wins
    count = 0
    # create a loop that runs n times
    for i in range(n):
        # select a random integer with a 1/3 chance of getting a 1, which represents selecting the car on first guess
        select = random.randint(1, 3)
        # set win variable to True or False depending on player initially selecting the correct door
        win = (select == 1)
        # if statement to add 1 to count based on initial choices
        if (switchOrKeep and not win) or (not switchOrKeep and win):
            # adding 1 to count
            count += 1
    # return percentage of times the player won the car
    return (count/n)*100

# run the game 10000 times and choose to switch
print(game(10000, True))

# the final result is the percentage of times you'd win the game, depending on your choice to switch or not switch doors