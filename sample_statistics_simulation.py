import numpy as np
import matplotlib.pyplot as plt

#Number of samples:
num_samples = 10000

# Values of N:
N_values = [2, 20, 200, 5000]

# Equation for the calculation of the mean value for X and Y variables:
def calculate_mean(data):
    return np.mean(data)

# Determine the means of X and Y variables as matrices in 
# order to take the mean values for every N-values:
means_x = []
means_y = []

for N in N_values:
    # Sample values following exponential distribution:
    x_samples = np.random.exponential(scale=1/2, size=(num_samples, N))

    # Sample values following uniform distribution in [0,4]:
    y_samples = np.random.uniform(low=0, high=4, size=(num_samples, N))
    
    # Calculation of the mean values for X and Y variables:
    means_x.append(np.mean(x_samples, axis=1))
    means_y.append(np.mean(y_samples, axis=1))

# Determine the standard deviations of X and Y variables  
# as matrices in order to take the standard deviations values
# for every N-values:
std_dev_x = [np.std(means) for means in means_x]
std_dev_y = [np.std(means) for means in means_y]

#Print the standard deviation in each N-case:
print("Var[X]=", std_dev_x, "for N = 2, 20, 200, 500")
print("Var[Y]=", std_dev_y, "for N = 2, 20, 200, 500")


colors = ['blue', 'green', 'orange', 'red']

#plt.figure(figsize=(9, 6))

# Plot for mean of x:
#plt.subplot(2, 1, 1)
for i in range(len(N_values)):
    plt.hist(means_x[i], bins=30, alpha=0.7, label=f'N={N_values[i]}', color=colors[i], edgecolor='black')
plt.xlabel('Mean of x')
plt.ylabel('Frequency')
plt.title('Histograms of Sample Mean for variable X')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot for mean of y:
#plt.subplot(2, 1, 2)
for i in range(len(N_values)):
    plt.hist(means_y[i], bins=30, alpha=0.7, label=f'N={N_values[i]}', color=colors[i], edgecolor='black')
plt.xlabel('Mean of y')
plt.ylabel('Frequency')
plt.title('Histograms of Sample Mean for variable Y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
