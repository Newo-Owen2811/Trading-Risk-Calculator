import os
import random

G = "\033[92m"       
Y = "\033[93m"       
O = "\033[38;5;208m" 
R = "\033[91m"       
CR = "\033[0m"        

def simulation(p, rounds):
    win = 0
    sim = p / 100
    for _ in range(rounds):
        x = random.random()
        if x <= sim:
            win += 1
    ar = (win / rounds) * 100 if rounds > 0 else 0
    
    return f"You won {win} out of {rounds} times! ({ar:.2f}% actual win rate)"

def loss_streak_simulation(p, totalt, ts, trials=10000):
    sim = p / 100.0
    streak_hits = 0

    for _ in range(trials):
        cls = 0
        hit = False
        
        for _ in range(totalt):
            x = random.random()
            if x <= sim:
                cls = 0  
            else:
                cls += 1  
                if cls >= ts:
                    hit = True
                    break  
                    
        if hit:
            streak_hits += 1

    return (streak_hits / trials) * 100

def gni(pro):
    while True:
        try:
            return float(input(pro))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- RISK PER TRADE GUIDE ---")
    print(f"   {G}≤ 2%  Conservative{CR}")
    print(f"   {Y}2 - 4%  Moderate{CR}")
    print(f"   {O}5 - 10% Aggressive{CR}")
    print(f"   {R}> 10%  Extreme{CR}")
    print("----------------------------")
    print("1. Calculate Risk")
    print("2. Calculate Chances")
    print("3. Simulation")
    print("4. Exit")
    
    choice = input("\nSelect an option: ")

    if choice == "1":
        capital = gni("\nEnter your total account balance ($): ")
        risk_percentage = gni("Enter the percentage you want to risk (%): ")
        
        car = capital * (risk_percentage / 100)
        lstba = capital / car

        print(f"\n-> Cash amount at risk per trade: ${car:,.2f}")
        print(f"-> Consecutive losses to wipe out your account: {int(lstba)}")

        input("\nPress Enter to return to the menu...")

    elif choice == "2":
        print("\nHow would you like to calculate the chance?")
        print("A. Single Series Probability (Formula: (1 - winrate)^streak)")
        print("B. Monte Carlo Simulation (Chance of hitting streak across N trades)")
        
        while True:
            subchoice = input("Select calculation type (A/B): ").strip().upper()
            if subchoice in ["A", "B"]:
                break
            else:
                print("Invalid choice. Please enter A or B.")

        rr = gni("Enter your Risk-to-Reward ratio (e.g., 1.5 for 1:1.5): ")
        wr = gni("Enter your historical win rate (%): ")
        ls = gni("Enter the target consecutive loss streak to evaluate: ")
        
        if subchoice == "B":
            totlt = int(gni("Enter total number of trades in your sample (e.g., 100): "))
            print(f"\nRunning {totlt} simulated series...")
            percent = loss_streak_simulation(wr, totlt, int(ls))
            print(f"\n-> Estimated probability of experiencing a {int(ls)}-loss streak over {totlt} trades: {percent:.2f}%")
            input("\nPress Enter to return to the main menu...")
            
        elif subchoice == "A":
            lr = (100 - wr) / 100
            chance = lr ** ls
            percent = chance * 100
            print(f"\n-> Estimated probability of experiencing {int(ls)} consecutive losses: {percent:.2f}%")
            input("\nPress Enter to return to the main menu...")
        
    elif choice == "3":
        winrate = gni("Enter win rate (%): ")
        rounds = int(gni("Enter rounds: "))
        result = simulation(winrate, rounds)
        print(f"\n-> {result}")
        input("\nPress Enter to return to the main menu...")

    elif choice == "4":
        print("\nGoodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")