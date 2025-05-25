import random

def simulate_dice_rolls(num_rolls):
    # Check if input is a positive integer
    if not isinstance(num_rolls, int) or num_rolls <= 0:
        return "Error: Please enter a positive integer."
    
    # Initialize a dictionary to store frequencies
    frequencies = {i: 0 for i in range(1, 7)}
    
    # Simulate dice rolls
    for _ in range(num_rolls):
        roll = random.randint(1, 6)
        frequencies[roll] += 1
    
    # Format and return results
    result = f"\nResults of {num_rolls} dice rolls:\n"
    for number, count in frequencies.items():
        percentage = (count / num_rolls) * 100
        result += f"Number {number}: {count} times ({percentage:.2f}%)\n"
    
    return result

def main():
    try:
        # Get input from user
        rolls = input("Enter the number of times to roll the dice: ")
        rolls = int(rolls)
        
        # Run simulation and print results
        print(simulate_dice_rolls(rolls))
        
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main() 