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