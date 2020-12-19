from dna import Dna
import numpy as np

rangeGene  = np.arange(8)
gene = Dna(mutation=0.05)
gene.fitness()
print(gene.table)
print(gene.fit)

print(gene.cross_over( np.arange(8), gene.genes ))
#pop = gene.randomic_population()
