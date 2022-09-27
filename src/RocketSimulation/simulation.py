from RocketSimulation.dataClasses import RocketEndConditions, WorldData

import time
import matplotlib.pyplot as plt

class RocketSimulation:
    def __init__(self, rocket, world: WorldData, end_conditions: RocketEndConditions) -> None:
        self.Rocket = rocket
        self.World = world
        self.EndConditions = end_conditions
        self.RocketPositionHistory = []
        self.timeIncrements = 0.1

    def simulate(self, oldTime):
        while True:
            nowTime = oldTime+self.timeIncrements
            self.Rocket.update(nowTime-oldTime, self.World)
            self.RocketPositionHistory.append((nowTime, self.Rocket.x, self.Rocket.y))
            if self.EndConditions.evaluateCondition(self.Rocket) or len(self.RocketPositionHistory) > 100000: break
            oldTime = nowTime
        

class Simulation:
    @staticmethod
    def start(rocketSim: RocketSimulation):
        rocketSim.simulate(time.perf_counter())

    def display(rocketSim: RocketSimulation):
        timesList = []
        heightList = []

        for point in rocketSim.RocketPositionHistory:
            timesList.append(point[0])
            heightList.append(point[2])
        plt.plot(timesList, heightList)
        plt.show()

        