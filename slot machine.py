"""Slot Machine Project:
Needed: User input, User balance, spin/play function, lines/wheels"""

#imports
import random

def lines(bet, bal):
    print(f"Betting: {bet}, Spinning...")
    apple = 2
    orange = 3 
    banana = 4
    line1 = [apple, orange, banana]
    line2 = [orange, banana, apple]
    line3 = [banana, apple, orange]
    spin_num1 = random.randint(0,2)
    spin_num2 = random.randint(0,2)
    spin_num3 = random.randint(0,2)
    result1 = line1[spin_num1]
    result2 = line2[spin_num2]
    result3 = line3[spin_num3]
    if (result1) == (result2) == (result3):
        overall_result = (result1) + (result2) + (result3) + bet #needs to be checked
        if result1 == apple:
            multipler = (float(result1))*2 + 0.5
        elif result1 == orange:
            multipler = result1
        else:
            if result1 == banana:
                multipler = (float(result1))*2 + 0.5
        print(f"You've spun a: {result1}, {result2}, and {result3}!\nWinnings: ${overall_result}")
        overall_result = overall_result * multipler
        print(f"{result1}, {result2}, {result3} = {multipler}x multipler!\nOverall Total: {overall_result}")
        newbal = bal + overall_result
        print(f"New wallet balance is: {newbal}")
        return newbal
    else:
        print(f"You've spun: {result1}, {result2}, {result3}, must spin 3 in a row! ")
        print(f"New wallet balance is: {bal}")
        return bal
        
def spin(balance):
    t = True
    z = -1
    while t:
        if z == -1:
            z = balance
            spin = input("Do you wish to: Spin(S) or Leave now(Q)?: ")
            if spin == "Q":
                t = False
            elif spin == "S":
                while True:
                    init_bet = input(f"Balance: {z}\nHow much of your wallet do you wish to bet?: $ ")
                    try:
                        int_bet = int(init_bet)
                    except:
                        print("Error! Invalid Input")
                        continue
                    else:
                        if int_bet > z:
                            print("Sorry, Bet is greater than your Wallet amount, deposit more to bet more!")
                            continue
                        elif int_bet <= z:
                            z = z - int_bet
                            break
                        else:
                            print("Error! Invalid input!")
                            continue
                z = lines(int_bet, z)
                continue
            else:
                print("Error!: Invalid input")
                continue
        elif z <= 0:
            broke = input("Out of Funds! Must Deposit more! Do you wish to: Deposit(D) or Leave now(Q)?:")
            if broke == "Q":
                t = False
            elif broke == "D":
                while True:
                    a = z + ((-z)*2) #absolute value of the negative balance
                    dep = input(f"How much of your wallet do you wish to deposit?(Wallet: {z}): $ ")
                    try:
                        dep = int(dep)
                    except:
                        print("Error! Invalid Input!")
                        continue
                    else:
                        if dep <= a:
                            print("Deposit amount not enough, Try again")
                            continue
                        else:
                            break
                z = dep
                continue
            else:
                print("Error!: Invalid input")
                continue
        else:
            spin = input("Do you wish to: Spin(S) or Leave now(Q)?: ")
            if spin == "Q":
                t = False
            elif spin == "S":
                while True:
                    init_bet = input(f"Balance: {z}\nHow much of your wallet do you wish to bet?: $ ")
                    try:
                        int_bet = int(init_bet)
                    except:
                        print("Error! Invalid Input")
                        continue
                    else:
                        if int_bet > z:
                            print("Sorry, Bet is greater than your Wallet amount, deposit more to bet more!")
                            continue
                        elif int_bet <= z:
                            z = z - int_bet
                            break
                        else:
                            print("Error! Invalid input!")
                            continue
                z = lines(int_bet, z)
                continue
            else:
                print("Error!: Invalid input")
                continue
    return z

def main():
    startbal = 0
    print("Well hello there fellow bettor!\nI've noticed you've fallen prey to the lure of our new and improved slot machine")
    t = True
    while t: 
        deposit = input("The 'Spin-3000', now I know your tempted to play...\nSo how much do you want to deposit?: $ ")
        if int(deposit) > 0:
            startbal = startbal + int(deposit)
            print(f"Alright, that gives you a wallet of: ${startbal}")
            t = False
        else:
            print("Error: valid numeric values only!")
            continue
    return startbal, int(deposit)

if __name__ == "__main__":
    y, z = main()
    x = spin(y)
    if x < z:
        print(f"Final Balance: {x}\nThanks for playing with us! Ha Ha Ha, Better 'luck' next time....")
    else:
        print(f"Final Balance: {x}\nThanks for playing with us! You've got the best of us! Until next time....")
