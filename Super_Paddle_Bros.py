# Import dependencies
from random import *
import time
import sys


class Characters:      #class location
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def display(self):
        return [self.name, self.hp, self.attack]
    # function to return current stats from other functions as a list. This list used to update value in class


class Difficulty:         #class location
    def __init__(self, multiplier):
        self.multiplier = multiplier


class fish_counter:        #class location
    def __init__(self, counter):
        self.counter = counter


def intro():
    possible_numbers = ["1", "2", "3"]
    # print statement
    print("""Hello player, welcome to Super Paddle Bros!!          
    \nYou will be traversing down a dangerous river with your trusty stand-up paddle board. 
    Your journey on the river will end if the health of your SUP or your own health reaches zero.
    Make careful decisions so that you can reach Paradise Island at the end of this long adventure.
    Select your difficulty and get on your way!""")
    diff = input("\nDifficulty Choices:\n [1]Easy\n [2]Medium\n [3]Hard\n What difficulty would you like? ")
    while diff not in possible_numbers:
        print("Sorry, that wasn't an option.")
        diff = input("\nDifficulty Choices:\n [1]Easy\n [2]Medium\n [3]Hard\n What difficulty would you like? ")
    diff = int(diff)
    if diff == 1:
        print('\nHAH! I see you don''t have your sea legs yet. Black Beard would be ashamed.')
        Difficulty.multiplier = 1
    elif diff == 2:
        print('\nThe Goldilocks option... How safe of you.')
        Difficulty.multiplier = 1.25
    else:
        print('\nI see you like a challenge... Better be ready!')
        Difficulty.multiplier = 1.5

    return Difficulty.multiplier


def pirateName():
    #dictionary location
    first = {'A': 'Swashbuckler', 'B': 'Shipmate', 'C': 'Two-Toe', 'D': 'Rapscallion', 'E': 'Mad', 'F': 'Creeper',
             'G': 'Mean-Mug', 'H': 'Grubby', 'I': 'Fancy Pants', 'J': 'Money-Buckets', 'K': 'Fish-Face',
             'L': 'Billy-Goat', 'M': 'Periwinkle', 'N': 'Surly', 'O': 'Stinky', 'P': 'Matey', 'Q': 'Royal',
             'R': 'Rascal', 'S': "Plunderin'", 'T': 'Peg-Leg', 'U': 'Jolly', 'V': 'Captain', 'W': 'Sea', 'X': 'Spike',
             'Y': 'Peg-Leg', 'Z': 'Booty'}
    #Dictionary location
    last = {'a': 'Wobbly-Peg', 'b': 'the Kidd', 'c': 'Stink-a-lot', 'd': 'Fishmonger', 'e': "O'Greedy",
            'f': "O'Patches", 'g': 'Stinky-Breath', 'h': "d'Plank", 'i': 'Cannon-Shooter', 'j': 'Dirty-Locks',
            'k': 'Shady-Cooper', 'l': 'Landlubber', 'm': 'McWinky', 'n': 'Hook-Hand', 'o': 'Freebooter',
            'p': 'Shipwreck','q': 'McStubby', 'r': 'Lobster-Legs', 's': 'McMonkey', 't': 'Puffy-Pants', 'u': 'Big-Lips',
            'v': 'Tuna-Toes', 'w': 'Sparrow', 'x': 'Sparrow', 'y': 'Three-Eyes', 'z': "O'Jelly"}

    print('Are you ready?? Let''s g...\n\nWoah there, not so fast. First I need to know your name.')

    f = input('\nWhat is your first initial? ')
    l = input('What is your last initial? ')
    f = f.upper()
    l = l.lower()
    while f not in first.keys() or l not in last.keys():
        print('Please only input one letter.')
        f = input('What is your first initial? ')
        l = input('What is your last initial? ')
        f = f.upper()
        l = l.lower()

    name = first.pop(f) + ' ' + last.pop(l)
    print('\n\nWell hello there, ' + name + '! Adventure awaits!')

    return name


def fork(name, playerhp, SUPhp):          #function definition location
    player = Characters(name, playerhp, 10)
    SUP = Characters('Funny SUP Name', SUPhp, 0)
    # temporary characters for this function, with hp coming from current state in the game

    possible_choices = ["Right", "Left", "right", "left"]

    print("\nYou are faced with a fork in the river. On the left you see intense white water rapids that will "
          "probably\ndamage your SUP, but you can see a smooth ending to this route. \nOn the right you see a smooth "
          "beginning,but the river bends around a large cliff. The end of this route is unknown.")

    route = input("\nWhich route would you like to take? Right or Left? \n")
    while route not in possible_choices:
        route = input(" Please use correct spelling. Which route would you like to take? Right or Left? \n")

    if route == "Left" or route == "left":
        # Random int
        damage = randint(5, 30)
        print("\nYou have decided to take the white water portion of the river suffered some damage to your SUP.")
    if route == "Right" or route == "right":       #nested if loop location
        rand_right = randint(1, 4)
        # Nested if loop
        if rand_right == 1:                        #nested if loop location
            print("\nThe curve around the bend was nothing to worry about. Nothin' but sunshine and rainbows so far:)")
            damage = 0
        elif rand_right == 2:
            damage = 20
            print("\nThe path got a little bit rougher after the bend and you sustained light damage.")
        else:
            print("\nOhhh buddy. Sharp rocks and fast water after the bend caused heavy damage to your SUP.")
            damage = 40

    damage = damage * Difficulty.multiplier
    SUP.hp += -damage
    print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)
    # will display health after every decision
    s = SUP.display()
    return s


def game_rules():         #function definition location
    print("\n\nThis game will consist of many difficult challenges.")
    print("Each challenge will drain the health of your")
    print("character and your SUP. Fishing can help replenish")
    print("your health but you will only have two oppurtunities.")
    print("Now, your adventure begins!!")


def battleMonkeyAlligator(name, playerhp, SUPhp):          #funciton definition location
    player = Characters(name, playerhp, 10)
    SUP = Characters('Funny SUP Name', SUPhp, 0)
    # temporary characters for this function, with hp coming from current state in the game

    alligator = Characters('Aggressive Armenian Alligator', 25, 40)
    monkey = Characters('Banana Slinging Monkey', 15, 15)
    # enemies for this battle

    options = ['1', '2']

    print("\nWatch out! There is an Aggressive Armenian Alligator incoming.\nWhat's that? A Band of Banana Slinging "
          "Monkeys is riding his back.")
    # narrative intro to situation

    while monkey.hp > 0 and alligator.hp > 0:              #while loop
        # while both animals have health remaining

        print('\n [1]- Throw rocks at the monkeys.\n [2]- Give that gator a smack with your paddle.')
        ans = input('What will you do? [1 or 2] ')
        # initial command

        while ans not in options:                        #Nested while loop
            print("\nThat's not one of the options. Try again.")
            print('\n [1]- Throw rocks at the monkeys.\n [2]- Give that gator a smack with your paddle.')
            ans = input('What will you do? [1 or 2] ')

        ans = eval(ans)

        if ans == 1:
            print('\nPerfect aim! You took out a monkey, but his gator pal chomped down on your SUP.')
            monkey.hp += -player.attack                        # +=
            SUP.hp += -alligator.attack * Difficulty.multiplier   # +=
        # monkey gets hurt, but so does the SUP

        elif ans == 2:
            print('\nWhat a whack! But one of those damn monkeys hit you with a banana.')
            alligator.hp += -player.attack                        # +=
            player.hp += -monkey.attack * Difficulty.multiplier     # +=
        # alligator gets hurt but so does the player

        print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)              # Using the formatting for strings
        # will display health after every decision

        if player.hp <= 0 or SUP.hp <= 0:
            print('\n\n\n\nGame Over')
            sys.exit(0)
        # exit program if player or SUP dies.


    # when user kills one of the two enemies
    if alligator.hp <= 0:
        # alligator dies
        print('\nThe alligators fainted! Lucky for you, monkeys don''t know how to swim!')
        print('\nThe path is clear. Please proceed.')

    elif monkey.hp <= 0:
        # monkey dies, but fight continues for one more turn
        print('\nYour stoney onslaught was too much for the attacking monkeys. The gator dives underwater.')
        while alligator.hp > 0:
            # while alligator is still alive
            print('  [1]- Dive in the water and wrestle that reptile.\n  [2]- Use your leg as bait and sucker punch the'
                  ' gator when he comes out.')
            ans = input('What will you do? [1 or 2] ')

            while ans not in options:
                print('\nThat'' not one of the options. Try again.')
                print('  [1]- Dive in the water and wrestle that reptile.\n  [2]- Use your leg as bait and sucker punch'
                      ' the gator when he comes out.')
                ans = input('What will you do? [1 or 2] ')
            # two possible choices, both automatically kill the alligator
            ans = eval(ans)

            if ans == 1:
                print('\nYou dive after him and get the beast in a headlock!\nNo more gator! But that muggy water has '
                      'hurt your eyes.')
                alligator.hp += -player.attack * 3
                player.hp += -10

            elif ans == 2:
                print('\nAs you slide your leg into the cool water, the gator chomps down on your leg! \nYou manage to '
                      'smack him on the nose sending him back where he came from.')
                alligator.hp += -player.attack * 3
                player.hp += -alligator.attack * Difficulty.multiplier

            print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)
            # will display health after every decision

            if player.hp <= 0 or SUP.hp <= 0:
                print('\n\n\n\nGame Over')
                sys.exit(0)
            # exit program if player or SUP dies.

        print('\nThe path is finally clear. Please proceed')
        # will print after alligator and monkey are dead

    p = player.display()
    s = SUP.display()
    return p, s
    # returns a list with the class attributes of the player, and then of the SUP


def fishing(name, playerhp, SUPhp):
    player = Characters(name, playerhp, 10)
    SUP = Characters('Funny SUP Name', SUPhp, 0)

    possible_choices1 = ['1', '2', '3', '4', '5']
    possible_choices2 = ['1', '2', '3', '4', '5', '6']
    possible_choices3 = ['1', '2', '3', '4', '5', '6', '7']

    if Difficulty.multiplier == 1:
        fish_num = randint(1, 5)        # Random number generator
        num_range = " 1 through 5."
        possible_choices = possible_choices1
    if Difficulty.multiplier == 1.25:
        fish_num = randint(1, 6)        # Random number generator
        num_range = " 1 through 6."
        possible_choices = possible_choices2
    if Difficulty.multiplier == 1.5:
        fish_num = randint(1, 7)        # Random number generator
        num_range = " 1 through 7."
        possible_choices = possible_choices3

    print("\nIn order to capture your fish, you will have to guess a number" + num_range)
    print("Do not re-guess number because the value is not changing.")

    list = [1, 2, 3]

    for x in list:                    # Walks through the contents of a list
        user_guess = input("What is your guess?")
        while user_guess not in possible_choices:
            print("\nThat is not a valid guess.")
            user_guess = input("What is you guess?")
        user_guess = int(user_guess)
        if int(user_guess) == int(fish_num):
            player.hp += 15
            print("\nYou gained 15 health!")
            break
        if x == 3 and fish_num != user_guess:
            print("\nSorry you were unable to catch any fish.")

    p = player.display()
    s = SUP.display()
    return p, s


def choice(name, playerhp, SUPhp):
    player = Characters(name, playerhp, 10)
    SUP = Characters('Funny SUP Name', SUPhp, 0)

    possible_choices = ("Fish", "Continue", "fish", "continue")         # Tuple
    print("\nBefore we move on with our journey, would you like to fish?\n"
          "Remember that you can only fish twice to replenish your health.")
    choice = input("Would you like to continue on your journey or use one of your fishing opportunities, Fish or"
                   " Continue? ")

    while choice not in possible_choices:
        choice = input("Please use correct spelling, Fish or Continue? ")
    if choice == 'Fish' or choice == 'fish':
        if fish_counter.counter > 0:
            if choice == "Fish" or choice == "fish":
                fish_counter.counter -= 1
                p, s = fishing(name, playerhp, SUPhp)     #Function that calls another function
                return p, s

        if fish_counter.counter < 1:
            if choice == "Fish" or choice == "fish":
                print("You have already used all of your opportunities to fish.")
                p = player.display()
                s = SUP.display()
                return p, s
    else:
        print("Not feelin' lucky I see. Let's keep moving.")
        p = player.display()
        s = SUP.display()
        return p, s


def waterfall(name, playerhp, SUPhp):
    possible_choices_jungle = ["Slide", "Fight", "Shoot", "slide", "fight", "shoot"]

    player = Characters(name, playerhp, 10)
    SUP = Characters('Funny SUP Name', SUPhp, 0)
    # temporary characters for this function, with hp coming from current state in the game

    print('\n\nWell, who knew that alligators could coordinate with monkeys?\n\n'
          'I''m glad you survived, but the challenges are not over yet. You hear and see a waterfall coming up.\n'
          'It is impossible to know how tall the waterfall is as you can not get close enough without going over\n'
          'the edge. It is too risky to attempt a surf down the falls. You must travel down the cliff and dangerous '
          'jungle with your SUP and gear.')

    print("\nOh no. The beginning of your trek was easy, but you see the entire path down is riddled with cobras.")
    print("You can either flip over your S-U-P and slide down the rest of the cliff, fight your way down the path \n"
          "against the snakes, or shoot your zipline launcher and risk it not getting a firm hold.")
    jungle_choice = input("\nWould you like to Slide, Fight, or Shoot?")

    while jungle_choice not in possible_choices_jungle:
        jungle_choice = input("\nPlease use correct spelling, would you like to Slide, Fight, or Shoot?")

    if jungle_choice == "Slide" or jungle_choice == "slide":
        print("Whoa what a ride! You made it down the hill but severely damaged your S-U-P in the process.")
        jungle_damage = 50
        jungle_damage = jungle_damage * Difficulty.multiplier
        SUP.hp += -jungle_damage

    if jungle_choice == "Fight" or jungle_choice == "fight":
        rand_snake = randint(1, 3)
        snake_damage = 10 * rand_snake
        snake_damage = snake_damage * Difficulty.multiplier
        print("You were bitten by " + str(rand_snake) + " cobras.")
        player.hp += - snake_damage

    if jungle_choice == "Shoot" or jungle_choice == "shoot":
        rand_shot = randint(1, 5)
        if rand_shot == 4:
            print("You are a terrible shot. You're line gave out and you fell to your death.")
            fall_damage = 10000
            player.hp += - fall_damage
        else:
            print("\n\nWhoa! What a ride. You made it safely to the bottom.")

    print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)
    # will display health after every decision

    p = player.display()
    s = SUP.display()
    return p, s


def battleHippoCrane(name, playerhp, SUPhp):
    player = Characters(name, playerhp, 10)
    SUP = Characters('Funny SUP Name', SUPhp, 0)
    # temporary characters for this function, with hp coming from current state in the game

    hippo = Characters('Hardheaded Hippo', 40, 25)
    crane = Characters('Clandestine Crane', 10, 30)
    # enemies for this battle

    options = ['1', '2']

    print('\nYou see a Crew of Clandestine Cranes approaching. \nAs they approach, your worst fears are confirmed. '
          '\nThey are using Baby Hippos as artillery on your SUP! \nWATCH OUT!!')
    # narrative intro to situation

    while crane.hp > 0:
        # while crane has health remaining

        print(
            '\n [1]- Use a blanket to trampoline that hippo right back.\n [2]- Use a vine to lasso those cranes to the'
            ' ground.')
        ans = input('What will you do? [1 or 2]')
        # initial command

        while ans not in options:
            print('That''s not one of the options. Please try again.')
            print('\n [1]- Use a blanket to trampoline that hippo right back.\n [2]- Use a vine to lasso those cranes '
                  'to the ground.')
            ans = input('What will you do? [1 or 2]')
        ans = eval(ans)

        if ans == 1:
            print(
                '\nThe hippo got launched by your blanket, it flew up, got dodged by the crane, and came crashing down '
                'on your SUP. Try something else!')
            SUP.hp += -crane.attack * Difficulty.multiplier
        # bad news bears

        elif ans == 2:
            print('\nYou swing that vine like Indiana Jones and latch onto the cranes beak! You tug on the vine and the'
                  ' crane comes tumbling down.')
            crane.hp += -player.attack
        # good news geese

        print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)
        # will display health after every decision

        if player.hp <= 0 or SUP.hp <= 0:
            print('\n\n\n\nGame Over')
            sys.exit(0)
        # break if player or SUP dies.



    # when user kills the goose
    print('\nYou see something move in the water... \nOH NO! A Hardheaded Hippopotamus peeks her head out... '
          '\nWatch out for mother''s revenge!')
    while hippo.hp > 0:
        # while hippo  has health remaining

        if player.hp <= 0 or SUP.hp <= 0:
            print('\n\n\n\nGame Over')
            sys.exit(0)
        # break if player or SUP dies.
        ans = 2
        while ans == 2:

            if hippo.hp <= 0:
                break
            # if hippo dies

            print(' [1]- Use your paddle to hit the hippo. \n [2]- Throw a boomerang at the hippo.')
            ans = input('What will you do? [1 or 2]')
            # initial command

            while ans not in options:
                print("That's not one of the options. Please try again.")
                print('\n [1]- Use your paddle to hit the hippo. \n [2]- Throw a boomerang at the hippo.')
                ans = input('What will you do? [1 or 2]')
            ans = eval(ans)

            if ans == 1:
                print('\nOH NO! The hippo snaps your paddle in two!')
                print('\n\n\nYour paddle is broken. What will you do now??')
                SUP.hp += -hippo.attack * Difficulty.multiplier
                break

            # bad news bears

            elif ans == 2:
                print('\nYou thump the hippo on the snout and the boomerang comes back to your hands.\n'
                      'The hippo retaliates with an Aqua Blast to the chest. The wind is knocked out of you.')
                hippo.hp += -player.attack
                player.hp += -hippo.attack * Difficulty.multiplier

            print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)
            # will display health after every decision

            if player.hp <= 0 or SUP.hp <= 0:
                print('\n\n\n\nGame Over')
                sys.exit(0)

        while hippo.hp > 0:

            print('\n [1]- Use your machete blade. \n [2]- Throw a boomerang at the hippo.')
            ans = input('What will you do? [1 or 2]')

            while ans not in options:
                print('That''s not one of the options. Please try again.')
                print('\n [1]- Use your machete blade. \n [2]- Throw a boomerang at the hippo.')
                ans = input('What will you do? [1 or 2]')
            ans = eval(ans)

            if ans == 1:
                print('\nKAPOW!! That sure hurt momma Hippo.\nShe turns around and booty bumps your SUP.')
                hippo.hp += -player.attack
                SUP.hp += - hippo.attack * Difficulty.multiplier
            # bad news bears

            elif ans == 2:
                print('\nYou thump the hippo on the snout and the boomerang comes back to your hands.\n'
                      'The hippo retaliates with an Aqua Blast to the chest. The wind is knocked out of you.')
                hippo.hp += -player.attack
                player.hp += -hippo.attack * Difficulty.multiplier
            # good news geese

            print('   Health: ', player.hp, '\n   SUP: ', SUP.hp)         # Using the formatting for strings
            # will display health after every decision

            if player.hp <= 0 or SUP.hp <= 0:
                print('\n\n\n\nGame Over')
                sys.exit(0)

    print('\nThe path is finally clear. Please proceed')
    # will print after alligator and monkey are dead
    p = player.display()
    s = SUP.display()
    return p, s
    # returns a list with the class attributes of the player, and then of the SUP


def victory(name):
    print("--------------------------------------------------------------")
    print("YAAAAAAAAAYYYYYYYYYY!!! YOU MADE IT TO PARADISE ISLAND!!!!")
    print("WE HAVE RESTORED ALL OF YOUR HEALTH AND FIXED YOUR S-U-P!")
    print("Thank you " + name + " for playing Super Paddle Bros.!")
    time.sleep(5)

def final_animation():
    print("                 --")
    print("                 ||")
    print("                 ||")
    print("                 --")
    print("")
    time.sleep(.25)
    print("            --")
    print("            ||")
    print("            ||")
    print("            --")
    print("")
    time.sleep(.25)
    print("          --")
    print("          ||")
    print("          ||")
    print("          --")
    print("")
    time.sleep(.25)
    print("       --")
    print("       ||")
    print("       ||")
    print("       --")
    print("")
    time.sleep(.25)
    print("    --")
    print("    ||")
    print("    ||")
    print("    --")
    print("")
    time.sleep(.25)
    print("   --")
    print("   ||")
    print("   ||")
    print("   --")
    print("")
    time.sleep(.25)
    print("      --")
    print("      ||")
    print("      ||")
    print("      --")
    print("")
    time.sleep(.25)
    print("        --")
    print("        ||")
    print("        ||")
    print("        --")
    print("")
    time.sleep(.25)
    print("          --")
    print("          ||")
    print("          ||")
    print("          --")
    print("")
    time.sleep(.25)
    print("             --")
    print("             ||")
    print("             ||")
    print("             --")
    print("")
    time.sleep(.25)
    print("                --")
    print("                ||")
    print("                ||")
    print("                --")
    print("")
    time.sleep(.25)
    print("                  --")
    print("                  ||")
    print("                  ||")
    print("                  --")
    print("")
    time.sleep(.25)
    print("                      --")
    print("                      ||")
    print("                      ||")
    print("                      --")
    print("")
    time.sleep(.25)
    print("                        --")
    print("                        ||")
    print("                        ||")
    print("                        --")
    print("")
    time.sleep(.25)
    print("                     --")
    print("                     ||")
    print("                     ||")
    print("                     --")
    print("")
    time.sleep(.25)
    print("                 --")
    print("                 ||")
    print("                 ||")
    print("                 --")
    print("")
    time.sleep(.25)
    print("                 --  ___                  ")
    print("                 || |   |                 ")
    print("                 || |   |                 ")
    print("                 -- |   |                 ")
    print("           _________|   |______           ")
    print("          /                    \          ")
    print("         /                      \         ")
    print("        /      PARADISE          \        ")
    print("  _____/        ISLAND            \       ")
    print(" |                                 \      ")
    print(" |                                  \     ")
    print(" |___________________________________\    ")

def main():
    get_multiplier = intro()

    name = pirateName()
    player = Characters(name, 100, 10)
    SUP = Characters('Black Pearl', 300, 0)

    game_rules()        #function call location

    fish_counter.counter = 2

    # Fork
    s = fork(name, player.hp, SUP.hp)       #function call location
    SUP = Characters(s[0], s[1], s[2])
    if player.hp <= 0 or SUP.hp <= 0:
        print('Game Over')
        sys.exit(0)

    p, s = choice(player.name, player.hp, SUP.hp)
    player = Characters(p[0], p[1], p[2])
    SUP = Characters(s[0], s[1], s[2])

    # Monkey-Alligator Battle
    p, s = battleMonkeyAlligator(player.name, player.hp, SUP.hp)     #function call location
    player = Characters(p[0], p[1], p[2])
    SUP = Characters(s[0], s[1], s[2])

    p, s = choice(player.name, player.hp, SUP.hp)
    player = Characters(p[0], p[1], p[2])
    SUP = Characters(s[0], s[1], s[2])

    # Waterfall
    p, s = waterfall(player.name, player.hp, SUP.hp)
    player = Characters(p[0], p[1], p[2])
    SUP = Characters(s[0], s[1], s[2])
    if player.hp <= 0 or SUP.hp <= 0:
        print('\n\n\n\nGame Over')
        sys.exit(0)

    p, s = choice(player.name, player.hp, SUP.hp)
    player = Characters(p[0], p[1], p[2])
    SUP = Characters(s[0], s[1], s[2])

    # Hippo-Crane Battle
    p, s = battleHippoCrane(player.name, player.hp, SUP.hp)
    player = Characters(p[0], p[1], p[2])
    SUP = Characters(s[0], s[1], s[2])

    final_animation()
    victory(name)

main()
