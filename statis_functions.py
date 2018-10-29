import numpy as np

def Pearson_correlation_coefficient(x, y):
	x_mean = np.mean(x)
	y_mean = np.mean(y)
	numerators = np.dot(x-x_mean, y-y_mean)
	denominators = np.linalg.norm(x-x_mean, 2)*np.linalg.norm(y-y_mean, 2)
	return numerators/denominators

def Kendall_tau_coefficient(x, y):
	n = len(x)
	denominators = n*(n-1)/2
	

if __name__ == "__main__": 
	x = np.array(range(9))
	y = np.random.random(9)
	print(y)
	print(Pearson_correlation_coefficient(x, y))