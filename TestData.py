# Test data
price = [100, 110, 120, 130, 140]
volume = [10, 20, 30, 40, 50]
balance = 1000
volatility_index = [0.1, 0.2, 0.3, 0.4, 0.5]

# Run the genetic algorithm
population_size = 10
num_to_select = 4
num_to_breed = 6
mutation_probability = 0.1
max_iterations = 100

best_chromosome = genetic_algorithm(population_size, num_to_select, num_to_breed, mutation_probability, max_iterations)
print(best_chromosome)
