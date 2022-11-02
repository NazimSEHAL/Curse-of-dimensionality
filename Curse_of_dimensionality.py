import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.function_base import average

D = []

# Choosing the numbers n, d, m, p.
n = int(input('the number of vectors n = '))
d = int(input('the number of dimensions d = '))
m = int(input('the number of vectors m = '))
P = int(input('quantization step p = '))

# Generating n vector of dimension d randomly and uniformly distributed which will be stored in the vector N.
N = np.random.rand(n,d)

# Selecting m vectors from the vectors N.
random_indices = np.random.choice(n, size=m, replace=False)
M = N[random_indices, :]

# View the contents of N and M.
print(N)
print(M)

# Calculate the Euclidean distance between each vector of M and each vector of N and save the values ​​in vector D.
for i in M:
    for j in N:
        D.append(np.linalg.norm(i - j))

        # Eliminer les valeurs nulls.
        for k in D:
             if k == 0:
                 D.remove(k)

# Eliminate repetitive values ​​of D.
D = list(set(D))

# View the contents of D
print(D)

# We are looking for the size of D to check if it verifies the law demonstrated in the report.
print("le nombre de distances calculer est ",len(D))

# Calculation and display of the average distances.
Average = average(D)
print("The average is ",Average)

# Calculating the standard_deviation
standard_deviation = np.std(D)
print('The standard_deviation is ',standard_deviation)

# Histogramme
plt.hist(D, P, facecolor='b', align='mid')
#plt.hist(D)
plt.title(f'n = {n}, d = {d}, m = {m}')
plt.xlabel('distances')
plt.ylabel('number')
plt.show()


# Generate a graph that clearly demonstrates the dimension curse phenomenon
x = range(len(D))
plt.stem(x, D)
plt.title(f'n = {n}, d = {d}, m = {m}')
plt.xlabel('index')
plt.ylabel('distance')
plt.show()

plt.stem(D, markerfmt=' ')
plt.title(f'n = {n}, d = {d}, m = {m}')
plt.xlabel('index')
plt.ylabel('distance')
plt.show()


