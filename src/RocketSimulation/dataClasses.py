
from dataclasses import dataclass
from objects import Rocket

@dataclass
class WorldData:
    ''' Stores the information about the world of the simulation '''
    ''' Default values represent Earth '''
    gravity: float = 9.8
    atmosphericDensity: float = 1.2

@dataclass
class RocketEndConditions:
    ''' Stores the rocket end conditions for a given Simulation '''
    minHeight: float = None # End below certain height
    maxHeight: float = None # End above certain height
    minVel: float = None # End below certain velocity
    maxVel: float = None # End above certain velocity

    def evaluateCondition(self, rocket: Rocket):
        if rocket.y > self.maxHeight: return True
        elif rocket.y <  self.minHeight: return True
        if rocket.getVelocityM() > self.maxVel: return True
        elif rocket.getVelocityM() < self.minVel: return True
        
        # Did not meet any conditions (Does not terminate simulation)
        return False


