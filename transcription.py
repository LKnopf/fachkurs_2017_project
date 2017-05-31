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

    def update(self):
        """
        check for free polymerase
        """
        #self.model.states[Polymerase].molecules

        DNA_obj = self.model.states[DNA].get_molecules("DNA")[0]




        #DNA_obj.bind_polymerase(self.model.states[Polymerase].molecules["free Polymerase"])

        for i in range(1):   #500
            DNA_obj.bind_polymerase(self.model.states[Polymerase].molecules["free Polymerase"])
            pass



        for i in range(1):   #500
            DNA_obj.move_polymerase()
            



        #print(self.test.poly_status)
        #print(DNA_obj.poly_pos)
        













    