import numpy as np
import random

genes = 2
chromosomes = 10
mating_pool_size = 6
offspring_size = chromosomes - mating_pool_size
lb = -5
ub = 5
generations = 3

def calculate_fitness(population):
    return np.sum(population ** 2, axis=1)

def find_fittest_index(fitness):
    return np.argmax(fitness)

def main():
    population = np.random.uniform(lb, ub, size=(chromosomes, genes))

    for generation in range(generations):
        print("Generation:", generation + 1)

        fitness = calculate_fitness(population)
        print("\nPopulation:")
        print(population)
        print("\nFitness calculation:")
        print(fitness)

        parents = np.zeros((mating_pool_size, genes))
        for p in range(mating_pool_size):
            fittest_index = find_fittest_index(fitness)
            parents[p] = population[fittest_index]
            fitness[fittest_index] = -1  # Marking as selected

        print("\nParents:")
        print(parents)

        offspring = np.zeros((offspring_size, genes))
        for k in range(offspring_size):
            crossover_point = random.randint(0, genes - 1)
            parent1_index = k % parents.shape[0]
            parent2_index = (k + 1) % parents.shape[0]
            offspring[k, :crossover_point] = parents[parent1_index, :crossover_point]
            offspring[k, crossover_point:] = parents[parent2_index, crossover_point:]

        print("\nOffspring after crossover:")
        print(offspring)

        for child in offspring:
            random_index = random.randint(0, genes - 1)
            random_value = random.uniform(lb, ub)
            child[random_index] += random_value

        print("\nOffspring after Mutation:")
        print(offspring)

        # Merge parents and offspring into new population
        population[:mating_pool_size] = parents
        population[mating_pool_size:] = offspring

        print("\nNew Population for next generation:")
        print(population)

    final_fitness = calculate_fitness(population)
    fittest_index = find_fittest_index(final_fitness)
    fittest_ind = population[fittest_index]
    best_fitness = final_fitness[fittest_index]

    print("\nBest Individual:")
    print(fittest_ind)

    print("\nBest Individual's Fitness:")
    print(best_fitness)

if __name__ == "__main__":
    main()
