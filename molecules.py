from copy import copy
from database import ModelData
from random import randint
import numpy as np


class Molecule:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.name == other.name


class Polymer(Molecule):
    def __init__(self, name, sequence, mass_of_monomers):
        super().__init__(name)
        self.mass_of_monomers = mass_of_monomers
        self.sequence = ''
        self.bindings = []
        for monomer in sequence:
            self.add_monomer(monomer)

    def __eq__(self, other):
        return super().__eq__(other) and self.sequence == other.sequence

    def __len__(self):
        return len(self.sequence)

    def add_monomer(self, monomer):
        if monomer not in self.mass_of_monomers:
            raise ValueError('Invalid monomer {}'.format(monomer))
        self.sequence += monomer

    def calc_mass(self):
        return sum(self.mass_of_monomers[monomer] for monomer in self.sequence)


class Ribo(Molecule):
    pass


class Protein(Polymer):

    amino_acid_weights = ModelData.amino_acid_weights

    def __init__(self, name, sequence=''):
        super().__init__(name, sequence, self.amino_acid_weights)


class Polymerase(Molecule):
    pass
    



class DNA(Polymer):

    nucleic_acid_weights_DNA = ModelData.nucleic_acid_weights_DNA

    def __init__(self, name, sequence=''):

        self.sequence = sequence
        self.poly_pos = {}
        self.poly_status = {}
        #self.isgene = 


        super().__init__(name, self.sequence, self.nucleic_acid_weights_DNA)


    def bind_polymerase(self, poly):
        

        if sum(self.poly_pos) < poly:
            pos = randint(0,len(self.sequence) -1 )
            number = len(self.poly_pos) + 1
            
            self.poly_pos[number] = pos
            self.poly_status[number] = 0

    def move_polymerase(self):
        


        for entry in self.poly_pos: 
            if ModelData.is_gene[self.poly_pos[entry]] == 1:
                if ModelData.is_gene[self.poly_pos[entry]-1] == 0:
                    self.poly_status[entry] = 1
            else:
                if ModelData.is_gene[self.poly_pos[entry]-1] == 1:
                    self.poly_status[entry] = 0



        for entry in self.poly_pos: 
            if self.poly_pos[entry] + 1 >= len(self.sequence):
                self.poly_pos[entry] = 0
            else:
                self.poly_pos[entry] += 1


            





class MRNA(Polymer):

    nucleic_acid_weights = ModelData.nucleic_acid_weights

    def __init__(self, name, sequence=''):

        super().__init__(name, sequence, self.nucleic_acid_weights)


class MoleculeCollection:
    def __init__(self, molecule_type):
        self.molecule_type = molecule_type
        self.molecules = None

    def add(self, molecule):
        if not isinstance(molecule, self.molecule_type):
            raise ValueError('Expected object of type {}, received of type {}'
                             .format(self.molecule_type, type(molecule)))

    def take(self, name, number):
        pass

    def count(self, name):
        pass

    def populate(self, name, number):
        for _ in range(number):
            self.add(self.molecule_type(name))


class PopulationCollection(MoleculeCollection):
    def __init__(self, molecule_type):
        super().__init__(molecule_type)
        self.molecules = dict()

    def add(self, molecule):
        super().add(molecule)
        if molecule.name in self.molecules.keys():
            self.molecules[molecule.name] += 1
        else:
            self.molecules[molecule.name] = 1

    def take(self, name, number=1):
        assert self.molecules[name] >= number
        self.molecules[name] -= number

    def count(self, name=None):
        if name is None:
            return sum([self.molecules[name] for name in self.molecules])
        return self.molecules[name]


class ParticleCollection(MoleculeCollection):
    def __init__(self, molecule_type):
        super().__init__(molecule_type)
        self.molecules = dict()

    def add(self, molecule):
        super().add(molecule)
        if molecule.name in self.molecules.keys():
            self.molecules[molecule.name].append(copy(molecule))
        else:
            self.molecules[molecule.name] = [copy(molecule)]

    def take(self, name, number=1):
        result = []
        for _ in range(number):
            if len(self.molecules[name]) > 0:
                molecule = self.molecules[name].pop()
                result.append(molecule)

        assert number == len(result)

        return result

    def count(self, name=None):
        if name is None:
            return sum([len([x for x in self.molecules[molname]]) for molname in self.molecules])
        return len([x for x in self.molecules[name]])

    def get_molecules(self, name=None):
        if not name:
            return [molecule for molecules in self.molecules.values() for molecule in molecules]
        else:
            return self.molecules[name]
