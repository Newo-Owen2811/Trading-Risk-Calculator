import os

# Color code
G = "\033[92m"       
Y = "\033[93m"       
O = "\033[38;5;208m" 
R = "\033[91m"       
CR = "\033[0m"        


def gni(pro):
    while True:
        try:
            return float(input(pro))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("--- RISK PER TRADE GUIDE ---")
    print(f"   {G}≤ 2%   Conservative{CR}")
    print(f"   {Y}2 - 4%  Moderate{CR}")
    print(f"   {O}5 - 10% Aggressive{CR}")
    print(f"   {R}> 10%  Extreme{CR}")
    print("----------------------------")
    print("1. Calculate Risk")
    print("2. Calculate Chances ")
    print("3. Exit")
    
    choice = input("\nSelect an option: ")

    if choice == "3":
        print("\nGoodbye!")
        break
    elif choice == "2":
       rr = gni("Enter your Risk-to-Reward ratio (e.g., 1.5 for 1:1.5): ")
       wr = gni("Enter your historical win rate (%): ")
       ls = gni("Enter the target consecutive loss streak to evaluate: ")
       lr = (100 - wr) / 100
       chance = lr ** ls
       percent = chance * 100
       print(f"\n-> Estimated probability of experiencing {int(ls)} consecutive losses: {percent:.2f}%")
       input("\nPress Enter to return to the main menu...")

    elif choice != "1":
        print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")
        continue

    capital = gni("\nEnter your total account balance ($): ")
    risk_percentage = gni("Enter the percentage you want to risk (%): ")
    
    #Math
    car = capital * (risk_percentage / 100)
    lstba = capital / car

    # results
    print(f"\n-> Cash amount at risk per trade: ${car:,.2f}")
    print(f"-> Consecutive losses to wipe out your account: {int(lstba)}")

    input("\nPress Enter to return to the menu...")
#To be continued


