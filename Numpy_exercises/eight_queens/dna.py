
import numpy as np
from numpy import random

class Dna:
    """
    The eight queens puzzle is the problem of plaching eight chess queens on an 8x8
    chessboard so that no two queens threaten each other; thus, a solution requires that
    no two queens share the same row
    """

    def __init__(self,mutation = 0.5,population = 5, genes = random.choice(np.arange(64),size=(8))):

        self.mutation = mutation
        self.population = population
        self.table = np.arange(64).reshape(8,8)
        self.genes = genes

    def randomic_population(self):
        """
        Returns an narray with random individuals
        according to the total number of the population
        """
        pop = []
        for i in range(self.population):
            pop.append(random.choice(np.arange(64), size =(8)))
        return np.vstack(pop)

    def fitness(self):
        """
        Function responsible
        for scoring +1 for each queen who can attack another
        """
        return 'fit'

    def cross_over(self, father, mother):
        """
        Function thar receives two individuals and returns an array with
        a randomic mixture of the parents' genes
        """
        return 'cross'





