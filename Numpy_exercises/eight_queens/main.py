from dna import Dna
import numpy as np
from numpy import random

gene  = Dna(population=100,mutation=0.05)

population  = gene.randomic_population()


def epoch():

    for i in range(len(population)):
        # Fit
        population[i].fitness()
        # mating Pool

    matingPool = []

    for i in range(len(population)):
        n = population[i].fit * 100

        for j in range(n):
            matingPool.append(population[i])
            father = matingPool[random.choice(len(matingPool) )]
            mother = matingPool[random.choice(len(matingPool) )]

            child = gene.cross_over(father.genes,mother.genes)
            child.fitness()
            print(child.fit)

def main():
    epoch()


if __name__ == "__main__":
    main()