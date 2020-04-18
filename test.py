import random

rand_set = []
for i in range(5):
    rand_set.append(random.random())
rand_set.sort()

print(rand_set)