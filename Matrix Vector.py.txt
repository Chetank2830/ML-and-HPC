import random 
import numpy as np
import time
M = 700
A = np.random.randint(0, M, size=(M, M))
a = np.random.randint(0, M, size=M)
d = np.zeros(M, dtype=int)
start = time.time()
for i in range(M):
    sum = 0
    for j in range(M):
        sum += A[i][j] * a[j]
    d[i] = sum
duration = time.time() - start
print("Serial Multiply Vector and matrix:", duration)
start = time.time()
d = np.dot(A, a)
duration = time.time() - start
print("Parallel Multiply Vector and matrix:", duration)
N = 10000000
a = [random.randint(0, N) for _ in range(N)]
b = [random.randint(0, N) for _ in range(N)]
c = np.zeros(N, dtype=int)
start = time.time()
for i in range(N):
    c[i] = b[i] + a[i]
duration = time.time() - start
print("Serial vector addition:", duration)
start = time.time()
c = np.add(a, b)
duration = time.time() - start
print("Parallel vector addition:", duration)

print("*************")

