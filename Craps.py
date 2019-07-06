# Craps program
# Seth Fort

from random import randint

# import Random Number Generator

chip_start = int(100)

# Starting number of chips for the player

def main():
    s = ''
    while not s or s[0] in 'Yy':
        play_the_game()
        s = input('Play again? (Y or N): ')

# If player has lost or won, ask if they would like to rerun the program

def play_the_game():
    chip_count = chip_start
    r = roll();
    if r == 7 or r == 11:
        chip_count += 5
        print(r, 'is an instant WINNER!\n')
        print('You now have $', chip_count)
        return
    if r == 2 or r == 3 or r == 12:
        chip_count -= 5
        print(r, 'is an instant LOSER. Sorry!\n')
        print('You now have $', chip_count)
        return
# Natural 7 or 11s win and add $5
# Natural 2s 3s and 12s Lose and take $5
# anything else starts your point number

    print('Your point is now a ', r)
    print('You now have $', chip_count)
    point = r
    while True:
        s = input("Roll again (E=exit)?: ")
        if len(s) > 0 and s[0] in 'Ee':
            return
        r = roll ()
        chip_count += 2
        print('You rolled a', r)
        print('You now have $', chip_count)

# To start simply, each roll that doesn't lose will add $2
# Created by Seth Fort

        if r == point:
            chip_count += 5
            print('You\'re a WINNER!\n')
            print('You now have $', chip_count)
            return

# A winning point roll where the player rolls their number, add an extra $5

        elif r == 7:
            chip_count -= 7
            print('Sorry, you\'re a LOSER. \n')
            print('You now have $', chip_count)

# A crap out will take $7

            return

def roll():
    d1 = randint(1,6)
    d2 = randint(1,6)
    print(d1, d2)
    return d1 + d2

# these are the randomized dice rolls

main()

