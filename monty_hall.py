import random
from typing import Tuple, List
import sys

def setup_game() -> List[str]:
    """Set up the initial game state with one car and two goats."""
    doors = ['goat', 'goat', 'car']
    random.shuffle(doors)
    return doors

def host_opens_door(doors: List[str], player_choice: int) -> int:
    """Host opens a door with a goat, different from the player's choice."""
    possible_doors = [i for i in range(3) 
                     if i != player_choice and doors[i] == 'goat']
    return random.choice(possible_doors)

def play_interactive_game():
    """Run an interactive version of the Monty Hall game."""
    print("\nWelcome to the Monty Hall Game!")
    print("Behind two doors are goats, and behind one door is a car.")
    
    # Initial setup
    doors = setup_game()
    
    # Player's first choice
    while True:
        try:
            choice = int(input("\nChoose a door (1, 2, or 3): ")) - 1
            if 0 <= choice <= 2:
                break
            print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Host opens a door
    opened_door = host_opens_door(doors, choice)
    print(f"\nI'll open door {opened_door + 1}, which has a goat.")
    
    # Player's final decision
    while True:
        switch = input("\nWould you like to switch doors? (yes/no): ").lower()
        if switch in ['yes', 'no']:
            break
        print("Please answer 'yes' or 'no'.")
    
    # Calculate final choice and result
    if switch == 'yes':
        final_choice = [i for i in range(3) 
                       if i != choice and i != opened_door][0]
        print(f"\nYou switched to door {final_choice + 1}.")
    else:
        final_choice = choice
        print("\nYou stayed with your original choice.")
    
    # Reveal result
    print(f"\nYou got a {doors[final_choice]}!")
    print("\nFinal door contents:")
    for i, item in enumerate(doors):
        print(f"Door {i + 1}: {item}")

def run_simulation(trials: int, initial_choice: int) -> Tuple[float, float]:
    """Run multiple trials and return win probabilities for stay/switch strategies."""
    stay_wins = 0
    switch_wins = 0
    
    for _ in range(trials):
        doors = setup_game()
        opened_door = host_opens_door(doors, initial_choice)
        switch_choice = [i for i in range(3) 
                        if i != initial_choice and i != opened_door][0]
        
        # Count wins for both strategies
        if doors[initial_choice] == 'car':
            stay_wins += 1
        if doors[switch_choice] == 'car':
            switch_wins += 1
    
    return (stay_wins / trials, switch_wins / trials)

def main():
    print("Welcome to the Monty Hall Problem Simulator!")
    print("\nChoose a mode:")
    print("1. Interactive Game")
    print("2. Simulation Mode")
    
    while True:
        try:
            mode = int(input("\nEnter mode (1 or 2): "))
            if mode in [1, 2]:
                break
            print("Please enter 1 or 2.")
        except ValueError:
            print("Please enter a valid number.")
    
    if mode == 1:
        play_interactive_game()
    else:
        # Get simulation parameters
        while True:
            try:
                trials = int(input("\nEnter number of trials: "))
                if trials > 0:
                    break
                print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
        
        while True:
            try:
                door = int(input("Enter your initial door choice (1, 2, or 3): ")) - 1
                if 0 <= door <= 2:
                    break
                print("Please enter 1, 2, or 3.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Run simulation and display results
        stay_prob, switch_prob = run_simulation(trials, door)
        print(f"\nResults after {trials} trials:")
        print(f"Probability of winning if you stay: {stay_prob:.2%}")
        print(f"Probability of winning if you switch: {switch_prob:.2%}")

if __name__ == "__main__":
    main() 