import numpy as np
a = np.random.randn(10,20)
print(a)

b = np.random.randn(20,25)
print(b)
c=np.matmul(a, b)
print("mulpication",c)
print("sum is",np.sum(c))
