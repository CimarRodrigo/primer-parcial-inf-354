import array
import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator
toolbox.register("attr_bool", random.randint, 0, 1)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 4)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def MyCxTwoPoint(ind1, ind2):
    mitad = len(ind1) // 2 
    ind1[mitad:], ind2[mitad:] = ind2[mitad:], ind1[mitad:]
    return ind1, ind2

def MyMutFlipBit(individual, indpb):
    if(individual[len(individual)-2] == 0):
        individual[len(individual)-2] = 1
    else:
        individual[len(individual)-2] = 0

    return individual,

def evalFunction(individual):
    numero_entero = int("".join(str(x) for x in individual), 2)
    return numero_entero**(2*numero_entero) - 1,

toolbox.register("evaluate", evalFunction)
toolbox.register("mate", MyCxTwoPoint)
toolbox.register("mutate", MyMutFlipBit, indpb=1)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)

    pop = toolbox.population(n=12)
    print(pop)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=1, ngen=3, 
                                   stats=stats, halloffame=hof, verbose=False)

    return pop, log, hof

if __name__ == "__main__":
    pop, log, hof = main()
    print(log)
