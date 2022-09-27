import math, random


class Rocket:
    ''' Rocket class to create simple object which holds all information about a Rocket '''
    def __init__(self, thrust, mass, radius, position, startVelocity) -> None:
        self.x, self.y = position
        self.velocityX, self.velocityY = startVelocity
        self.thrust = thrust
        self.mass = mass        
        self.radius = radius

    def update(self, timeElapsed, world):
        self.velocityY += (self.thrust/self.mass)*timeElapsed
        dragY = 0.5*world.atmosphericDensity*(self.velocityY**2)*0.75*(math.pi*(self.radius**2))
        gravity = world.gravity
        self.velocityY -= (gravity)*timeElapsed
        self.velocityY -= (abs(self.velocityY)/self.velocityY)*(dragY/self.mass)*timeElapsed
        self.x += self.velocityX * timeElapsed
        self.y += self.velocityY * timeElapsed


    def getVelocityM(self):
        return abs(self.velocityX)+abs(self.velocityY)


        