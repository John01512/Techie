import numpy as np
import random

# Number of genes in each chromosome
genes = 2

# Number of chromosomes in the population
chromosomes = 10

# Size of the mating pool (number of parents selected for reproduction)
mating_pool_size = 6

# Number of offspring produced through crossover
offspring_size = chromosomes - mating_pool_size

# Lower and upper bounds for gene values
lb = -5
ub = 5

# Number of generations to run
generations = 3

# Function to calculate fitness of each chromosome in the population
def calculate_fitness(population):
    return np.sum(population ** 2, axis=1)

# Function to find the index of the fittest chromosome in the population
def find_fittest_index(fitness):
    return np.argmax(fitness)

# Main function to execute the genetic algorithm
def main():
    # Initialize the population with random values
    population = np.random.uniform(lb, ub, size=(chromosomes, genes))

    # Iterate through each generation
    for generation in range(generations):
        print("Generation:", generation + 1)

        # Calculate fitness for each chromosome in the population
        fitness = calculate_fitness(population)

        # Print population and fitness for this generation
        print("\nPopulation:")
        print(population)
        print("\nFitness calculation:")
        print(fitness)

        # Select parents for reproduction (mating pool)
        parents = np.zeros((mating_pool_size, genes))
        for p in range(mating_pool_size):
            fittest_index = find_fittest_index(fitness)
            parents[p] = population[fittest_index]
            fitness[fittest_index] = -1  # Marking as selected

        # Print selected parents
        print("\nParents:")
        print(parents)

        # Perform crossover (recombination) to create offspring
        offspring = np.zeros((offspring_size, genes))
        for k in range(offspring_size):
            crossover_point = random.randint(0, genes - 1)
            parent1_index = k % parents.shape[0]
            parent2_index = (k + 1) % parents.shape[0]
            offspring[k, :crossover_point] = parents[parent1_index, :crossover_point]
            offspring[k, crossover_point:] = parents[parent2_index, crossover_point:]

        # Print offspring after crossover
        print("\nOffspring after crossover:")
        print(offspring)

        # Apply mutation to introduce genetic diversity in offspring
        for child in offspring:
            random_index = random.randint(0, genes - 1)
            random_value = random.uniform(lb, ub)
            child[random_index] += random_value

        # Print offspring after mutation
        print("\nOffspring after Mutation:")
        print(offspring)

        # Replace least fit individuals in the population with offspring
        population[:mating_pool_size] = parents
        population[mating_pool_size:] = offspring

        # Print new population for the next generation
        print("\nNew Population for next generation:")
        print(population)

    # Calculate final fitness for the last population
    final_fitness = calculate_fitness(population)
    # Find the index of the fittest individual
    fittest_index = find_fittest_index(final_fitness)
    # Get the fittest individual and its fitness
    fittest_ind = population[fittest_index]
    best_fitness = final_fitness[fittest_index]

    # Print the fittest individual and its fitness
    print("\nBest Individual:")
    print(fittest_ind)
    print("\nBest Individual's Fitness:")
    print(best_fitness)

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()