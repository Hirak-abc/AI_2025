import random
import pandas as pd

# Initialize counters for each combination
counts = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}

# Number of simulations
num_trials = 1000

# Probabilities
p_a = 0.5
p_b = 0.4

# Store results for making a table
results = []

for _ in range(num_trials):
    # Generate random numbers
    rand_a = random.random()
    rand_b = random.random()
    
    # Determine A and B based on thresholds
    A = 1 if rand_a >= (1 - p_a) else 0
    B = 1 if rand_b >= (1 - p_b) else 0
    
    results.append((A, B))
    
    # Increment the counter for this combination
    counts[(A, B)] += 1

# Create a DataFrame for the results
df = pd.DataFrame(results, columns=['A', 'B'])

# Display the table of counts
count_table = pd.DataFrame.from_dict(counts, orient='index', columns=['Count'])
count_table['Probability'] = count_table['Count'] / num_trials
print("Counts and Probability Table:")
print(count_table)

# Show convergence to theoretical probabilities
# For independent events, P(A=1,B=1) = 0.5 * 0.4 = 0.2, etc.
theoretical_probs = {
    (0, 0): (1 - p_a) * (1 - p_b),
    (0, 1): (1 - p_a) * p_b,
    (1, 0): p_a * (1 - p_b),
    (1, 1): p_a * p_b
}

print("\nTheoretical Probabilities:")
for key, val in theoretical_probs.items():
    print(f"P{key} = {val:.2f}")
