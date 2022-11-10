def game():
    import random

    n = int(input("Enter max range of the number"))
    t = int(input("Enter number of turns"))

    number = random.randint(1,n)

    turns = t

    print("\nYou have 5 tries to guess the number\n",number)

    while True:
        
        guess = int(input("Guess the number: "))

        if turns != 1:
        
            if guess > number:
                print("\ntoo high think of a lower value")
                
            elif guess < number:
                print("\nToo low think of a higher value")

            elif guess == number:
                print("\nThat was correct the number was ",number)
                break

        if turns == 1:
            print("oh no you lost the game ")
            break

        turns -= 1

        print("\nNumber of turns left are ",turns,"\n")

    if input("Enter y to paly again: ") in "Yy":
        game()

game()
