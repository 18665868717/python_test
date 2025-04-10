import numpy as np
data={"i" : np.random.rand()}
data_1={o: np.random.rand() for o in range(5)}
print(data_1)
print(np.random.random(10))
print(np.random.random_sample(5))
print(np.random.randint(0,8))
print([ np.random.randint(0,8) for i in range(10)])