from random import randrange

while True:
    menu = input("Please choose:\n1 Number Guess game\n2 Quit\n")
    if menu == "1":
        print("Welcome to Number Guess!! To End enter '101'")
        while True:
            try:
                guess = input("Enter number between 1 to 10:\n")
                value = int(guess)
                minn = 1
                maxx = 10
                randomize = randrange(1,11)
                if  value == 101:
                    print("Good game! See you soon.")
                    break
                elif value > maxx:
                    print("Please enter only numbers between 1 to 10.")
                    continue
                elif value < minn:
                    print("Please enter only numbers between 1 to 10.")
                elif value == randomize:
                    print("Your guess is: ", value ,"\nThe random number is: ", randomize)
                    print("Well Done! Good Guess fam!")
                    continue
                elif value != randomize:
                    print("Your guess is: ", value ,"\nThe random number is: ", randomize)
                    print("Bad luck! Try again bud")
                    continue   
                else:
                    print("Invalid")
            except ValueError:
                print("Invalid input. Enter only numbers")
    elif menu == "2":
        print("Thank you, see you!")
        quit()
    else:
        print("Invalid input")