import processes
import random
import database
from molecules import Ribo, Protein, MRNA, PopulationCollection, ParticleCollection, DNA, Polymerase


class Transcription(processes.Process):

	def __init__(self, name, model):
        # call the constructor of the base class (processes.Process in this case)
        super().__init__(name, model)

    
	def update(self):
   
       	pass
    