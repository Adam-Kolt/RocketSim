from RocketSimulation.dataClasses import RocketEndConditions, WorldData
from RocketSimulation.objects import Rocket
from RocketSimulation.simulation import Simulation, RocketSimulation

def main():
    newSim = RocketSimulation(Rocket(990, 100, 1, (0, 100), (0, -10)), WorldData(), RocketEndConditions(-50, 1000))
    Simulation.start(newSim)
    Simulation.display(newSim)


if __name__ == "__main__":
    main()
