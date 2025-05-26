import numpy as np
import matplotlib.pyplot as plt
from typing import List

def simulate_card_draw() -> bool:
    """
    Simulates drawing cards from a standard deck and checks if the first 2 appears at position 14.
    Returns True if the condition is met, False otherwise.
    """
    # Create a deck with 4 of each value (1-13)
    deck = np.repeat(np.arange(1, 14), 4)
    # Shuffle the deck
    np.random.shuffle(deck)
    # Check if the first 2 appears at position 14 (index 13)
    return np.where(deck == 2)[0][0] == 13

def run_simulations(num_trials: int) -> List[float]:
    """
    Runs multiple simulations and tracks the running ratio of successful trials.
    
    Args:
        num_trials: Number of trials to run
        
    Returns:
        List of running ratios for each trial number
    """
    successes = 0
    ratios = []
    
    for i in range(1, num_trials + 1):
        if simulate_card_draw():
            successes += 1
        ratios.append(successes / i)
    
    return ratios

def plot_results(ratios: List[float], num_trials: int):
    """
    Plots the results of the simulation.
    
    Args:
        ratios: List of running ratios
        num_trials: Total number of trials
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_trials + 1), ratios, 'b-', label='Running ratio')
    plt.xlabel('Number of Trials')
    plt.ylabel('Ratio of Successful Trials')
    plt.title('Card Drawing Simulation Results')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    while True:
        try:
            num_trials = int(input("Enter the number of trials to run (or 0 to exit): "))
            if num_trials == 0:
                break
            if num_trials < 1:
                print("Please enter a positive number.")
                continue
                
            print(f"Running {num_trials} simulations...")
            ratios = run_simulations(num_trials)
            plot_results(ratios, num_trials)
            
            # Print final probability
            print(f"Final probability after {num_trials} trials: {ratios[-1]:.4f}")
            
        except ValueError:
            print("Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main() 