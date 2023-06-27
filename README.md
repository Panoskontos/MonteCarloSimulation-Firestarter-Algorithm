# MonteCarloSimulation-Firestarter-Algorithm



Title: Parallel Forest Fire Spread Simulation

Project Summary:
The project aims to implement a parallel algorithm using the POSIX Threads programming model to simulate the spread of a forest fire. The goal is to explore basic parallel algorithmic techniques and their application in shared memory systems.

Description:
The project focuses on computational modeling, specifically the simulation of forest fire spread using software. A simplified model is used to understand the process without the limitations, costs, and risks associated with real-world experiments. The model belongs to the Monte Carlo simulation category, utilizing probabilities and pseudo-random numbers.

The forest is represented as a two-dimensional array, and the simulation involves iteratively increasing fire spread probabilities. Multiple simulations are run for each probability, and the average percentage of the burned forest is calculated. The provided pseudocode outlines the simulation process.

Project Objectives:

Implement two parallel versions of the algorithm using POSIX Threads.
Version 1: Parallelize the outer loop with static workload assignment, expecting potential performance limitations due to varying simulation times.
Version 2: Parallelize the outer loop with dynamic workload assignment to overcome potential performance limitations.
Instructions:

Note: The project involves comparing the performance of the two parallel implementations by varying the forest size and the number of threads.


Results (in seconds)

![results](https://github.com/Panoskontos/MonteCarloSimulation-Firestarter-Algorithm/assets/65974766/9ea790d7-1b49-4418-94ed-7a10bc4a0641)


Youtube Video on: https://www.youtube.com/watch?v=bzJVH8c63GA&ab_channel=PanosKontos 
