import time
import random

# Print text with some delay


def print_pause(text_to_print):
    time.sleep(2)
    print(text_to_print)

# Makes the choosable options and control if the answer is correct


def correct_answer(question, options):
    correct_opt = []
    wrong_text = "Choose from: "

    for index in range(len(options)):
        time.sleep(1)
        print(options[index])
        correct_opt.append(str(index+1))

        if index == len(options)-1:
            wrong_text = wrong_text + str(index+1)
        else:
            wrong_text = wrong_text + str(index+1) + " or "

    while True:
        time.sleep(1)
        answer = input(f"{question}\n")
        if answer in correct_opt:
            return answer
        else:
            print_pause(wrong_text)

# The game restart function


def game_replay():
    print_pause("Do you want to play again?")
    replay = input("1. Yes\n"
                   "2. No\n")
    if replay == "1":
        print_pause("Reloading the game...")
        play_game()
    else:
        print_pause("Thanks..till next time!")

# Start to play the game


def play_game():
    random_creature = ["a small gnome", "a glamorous fairy",
                       "The Grim Reaper", "your wife"]
    random_fainting = ["slip, hit your head into the cabinet",
                       "in the excitement you feel a big pressure on your "
                       "chest",
                       "while it's casting a strange spell on you"]
    items = []
    creature = random.choice(random_creature)
    fainting = random.choice(random_fainting)
    intro(items, creature, fainting)

# The intro for the game with some random factors


def intro(items, creature, fainting):
    print_pause("It's a usual life rotation, work, eat, sleep in daily "
                "repeat.")
    print_pause("One night while you watching your favorite show, you hear a "
                "strange noise from your bedroom.")
    print_pause(f"You rush inside your room, where you see {creature} at your "
                "shelf searching for something.")
    print_pause("You sanding there processing, what is it looking for?!")

    if creature == "your wife":
        print_pause("But wait! You was living alone in your entire life! "
                    "You dont have a wife!!")

    print_pause("After a short time it's turning around and start heading "
                "into your direction!")
    print_pause(f"You start panicking and {fainting},everything goes black...")
    print_pause("....")
    print_pause("After a while you wake up.")
    print_pause("You find yourself in a very old and rundown elevator.")
    ride_elevator(items, creature)

# The lobby floor and its events


def lobby_floor(items, creature):
    if "Elevator service key" in items:
        print_pause("You using the elevator service key, trying to push "
                    "the button...")
        print_pause("it works!! You find yourself in the lobby,you start "
                    "running towards to the exit")
        print_pause("falling out of the doors.... and you find yourself "
                    "in your bedroom on the floor.")
        print_pause("You realize that you was very exhausted from working "
                    "overtime yesterday.")
        print_pause("After your little nap heading back to wach your "
                    "favorite show, ")
        print_pause(f"sitting down into the couch ,you see the {creature} in "
                    "the tv what you saw before")

        if creature == "your wife":
            print_pause("But you are still iving alone!!")
        else:
            print_pause("But it's turning its head and looks you right in the "
                        "eye and winks...")
            print_pause("Here you are, continuing our everyday life... or "
                        "maybe not...")
            print_pause("The End")
    else:
        print_pause("You trying to push the button, but it won't budge "
                    "it's stuck.")
        ride_elevator(items, creature)

# Medical floor and its events


def medical_floor(items, creature):
    question = "What do you do?"
    options = ["1. Get back into to elevator and close the door",
               "2. Try to outrun him and look around."]

    if "headache pills" in items:
        print_pause("You have looked this floor truly though. You don't find "
                    "any reason to disturb the creature in there.")
        ride_elevator(items, creature)

    else:
        print_pause("It's a small Medical station, there is dust everywhere.")
        print_pause("A bandaged creature turning towards you while moaning "
                    "start to walk in a fast pace into your direction.")
        answer = correct_answer(question, options)

        if answer == "1":
            print_pause("You rapidly pushing the close button in the elevator")
            print_pause("the door is shut, you are safe!")
            ride_elevator(items, creature)
        elif answer == "2":
            if "sportshoes" in items:
                print_pause("You are running like butter on the hot knife in "
                            "your legendary shoes!")
                print_pause("The creature cannot keep up with the pace and "
                            "falls to the ground.")
                print_pause("It's not moving, now you have time to check "
                            "around.")
                print_pause("You see a metal cabinet in the corner with "
                            "a big padlock on it")

                if "padlock key" in items:
                    print_pause("You using the key to open it, and find some "
                                "headache pills")
                    print_pause("you take it put it in your pocket.")
                    print_pause("Heading back to the elevator")
                    print_pause("You got headache pills!")
                    items.append("headache pills")
                    ride_elevator(items, creature)

                else:
                    print_pause("You trying to open it, but the padlock is "
                                "massive. No chance!")
                    print_pause("Looks like the creature start to get back "
                                "on its feets,")
                    print_pause("using the short time you get back in the "
                                "elevator")
                    ride_elevator(items, creature)

            else:
                print_pause("Trying to outmanouver it but ist faster than "
                            "it looks...")
                print_pause("the creature grabs you and tickles you to the "
                            "next world!")
                game_replay()

# The spoorts floor evetns


def sport_floor(items, creature):
    question = "Do you want to approach it?"
    options = ["1. Yes",
               "2. No"]

    if "sportshoes" in items:
        print_pause("You enter into an abandoned sport shop, see some trash "
                    "and stuff there.")
        print_pause("As you looking around again, you see nothing particular")
        print_pause("You turning back and get in the elevator.")
        ride_elevator(items, creature)

    else:
        print_pause("You enter into an abandoned sport shop, see some trash "
                    "and stuff there.")
        print_pause("As you looking around something catch your eyes!")
        print_pause("A shining box on one shelf!")
        print_pause("You approaching it, lighs even brighter, and you not "
                    "even sure do you want to go even closer!!!")
        answer = correct_answer(question, options)

        if answer == "1":
            print_pause("As you going there with your eyes closed, you "
                        "arrived to the box.")
            print_pause("Opening it you find in there a "
                        "legendary running shoes.")
            print_pause("On the box cover stays: 'Faster than the fastest "
                        "man on the earth.'")
            print_pause("You throw your old 'average' shoe away, and pull "
                        "the legendary shoes on, its passes perfectly.")
            print_pause("Now you have a Legendary running shoes!")
            items.append("sportshoes")
            print_pause("You turning back and get in the elevator.")
            ride_elevator(items, creature)
        elif answer == "2":
            print_pause("You turning back and get in the elevator.")
            ride_elevator(items, creature)

# Manager floor evetns


def manager_floor(items, creature):
    question = "What do you do?: "
    options = ["1. You see some unknow pills on the other table, try to "
               "give it to him.",
               "2. Head back to the elevator, elevator and search for help."]
    question_2 = "What will you do?: "
    options_2 = ["1. Run back to the elevator",
                 "2. Try to fight him!",
                 "3. Stay there and accept your fate.."]

    if "Elevator service key" in items:
        print_pause("The man just sitting there happy without headaches")
        print_pause("You done here, heading back to the elevator")
        ride_elevator(items, creature)

    else:
        if "headache pills" in items:
            options.append("3. Give him the headache pills.")

        print_pause("You step into a sparkling clean room,")
        print_pause("there is a big table with some golden statues on it,")
        print_pause("behind the table sits a generous looking old man.")
        print_pause("He has a terrible headache, and ask for your help!")
        answer = correct_answer(question, options)

        if answer == "1":
            print_pause("He takes the pills, thereafter you hear some "
                        "clicking noise, ")
            print_pause("shortly he goes berserk and attacking you,")
            answer_2 = correct_answer(question_2, options_2)

            if answer_2 == "1":
                print_pause("The elevator doors are not opening, pressing the "
                            "button does nothing! You thinking back to the "
                            "clicking sound... ")
                print_pause("he's catching up with you holding you down on "
                            "the ground and... ")
                print_pause("start to ask some very annoying questions what "
                            "annoys you to the next world!!!")
                game_replay()

            elif answer_2 == "2" or answer_2 == "3":
                print_pause("You have no chance against its massive power, ")
                print_pause("he's holding you down on the ground and start "
                            "to ask some very annoying questions ")
                print_pause("what annoys you to the next world.")
                game_replay()

        elif answer == "2":
            if "padlock key" in items:
                print_pause("You turning back and to the elevator and "
                            "search for help.")
                ride_elevator(items, creature)

            else:
                print_pause("You turning back and to the elevator and "
                            "search for help.")
                print_pause("But wait...!! he says")
                print_pause("here is a padlock key take it.")
                print_pause("Now you have a padlock key!")
                items.append("padlock key")
                ride_elevator(items, creature)

        elif answer == "3":
            print_pause("He takes the pills and gets better almost "
                        "immediately, ")
            print_pause("after thanking... he gives you the "
                        "Elevator service key.")
            print_pause("You got the Elevator service key")
            items.append("Elevator service key")
            ride_elevator(items, creature)

# Using the elevator


def ride_elevator(items, creature):
    question = "Choose a number for the floor you would like to visit:"
    options = ["1. Lobby",
               "2. Medical Floor",
               "3. Sport Shop Floor",
               "4. Manager floor"]
    answer = correct_answer(question, options)

    if answer == "1":
        lobby_floor(items, creature)
    elif answer == "2":
        medical_floor(items, creature)
    elif answer == "3":
        sport_floor(items, creature)
    elif answer == "4":
        manager_floor(items, creature)
    else:
        ride_elevator()


play_game()
