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
