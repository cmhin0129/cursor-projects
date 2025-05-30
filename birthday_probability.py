import numpy as np
import matplotlib.pyplot as plt

def birthday_probability(n):
    if n <= 1:
        return 0
    probability = 1
    for k in range(1, n):
        probability *= (1 - k/365)
    return 1 - probability

# Generate x values from 1 to 100
x = np.arange(1, 101)
# Calculate probabilities for each n
y = [birthday_probability(n) for n in x]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', label='Birthday Probability')

# Highlight p(23)
p_23 = birthday_probability(23)
plt.plot(23, p_23, 'ro', label=f'p(23) = {p_23:.4f}')

# Add labels and title
plt.xlabel('Number of People (n)')
plt.ylabel('Probability p(n)')
plt.title('Birthday Paradox Probability')
plt.grid(True, alpha=0.3)
plt.legend()

# Add text annotation for p(23) with an arrow
plt.annotate(f'p(23) = {p_23:.4f}',
             xy=(23, p_23),
             xytext=(30, p_23-0.1),
             arrowprops=dict(facecolor='black', 
                           shrink=0.05, 
                           width=0.5, 
                           headwidth=3, 
                           headlength=4))

plt.show() 