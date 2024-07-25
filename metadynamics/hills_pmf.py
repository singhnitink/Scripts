import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('pdf')
plt.style.use('classic')
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['axes.linewidth']= 2


plt.figure(figsize=(12, 8))

folders=["k1l1","k2l2","k3l3","k4l4","k6l6","k12l12"]
labels=[r"$\mathbf{(K_{1}L_{1})_{12}}$", r"$\mathbf{(K_{2}L_{2})_6}$", r"$\mathbf{(K_{3}L_{3})_4}$", r"$\mathbf{(K_{4}L_{4})_3}$", r"$\mathbf{(K_{6}L_{6})_2}$", r"$\mathbf{(K_{12}L_{12})_1}$"]
i=0
for files in folders:
    # Load the data from the file
    data = np.loadtxt(files+'/nvt5.colvars.metadynamics.hills.traj')

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



    # Plot the PMF as a function of CV2
    plt.plot(cv2_centers, pmf_cv2, label=labels[i], lw=3)
    i+=1
plt.xlabel("Fraction of α-helix", fontweight='bold')
plt.ylim(4,15)
plt.xlim(0,1.0)
plt.ylabel("Free energy(Kcal/mol)", fontweight='bold')
plt.legend(loc='upper right')
plt.xticks(np.arange(0,1.1,0.1), fontweight='bold')
plt.yticks(np.arange(4,16,1), fontweight='bold')
plt.savefig("hills_all.png")
#plt.show()
