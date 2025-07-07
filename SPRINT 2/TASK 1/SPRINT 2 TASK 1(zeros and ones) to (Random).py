import numpy as np

array_1_to_10 = np.arange(1, 11)
print("Array from 1 to 10:", array_1_to_10)

array_step_2 = np.arange(1, 11, 2)
print("Array with step 2:", array_step_2)

zeros_array = np.zeros(3)
print("Zeros array:", zeros_array)

ones_matrix = np.ones((10, 10))
print("10x10 matrix of ones:\n", ones_matrix)

evenly_spaced_array = np.linspace(1, 11, 25)

print("25 evenly spaced numbers from 1 to 11:")
print(evenly_spaced_array)

identity_matrix = np.eye(10)


print("10x10 Identity Matrix:")
print(identity_matrix)

random_array = np.random.rand(4)

print("Random array:", random_array)

random_1d = np.random.randn(2)
print("1D array from standard normal distribution:", random_1d)


random_6x6 = np.random.randn(6, 6)
print("6x6 matrix from standard normal distribution:\n", random_6x6)



random_int = np.random.randint(1, 6)
print("Random integer:", random_int)

random_array = np.random.randint(1, 6, size=10)
print("1D array of random integers:", random_array)

sequential_array = np.arange(25)


print("1D array with 25 sequential integers from 0:")
print(sequential_array)

Numpy_array = np.random.randint(0,50,size=10)
print("Numpy array")
print(Numpy_array)
