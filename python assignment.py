from random import choice

def checkup(first_check, second_check):
    first_checkup = "The correct fruits that are in place are:" + str(first_check)
    second_checkup = "The correct fruits that are in the wrong place are: " + str(second_check)
    return print(first_checkup + "\n" + second_checkup + "\n")

Counter = 1    
Start = "YES"
fruits = ["watermelon", "grape", "durian", "mangosteen", "lemon", "rambutan"]


print("#$n#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")
print(" Welcome!, Liivenesh's Mastermind Game invites you")
print("#$#$#$#$#$#$$#$#$#$#$#$#$#$#$#$#$#$#$#$")
print("\n~~~~~~~~~(Guidlines)~~~~~~~~~~~~~~~~")
print("This game contains 8 different types of fruits")
print("(watermelon, grape, durian, mangosteen, lemon, rambutan")
print("\n~~~~~~~~~(Game Instructons)~~~~~~~~~")
print("1. 4 different fruits will be randomized from the 6 different colours shown")
print(" (watermelon, grape, durian, mangosteen, lemon, rambutan)")
print("2. it is required for you to guess the 4 fruits and input your guess ")
print("3. the fruits that are in the correct position will be determined by the game")
print("4. game ends when the colour is guessed correctly")
print("\n~~~~~~~~~(RULES)~~~~~~~~~~~~~~~~~~~~")
print("1. players are given 6 attempts to guess the fruits")
print("2. players who exceed the limit will automatically be Game Over!\n ")



while Start == "YES":
    print("#$#$#$#$#$#$#$#$#$#$#$##$#$#$#$#$#$##$#$#$")
    print("#$#$#$#$#$#$( Game On!!)#$#$#$#$#$#$#$#$#$")
    print("$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")

    Answer = []
    for i in range(6):
        Answer.append(choice(fruits))

    print(str(Answer))

    Win = False
    while True:
        Assessment = False
        Wrong = 0
        Correct = 0
        while not Assessment:
            Assessment = True

            Estimate = []
            for i in range(0,6):
                Estimate.append(str(input("ENTER YOUR FRUIT GUESS\n")).lower().strip())
                if len(Estimate) !=0:
                     print("This is Your Estimation(s):" + (str(Estimate) + "\n"))
                if Estimate[i] not in fruits:

                     print("$#$#$#$#$##$#$#$#$#$#$#$#$#$#$#$#$#$#$#$")   
                     print("#$#$#$#$#(INVALID FRUIT!!)$#$#$#$#$#$#$#")
                     print("$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$") 
                     Assessment = False
                     break



        for i in range(6):
            if Estimate[i] == Answer[i] and Estimate[i] in Answer[i]:
                Correct += 1
                Wrong +=0  

        for i in range(6):
            if Estimate[i] not in Answer and Estimate[i] != Answer[i]:
                Correct += 0 
                Wrong += 0

        if Correct == 6:
            Win = True
            break    
        
        else:
            Counter += 1
            checkup(Correct, Wrong)
            

    print()


    if Win:
        print("********************************************************")
        print("*******(YOU GUESSED IT!! CONGRATULATIONS!!)*************")
        print("*************(MASTERMIND FOUND!!)***********************")
        print("***********(YOU ARE THE MASTERMIND)*********************")    
        print("The answer is" + str(Answer))    
    else:
        print("*******************************************************")
        print("******************(WARNING!!WARNING!!)*****************")
        print("*******************************************************")
        print("The answer is" + str(Answer) + "." + "YOU LOST!")
    

        
    print("Number of attempts used to found the correct fruit arrangement:" + str(Counter))

    
    print("#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")
    print("$#$#$#$#$#$#$#$#$(PLAY AGAIN?)#$#$#$#$#$#$$")
    print("#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")
    ("If Yes Enter Y, if NO Enter N:\n").upper()

    while Start != "YES" and Start != "NO":
        print("You are only allowed to answer with a 'Yes' or 'No'")
        

    Start = input("If Yes Enter YES, if NO Enter NO:\n").upper()
        

    if Start == "YES":
        print()
        print("#$n#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")
        print(" Welcome Back!, Mastermind Game invites you")
        print("#$#$#$#$#$#$$#$#$#$#$#$#$#$#$#$#$#$#$#$")
        print("\n~~~~~~~~~(Guidlines)~~~~~~~~~~~~~~~~")
        print("This game contains 8 different types of fruits")
        print("(watermelon, grape, durian, mangosteen, lemon, rambutan")
        print("\n~~~~~~~~~(Game Instructons)~~~~~~~~~")
        print("1. 4 different fruits will be randomized from the 6 different colours shown")
        print(" (watermelon, grape, durian, mangosteen, lemon, rambutan)")
        print("2. it is required for you to guess the 4 fruits and input your guess ")
        print("3. the fruits that are in the correct position will be determined by the game")
        print("4. game ends when the colour is guessed correctly")
        print("\n~~~~~~~~~(RULES)~~~~~~~~~~~~~~~~~~~~")
        print("1. Players have to enter the first alphabet of each fruits")
        print("2. players are given 6 attempts to guess the fruits")
        print("3. players who exceed the limit will automatically be Game Over!\n ")


    if Start == "NO":
        print()
        print("#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$")
        print("~~~~~~~~~~~~~(GAME ENDED!!)~~~~~~~~~~~~~~~")
        print("><><><><><><><><><><><><><><><><><><><><><")
        print("~~~~~~~~~~~(THANKS FOR PLAYING!)~~~~~~~~~~")
        print("$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#$#")  

#