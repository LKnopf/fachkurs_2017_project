import processes
import random
import database
from molecules import Ribo, Protein, MRNA, PopulationCollection, ParticleCollection, DNA, Polymerase
from database import ModelData

class Transcription(processes.Process):
    #The Transcription process
    def __init__(self, name, model):
        
        # call the constructor of the base class (processes.Process in this case)
        super().__init__(name, model)

        self.test = (DNA("DNA", self.model.db.genome))

    def update(self):
        """
        check for free polymerase
        """
        #self.model.states[Polymerase].molecules

        s = self.model.states[DNA].get_molecules("DNA")


        #s = self.model.states[DNA].molecules["DNA"]


        print(s[0].sequence[1])



        self.test.bind_polymerase(self.model.states[Polymerase].molecules["free Polymerase"])
        self.test.move_polymerase()

        #print(self.test.poly_status)
        #print(self.test.poly_pos)
        













    