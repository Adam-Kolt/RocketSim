from RocketSimulation.dataClasses import RocketEndConditions, WorldData
from RocketSimulation.objects import Rocket
from RocketSimulation.simulation import Simulation, RocketSimulation

def main():
    newSim = RocketSimulation(Rocket(1000, 100, (0, 0), (0, 10)), WorldData(), RocketEndConditions(-100, 100))
    Simulation.start(newSim)
    Simulation.display(newSim)


if __name__ == "__main__":
    main()
