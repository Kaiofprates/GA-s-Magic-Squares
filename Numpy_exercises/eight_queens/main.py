from dna import Dna
import numpy as np

rangeGene  = np.arange(8)
gene = Dna()
gene.fitness()
print(gene.table)
print(gene.fit)
#pop = gene.randomic_population()
