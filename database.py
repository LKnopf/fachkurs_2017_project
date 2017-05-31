import random as rnd
import string
import pandas as pd
import numpy as np

class ModelData:
    """
    class to process data sources for usage in the model
    """

    codon_to_amino_acid = dict([('UCA', 'S'), ('UCG', 'S'), ('UCC', 'S'), ('UCU', 'S'),
                                ('UUU', 'F'), ('UUC', 'F'), ('UUA', 'L'), ('UUG', 'L'),
                                ('UAU', 'Y'), ('UAC', 'Y'), ('UAA', '*'), ('UAG', '*'),
                                ('UGU', 'C'), ('UGC', 'C'), ('UGA', '*'), ('UGG', 'W'),
                                ('CUA', 'L'), ('CUG', 'L'), ('CUC', 'L'), ('CUU', 'L'),
                                ('CCA', 'P'), ('CCG', 'P'), ('CCC', 'P'), ('CCU', 'P'),
                                ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'),
                                ('CGA', 'R'), ('CGG', 'R'), ('CGC', 'R'), ('CGU', 'R'),
                                ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'),
                                ('ACA', 'T'), ('ACG', 'T'), ('ACC', 'T'), ('ACU', 'T'),
                                ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'),
                                ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'),
                                ('GUA', 'V'), ('GUG', 'V'), ('GUC', 'V'), ('GUU', 'V'),
                                ('GCA', 'A'), ('GCG', 'A'), ('GCC', 'A'), ('GCU', 'A'),
                                ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
                                ('GGA', 'G'), ('GGG', 'G'), ('GGC', 'G'), ('GGU', 'G')])

    amino_acid_weights = {'A': 89.0929, 'R': 175.208, 'N': 132.118, 'D': 132.094, 'C': 121.158, 'Q': 146.144,
                          'E': 146.121, 'G': 75.0664, 'H': 155.154, 'I': 131.172, 'L': 131.172, 'K': 147.195,
                          'M': 149.211, 'F': 165.189, 'P': 115.13,  'S': 105.092, 'T': 119.119, 'W': 204.225,
                          'Y': 181.188, 'V': 117.146}

    nucleic_acid_weights = {'A': 1.0, 'U': 2.2, 'G': 2.1, 'C': 1.3}
    nucleic_acid_weights_DNA = {'A': 1.0, 'T': 2.2, 'G': 2.1, 'C': 1.3}

    genes = pd.read_csv('ProteinTable167_161521.txt',  sep='\t')



    #genome = "ATGACTGCCATGACTGTTATGACTGAAATGACTGATGACTGCCATGACTGTTATGACTGAAATGACTGATGACTGCCATGACTGTTATGACTGAAATGACTG"
    #is_gene = np.zeros(len(genome))
    #is_gene[10:20] = 1


    with open('genome.txt', 'r') as f:
        genome = f.read()
        genome = genome.replace('\n','')


    is_gene = np.zeros(len(genome))

    count_ATG = 0
    count_div3 = 0

    for i in range(len(genes)):
        start = genes.loc[i,"Start"]
        stop = genes.loc[i,"Stop"]
        size = stop - start

        #if (genome[start-1:start+2]) == "ATG" or "GTG" or "TTG": count_ATG += 1
        #if (stop-start+1)%3 <= 0.001: count_div3 += 1


        for j in np.arange(start,stop,1):
            is_gene[j] = 1

    """
    def gaussian(x, mu, sig):
        return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))


    poly_bind_chance = np.zeros(len(genome))
    genome_pos = range(len(genome))

    #for i in genes.loc[:,"Start"]:
        print(i)
        poly_bind_chance += gaussian(genome_pos, i, 300)

    poly_bind_chance = poly_bind_chance / sum(poly_bind_chance)
    """








    def __init__(self):
        pass

    def get_states(self, molecule_class):
        """
        retrieves the information required to construct the different model molecules
        @param molecule_class: BioMolecule class
        @return: list
        """

        if str(molecule_class) == "<class 'molecules.MRNA'>":
            alphabet = list(self.codon_to_amino_acid.keys())
            mrnas = []
            genes = {}
            for _ in range(10):
                sequence = ''.join([rnd.choice(alphabet) for _ in range(rnd.randint(50, 500))])
                genes[''.join([rnd.choice(string.ascii_uppercase) for _ in range(3)])] = sequence

            for gene in genes:
                for i in range(rnd.randint(1, 10)):
                    mrnas.append((gene, genes[gene]))
            return mrnas
