import random
def simulation(p, rounds):
    win = 0
    sim = p / 100
    for _ in range(rounds):
        x = random.random()
        if x <= sim:
            win += 1
    print(f"You won {win} times!")

if __name__ == "__simulation__":
    simulation(0,0)