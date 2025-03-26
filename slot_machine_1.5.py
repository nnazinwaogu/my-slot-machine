"""Author: Nnazirim Nwaogu"""

#imports
import random

def bet(startingbalance, currbalance, netpos, spins, wagered):
    while True:
        userInput = input(f"Current Balance: ${currbalance} | P/L: ${netpos}\nEnter 1 to Spin, 2 to Quit:  \n")
        if int(userInput) != 1 and int(userInput) != 2:
            print("Silly Goose! That's an invalid input!\n")
            continue
        elif int(userInput) == 2:
            print("Leaving now...\n")
            leave(startingbalance, currbalance, netpos, spins, wagered)
            break 
        elif int(currbalance) <= 0:
            print(f"Oops, Your current balance is: ${currbalance}. You must deposit to continue.\n")
            print("When you return to the menu, spin again and you wil be prompted to deposit!\n")
            leave(startingbalance, currbalance, netpos, spins, wagered)
            break
        else:
            while True:
                bet = input(f"Current Balance: ${currbalance} -- Enter your wager amount:  \n")
                if int(bet) > int(currbalance) or int(bet) <= 0:
                    print("Haha! You can't do that!\n")
                    continue
                else:
                    currbalance, netpos, spins, wagered = lines(currbalance, netpos, spins, wagered, bet) #updating modified variables
                    break
            continue
    return startingbalance, currbalance, netpos, spins, wagered
    

def lines(currbalance, netpos, spins, wagered, bet): #want to separate the slot function logic from the betting logic 
    #this operates as a simple, 3-row, 1-line slot machine
    apple = 1
    orange = 1.5
    banana = 2
    lines = [[apple, orange, banana],
             [orange, banana, apple],
             [banana, apple, orange],]
    multiplerArray = [1, 2, 1, 4, 1, 6, 1, 8, 1, 10, 1, 12]
    
    spinNum1 = random.randint(0,2)
    spinNum2 = random.randint(0,2)
    spinNum3 = random.randint(0,2)
    multiNum = random.randint(0,11)
    result1 = lines[0][spinNum1]
    result2 = lines[1][spinNum2]
    result3 = lines[2][spinNum3]
    multipler = multiplerArray[multiNum]

    if (result1) == (result2) == (result3):
        overall_result = (result1) + (result2) + (result3) 
        print(f"You've spun a: {result1}, {result2}, and {result3}!\nWinnings: ${overall_result}\n")
        print(f"Spinning multipliers...\nYou've spun a: {multipler}x multiplier!\n")
        overall_result = overall_result * multipler #ignoring wager amount in resultant calculation reduces logic by instruction or two
        print(f"Overall Total: ${overall_result}\n")
        currbalance += overall_result
        print(f"New wallet balance is: ${currbalance}\n")
        netpos += overall_result
        spins += 1
        wagered += int(bet)
    else:
        overall_result = 0 - int(bet) # can't ignore, needed here
        print(f"You've spun: {result1}, {result2}, {result3}, must spin 3 in a row!\n")
        currbalance += overall_result
        print(f"New wallet balance is: ${currbalance}\n")
        netpos += overall_result 
        spins += 1
        wagered += int(bet)
    return currbalance, netpos, spins, wagered
        
def play(startingbalance, currbalance, netpos, spins, wagered):
    while True:
        spin = input("Do you wish to: Spin(1) or Leave now(2)?:  \n")
        if spin == "1":
            if currbalance <= 0:
                print(f"Balance: ${currbalance}\nMust Deposit\n")
                startingbalance, currbalance = deposit(startingbalance, currbalance)
                continue
            else:
                while True:
                    result = input("Do you want to deposit more(1) or not(2)?:  \n")
                    if result == "1":
                        startingbalance, currbalance = deposit(startingbalance, currbalance)
                        continue
                    elif result == "2":
                        print("Game Loading...,\n")
                        startingbalance, currbalance, netpos, spins, wagered = bet(startingbalance, currbalance, netpos, spins, wagered)
                        break 
                    else:
                        print("Silly Goose! Pick 1 or 2!\n")
                        continue
        elif spin == "2":
            print("Good choice ;)\nLeaving now...\n")
            break
        else:
            print("Silly Goose! Pick 1 or 2!\n")
            continue
    return startingbalance, currbalance, netpos, spins, wagered 

def deposit(startingbalance, currbalance): 
    while True:
        currbalancestr = input(f"Balance: ${currbalance} --- How much are you depositing?:  \n")
        if (int(currbalancestr) >= 0):
            currbalance += int(currbalancestr)
            if startingbalance == 0:
                startingbalance = currbalance
            break                 
        else:
            print("Silly Goose! Thats not a valid input\n")
            continue 
    print(f"New Balance: ${currbalance}")
    return startingbalance, currbalance

def leave(startingbalance, currbalance, netpos, spins, wagered):
    print("---RESULTS---\n")
    print(f"Starting Balance: {startingbalance}\n")
    print(f"Spun {spins} times\n")
    print(f"Wagered through ${wagered}\n")
    print(f"Current Balance: {currbalance}\n")
    print(f"Profit/Loss: ${netpos}\n")
    if netpos < startingbalance:
        print("Hope you had fun! Better luck next time!\n")
    else:
        print("Hope you had fun! Spread the luck next time!\n")
    return None


def main():
    #Game Variables 
    startbal = 0 
    currbal = 0 
    netpos = 0 
    result = 0  
    spins = 0
    wagered = 0

    print("Oh!\n Hi there!\n Didn't see you there, trying to throw away your mone- *BANG*\n")
    print(" Ahem.. heh, don't mind that. My Name is Mr.Riggedd, and yes, I know it sounds funny.\n")

    while True:
        result = input(" Anyhoo, were you looking to Play(1) or Leave Now(2) (while you still can!):  \n")
        if result == "1":
            startbal, currbal, netpos, spins, wagered = play(startbal, currbal, netpos, spins, wagered)
            break
        elif result == "2":
            break
        else:
            print("Silly goose, pick between 1 or 2!\n")
            continue
    return leave(startbal, currbal, netpos, spins, wagered)  

if __name__ == "__main__":
    main() 