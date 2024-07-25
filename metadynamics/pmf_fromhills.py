import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('pdf')

# Load the data from the file
data = np.loadtxt('nvt5.colvars.metadynamics.hills.traj')

# Assign columns to variables for clarity
cv1 = data[:, 1]
cv2 = data[:, 2]
bias_potential = data[:, 5]

# Define the number of bins for the collective variables
num_bins = 100

# Create a 2D histogram of the collective variables, using the bias potential as weights
hist, xedges, yedges = np.histogram2d(cv1, cv2, bins=num_bins, weights=bias_potential)

# Normalize the histogram to avoid logarithm issues with zero values
hist = np.clip(hist, a_min=1e-10, a_max=None)

# Calculate the free energy
kbT = 0.001987 * 300  # Boltzmann constant in kcal/mol*K * Temperature in K (300 K assumed)
free_energy = -kbT * np.log(hist)

# Average the free energy over the second collective variable (CV2) to get the PMF as a function of CV1
pmf_cv1 = np.mean(free_energy, axis=1)
cv1_centers = (xedges[:-1] + xedges[1:]) / 2

# Average the free energy over the first collective variable (CV1) to get the PMF as a function of CV2
pmf_cv2 = np.mean(free_energy, axis=0)
cv2_centers = (yedges[:-1] + yedges[1:]) / 2

# Plot the PMF as a function of CV1
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(cv1_centers, pmf_cv1)
plt.xlabel('Collective Variable 1')
plt.ylabel('Free Energy (kcal/mol)')
plt.xticks(np.arange(0,22,2))
plt.yticks(np.arange(6,16,1))
plt.title('PMF vs CV1')

# Plot the PMF as a function of CV2
plt.subplot(1, 2, 2)
plt.plot(cv2_centers, pmf_cv2)
plt.xlabel('Collective Variable 2')
plt.ylabel('Free Energy (kcal/mol)')
plt.xticks(np.arange(0,1,0.1))
plt.yticks(np.arange(6,16,1))
plt.title('PMF vs CV2')
plt.tight_layout()
plt.savefig("hills.png")
#plt.show()
