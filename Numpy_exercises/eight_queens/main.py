from dna import Dna
import numpy as np
from numpy import random

gene  = Dna(population=200,mutation=0.05)

pop = gene.randomic_population()

generation = 1

def epoch(population):
    global generation
    print("""------- Generation -------""" + str(generation))
    generation = generation + 1
    for i in range(len(population)):
        # Fit
        population[i].fitness()
        # mating Pool

    matingPool = [gene]
    new_population = []

    for i in range(len(population)):
        n = population[i].fit * 100
        for j in range(n):
            matingPool.append(population[i])

    for i in range(len(population)):
        father = matingPool[random.choice(len(matingPool) )]
        mother = matingPool[random.choice(len(matingPool) )]
        if(len(father.genes) == 8 and len(mother.genes) == 8):
            child = gene.cross_over(father.genes,mother.genes)
            child.fitness()
            print('------ error {}'.format(child.fit))
            if child.fit == 0:
                print(child.genes)
                return 0
            new_population.append(child)

    epoch(new_population)




def main():
    epoch(pop)


if __name__ == "__main__":
    main()