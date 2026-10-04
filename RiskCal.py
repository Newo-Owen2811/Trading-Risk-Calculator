import os

# Color code
G = "\033[92m"       
Y = "\033[93m"       
O = "\033[38;5;208m" 
R = "\033[91m"       
CR = "\033[0m"        

def get_number_input(prompt_text):
    while True:
        try:
            return float(input(prompt_text))
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
    print("2. Exit")
    
    choice = input("\nSelect an option: ")

    if choice == "2":
        print("\nGoodbye!")
        break
    elif choice != "1":
        print("Invalid choice. Please try again.")
        input("\nPress Enter to continue...")
        continue

    capital = get_number_input("\nEnter your total account balance ($): ")
    risk_percentage = get_number_input("Enter the percentage you want to risk (%): ")

    #Math
    car = capital * (risk_percentage / 100)
    lstba = capital / car

    # results
    print(f"\n-> Cash amount at risk per trade: ${car:,.2f}")
    print(f"-> Consecutive losses to wipe out your account: {int(lstba)}")

    input("\nPress Enter to return to the menu...")
#To be continued
