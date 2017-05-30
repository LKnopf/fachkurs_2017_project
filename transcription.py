import processes
import random
import database
from molecules import Ribo, Protein, MRNA, PopulationCollection, ParticleCollection, DNA, Polymerase


class Transcription(processes.Process):
    #The Transcription process
    def __init__(self, name, model):
        self.test = (DNA("DNA", "ATGCTGATGAC"))
        # call the constructor of the base class (processes.Process in this case)
        super().__init__(name, model)

    def update(self):
        """
        check for free polymerase
        """
        #self.model.states[Polymerase].molecules

        s = self.model.states[DNA].get_molecules("DNA")
        s = self.model.states[DNA].molecules["DNA"]
        #print(s)
        self.test.bind_polymerase(len(self.model.states[Polymerase].molecules))
        print(self.test.poly_pos)








    