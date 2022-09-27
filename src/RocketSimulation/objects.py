class Rocket:
    ''' Rocket class to create simple object which holds all information about a Rocket '''
    def __init__(self, thrust, mass, position) -> None:
        self.x, self.y = position
        self.thrust = thrust
        self.mass = mass        

        
        