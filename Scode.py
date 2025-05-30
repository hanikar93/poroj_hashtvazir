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

# تابع برای جهش
def mutate(individual):
    idx1, idx2 = random.sample(range(N), 2)
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    
    # تابع اصلی الگوریتم ژنتیک
def genetic_algorithm(pop_size, generations):
    population = create_population(pop_size)
    for generation in range(generations):
        population = sorted(population, key=fitness)
        if fitness(population[0]) == 0:
            print(f'Solution found in generation {generation}: {population[0]}')
            return population[0]
        new_population = population[:2]  # والدین را نگه می‌داریم
        while len(new_population) < pop_size:
            parent1, parent2 = select_parents(population)
            child1, child2 = crossover(parent1, parent2)
            if random.random() < 0.1:  # احتمال جهش
                mutate(child1)
            if random.random() < 0.1:  # احتمال جهش
                mutate(child2)
            new_population.extend([child1, child2])
        population = new_population
    print('No solution found')
    return None

# اجرای الگوریتم
genetic_algorithm(pop_size=100, generations=1000)


