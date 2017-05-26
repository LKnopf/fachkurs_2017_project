import processes
import random
import database
from molecules import Ribo, Protein, MRNA, PopulationCollection, ParticleCollection, DNA, Polymerase


class Transcription(processes.Process):
    #The Transcription process
    def __init__(self, name, model):
        # call the constructor of the base class (processes.Process in this case)
        super().__init__(name, model)

    def update(self):
        """
        check for free polymerase
        """
        print(self.model.states[Polymerase].molecules)

    