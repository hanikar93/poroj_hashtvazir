python
import random

# تعداد وزرا
N = 8

# تابع برای ایجاد یک جمعیت اولیه
def create_population(size):
    population = []
    for _ in range(size):
        individual = list(range(N))
        random.shuffle(individual)
        population.append(individual)
    return population
# تابع برای محاسبه هزینه (تعداد برخوردها)
def fitness(individual):
    clashes = 0
    for i in range(N):
        for j in range(i + 1, N):
            if individual[i] == individual[j] or abs(individual[i] - individual[j]) == abs(i - j):
                clashes += 1
    return clashes

# تابع برای انتخاب والدین
def select_parents(population):
    weights = [1 / (1 + fitness(ind)) for ind in population]
    return random.choices(population, weights=weights, k=2)


# تابع برای ترکیب والدین
def crossover(parent1, parent2):
    point = random.randint(1, N-1)
    child1 = parent1[:point] + [gene for gene in parent2 if gene not in parent1[:point]]
    child2 = parent2[:point] + [gene for gene in parent1 if gene not in parent2[:point]]
    return child1, child2
