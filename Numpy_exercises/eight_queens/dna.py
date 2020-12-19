
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
        self.fit  = 0

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
        for i in self.genes:
            self.table.reshape(64)[i] = -1

        for i in range(8):
            res = [n for n in self.table[i] if (n == -1 )]
            if len(res) >= 2:
                self.fit = self.fit + 1

            diagonal = [n for n in self.table.diagonal(i) if (n == -1)]
            if len(diagonal) >= 2:
                self.fit = self.fit + 1

            diagonalInversa = [n for n in np.fliplr(self.table).diagonal(i) if (n == -1)]
            if len(diagonalInversa) >= 2:
                self.fit = self.fit + 1

            axis1 =  [n for n in np.fliplr(self.table).diagonal(i,axis1=1,axis2=0) if (n == -1)]
            if len(axis1) >= 2:
                self.fit = self.fit + 1

            axis2 = [n for n in self.table.diagonal(i,axis1 = 1, axis2 = 0) if (n == -1)]
            if len(axis2) >= 2:
                self.fit = self.fit + 1

        return self.fit

    def cross_over(self, father, mother):
        """
        Function thar receives two individuals and returns an array with
        a randomic mixture of the parents' genes
        """
        return 'cross'





