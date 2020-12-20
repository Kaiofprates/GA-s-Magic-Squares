from dna import Dna
import numpy as np
from numpy import random

gene  = Dna(population=3000,mutation=0.4)

pop = gene.randomic_population()

generation = 1

def epoch(population):
    global generation
    print("=======================================")
    print("""------- Generation -------""" + str(generation))

    generation = generation + 1

    s = 0

    for i in range(len(population)):
        # Fit
        population[i].fitness()
        s = s + population[i].fit
        # mating Pool

    mean = s / gene.population
    print("-   mean error = {}".format(mean))
    print("========================================")
    matingPool = [gene]
    new_population = []

    for i in range(len(population)):
        p = population[i].fit
        n = (11 - population[i].fit) * 100
        if(n < 0):
            n = 2
        if(p == 1): n = 5000
        if(p == 2): n = 1000
        if(p == 3): n = 800

        for j in range(n):
            matingPool.append(population[i])

    for i in range(len(population)):
        father = matingPool[random.choice(len(matingPool) )]
        mother = matingPool[random.choice(len(matingPool) )]
        if(mean <= 7):
            gene.flag = True
        if(len(father.genes) == 8 and len(mother.genes) == 8):
            child = gene.cross_over(father.genes,mother.genes)
            child.fitness()
            #if (child.fit == 2): print(child.genes)
            #print('------ error {}'.format(child.fit))
            if child.fit == 0:
                print(child.genes)
                print("------Generation----{}".format(generation))
                return 0
            new_population.append(child)

    epoch(new_population)




def main():
    epoch(pop)


if __name__ == "__main__":
    main()