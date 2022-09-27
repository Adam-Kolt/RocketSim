from RocketSimulation.dataClasses import RocketEndConditions, WorldData
from objects import Rocket
import time
import matplotlib.pyplot as plt

class RocketSimulation:
    def __init__(self, rocket: Rocket, world: WorldData, end_conditions: RocketEndConditions) -> None:
        self.Rocket = rocket
        self.World = world
        self.EndConditions = end_conditions
        self.RocketPositionHistory = []

    def simulate(self, time, rocket):
        nowTime = time.perf_counter()
        rocket.update(nowTime-time)
        self.RocketPositionHistory.append((nowTime, rocket.x, rocket.y))
        if self.EndConditions.evaluateCondition(rocket): return
        self.simulate(nowTime, rocket)

class Simulation:
    @staticmethod
    def start(rocketSim: RocketSimulation):
        rocketSim.simulate(time.perf_counter(), rocketSim.Rocket)

    def display(rocketSim: RocketSimulation):
        timesList = []
        heightList = []

        for point in rocketSim.RocketPositionHistory:
            timesList.append(point[0])
            heightList.append(point[2])
        plt.plot(timesList, heightList)

        