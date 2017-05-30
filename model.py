import database
from molecules import Ribo, Protein, MRNA, PopulationCollection, ParticleCollection, DNA, Polymerase
from translation import Translation
from transcription import Transcription
import processes


class SimulationResult:
    """
    handles and stores a simulation result for one species
    """

    def __init__(self, molecule_collection):
        """
        @param molecule_collection: MoleculeCollection
        """
        self.molecule_collection = molecule_collection
        self.trace = []
        self.time = []

    def add_timepoint(self, time):
        """
        record new time point
        @param time: float
        @return: None
        """
        self.trace.append(self.molecule_collection.count())
        self.time.append(time)


class Model:
    """
    Initializes the states and processes for the model and lets the processes update their corresponding states.
    """

    def __init__(self):
        # all selfs should be initialized in the constructor
        self.states = {}
        self.processes = {}
        self.timestep = 0
        self.db = database.ModelData()

        self._initialize_states()
        self._initialize_processes()

        # generate a SimulationResult class for each state
        self.results = {state: SimulationResult(self.states[state]) for state in self.states}

    def _initialize_states(self):
        self.states[Ribo] = PopulationCollection(Ribo)
        self.states[Ribo].populate("free ribos", 10)
        self.states[Polymerase] = PopulationCollection(Polymerase)
        self.states[Polymerase].populate("free Polymerase", 10)

        self.states[DNA] = ParticleCollection(DNA)
        self.states[DNA].add(DNA("DNA", "ATG"))


        self.states[MRNA] = ParticleCollection(MRNA)
        for name, sequence in self.db.get_states(MRNA):
            self.states[MRNA].add(MRNA(name, sequence))
        self.states[Protein] = ParticleCollection(Protein)

    def _initialize_processes(self):
        self.processes[Translation] = Translation("Translation", self)
        self.processes[Transcription] = Transcription("Transcription", self)

    def step(self):
        """
        Do one update step for each process and save the results.
        """
        for p in self.processes:
            self.processes[p].update()

        for state in self.states:
            self.results[state].add_timepoint(self.timestep)

        self.timestep += 1

    def simulate(self, steps, log=True):
        """
        Simulate the model for some time.
        @param steps: int
        @param log: Bool
        @return None
        """
        for s in range(steps):
            self.step()
            if log:  # This could be an entry point for further logging
                print('mRNAs', self.states[MRNA].count())
                print("Proteins", self.states[Protein].count())

if __name__ == "__main__":
    c = Model()
    c.simulate(50, log=False)

