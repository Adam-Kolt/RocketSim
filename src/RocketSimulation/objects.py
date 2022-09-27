class Rocket:
    ''' Rocket class to create simple object which holds all information about a Rocket '''
    def __init__(self, thrust, mass, position, startVelocity) -> None:
        self.x, self.y = position
        self.velocityX, self.velocityY = startVelocity
        self.thrust = thrust
        self.mass = mass        

    def update(self, timeElapsed):
        self.x += self.velocityX * timeElapsed
        self.y += self.velocityY * timeElapsed


        