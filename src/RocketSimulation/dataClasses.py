
from dataclasses import dataclass

@dataclass
class WorldData:
    ''' Stores the information about the world of the simulation '''
    ''' Default values represent Earth '''
    gravity: float = 9.8
    atmosphericDensity: float = 1.2
