import random
import numpy as np

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return self.name

def time_dependent_travel_time(city1, city2, departure_time):
    """Simulates time-dependent travel time (very simplified)."""
    distance = np.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)
    # Simulate rush hour (7-9 AM and 4-6 PM) - increase travel time
    if 7 <= departure_time <= 9 or 16 <= departure_time <= 18:
        return distance * 1.5  # 50% slower
    else:
        return distance

def calculate_route_cost(route, start_time=0):
    """Calculates the total travel time for a route, considering time-dependency."""
    total_time = 0
    current_time = start_time
    for i in range(len(route) - 1):
        travel_time = time_dependent_travel_time(route[i], route[i+1], current_time)
        current_time += travel_time
        total_time += travel_time
    return total_time

def create_initial_population(cities, population_size):
    """Creates an initial population of random routes."""
    population = []
    for _ in range(population_size):
        route = cities[:]  # Create a copy
        random.shuffle(route)
        population.append(route)
    return population

def calculate_fitness(route):
    """Calculates the fitness of a route (lower travel time is better)."""
    return 1 / calculate_route_cost(route) # Inverse of cost

def select_parents(population, fitness_values):
    """Selects two parents using tournament selection."""
    tournament_size = 5
    tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
    winner1 = max(tournament, key=lambda item: item[1])[0]
    tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
    winner2 = max(tournament, key=lambda item: item[1])[0]
    return winner1, winner2

def crossover(parent1, parent2):
     """Performs ordered crossover."""
     size = len(parent1)
     start, end = sorted(random.sample(range(size), 2))
     child1 = [None] * size
     child2 = [None] * size

     # Copy a segment from parent1 to child1
     child1[start:end] = parent1[start:end]
     # Fill the remaining positions in child1 with genes from parent2 (in order)
     current_index = end % size
     for gene in parent2:
         if gene not in child1:
             child1[current_index] = gene
             current_index = (current_index + 1) % size

     # Copy a segment from parent2 to child2
     child2[start:end] = parent2[start:end]
      # Fill the remaining positions in child2 with genes from parent1 (in order)
     current_index = end % size
     for gene in parent1:
        if gene not in child2:
            child2[current_index] = gene
            current_index = (current_index+1)%size

     return child1, child2


def mutate(route, mutation_rate=0.01):
    """Performs swap mutation."""
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(route)), 2)
        route[idx1], route[idx2] = route[idx2], route[idx1]
    return route


def genetic_algorithm(cities, population_size=100, generations=500):
    """Runs a simple genetic algorithm."""
    population = create_initial_population(cities, population_size)

    for generation in range(generations):
        fitness_values = [calculate_fitness(route) for route in population]

        new_population = []
        for _ in range(population_size // 2):  # Integer division
            parent1, parent2 = select_parents(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        population = new_population

        best_route = min(population, key=calculate_route_cost)
        best_cost = calculate_route_cost(best_route)
        print(f"Generation {generation+1}: Best Cost = {best_cost:.2f}")


    return best_route, best_cost


# Example Usage (Simplified Scenario)
cities = [
    City("A", 0, 0),
    City("B", 1, 5),
    City("C", 5, 3),
    City("D", 8, 1),
    City("E", 3, 7)
]


best_route, best_cost = genetic_algorithm(cities)

print(f"\nBest Route Found: {best_route}")
print(f"Best Route Cost: {best_cost:.2f}")
