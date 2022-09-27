
from dataclasses import dataclass


@dataclass
class WorldData:
    ''' Stores the information about the world of the simulation '''
    ''' Default values represent Earth '''
    gravity: float = 9.8
    atmosphericDensity: float = 1.2

@dataclass
class RocketEndConditions:
    ''' Stores the rocket end conditions for a given Simulation '''
    minHeight: float = 0 # End below certain height
    maxHeight: float = 0 # End above certain height

    def evaluateCondition(self, rocket):
        if rocket.y > self.maxHeight: return True
        elif rocket.y <  self.minHeight: return True

        
        # Did not meet any conditions (Does not terminate simulation)
        return False


