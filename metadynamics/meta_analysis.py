import pandas as pd
import numpy as np
from sklearn import metrics
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use('pdf')
plt.style.use('classic')
mpl.rcParams['xtick.major.size'] = 8
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.size'] = 8
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['axes.linewidth']= 2

data1=pd.read_csv("nvt1.colvars.traj",skipinitialspace=True,delimiter=" ", comment='#',header=None,skiprows=lambda x: x % 1 != 0)
data1 = data1.rename({'0': 'Step', '1': 'rgyr', '2':'separation'}, axis=1)

data2=pd.read_csv("nvt2.colvars.traj",skipinitialspace=True,delimiter=" ", comment='#',header=None,skiprows=lambda x: x % 1 != 0)
data2 = data2.rename({'0': 'Step', '1': 'rgyr', '2':'separation'}, axis=1)

data3=pd.read_csv("nvt3.colvars.traj",skipinitialspace=True,delimiter=" ", comment='#',header=None,skiprows=lambda x: x % 1 != 0)
data3 = data3.rename({'0': 'Step', '1': 'rgyr', '2':'separation'}, axis=1)

data4=pd.read_csv("nvt4.colvars.traj",skipinitialspace=True,delimiter=" ", comment='#',header=None,skiprows=lambda x: x % 1 != 0)
data4 = data4.rename({'0': 'Step', '1': 'rgyr', '2':'separation'}, axis=1)

data5=pd.read_csv("nvt5.colvars.traj",skipinitialspace=True,delimiter=" ", comment='#',header=None,skiprows=lambda x: x % 1 != 0)
data5 = data5.rename({'0': 'Step', '1': 'rgyr', '2':'separation'}, axis=1)

#Check the convergence
import matplotlib.cm as cm
times=np.arange(55000000,105000000,5000000)
colormap=cm.tab20b
num_data=len(times)
i=0
plt.figure()
for time in times:
    data_pmf=pd.read_csv("nvt5."+str(time)+".pmf",skipinitialspace=True,delimiter=" ", comment='#',header=None)
    data_pmf.columns =['column1','column2','column3']
    col1_values=data_pmf.loc[:,'column1'].unique()
    average_with_col1=[]
    for value in col1_values:
        average_with_col1.append(np.min(data_pmf.loc[(data_pmf['column1'] == value) , "column3"].values[:])*4.184)
        #print(value)
        #print(data_pmf.loc[(data_pmf['column1'] == value) , "column3"].values[:])
    color=colormap(i/num_data)
    plt.plot(col1_values,average_with_col1, label=time, color=color, linewidth=3)
    i+=1
plt.title("Column 1")
plt.xlabel("Colvar 1", fontweight='bold')
plt.ylabel("Free energy", fontweight='bold')
plt.legend(loc='best',bbox_to_anchor=(1,0.8))
plt.savefig("colvar1_convergence.png")

import matplotlib.cm as cm
times=np.arange(55000000,105000000,5000000)
colormap=cm.tab20b
num_data=len(times)
i=0
plt.figure()
for time in times:
    data_pmf=pd.read_csv("nvt5."+str(time)+".pmf",skipinitialspace=True,delimiter=" ", comment='#',header=None)
    data_pmf.columns =['column1','column2','column3']
    col1_values=data_pmf.loc[:,'column2'].unique()
    average_with_col1=[]
    for value in col1_values:
        average_with_col1.append((np.min(data_pmf.loc[(data_pmf['column2'] == value) , "column3"].values[:]))*4.184)
        #print(value)
        #print(data_pmf.loc[(data_pmf['column1'] == value) , "column3"].values[:])
    color=colormap(i/num_data)
    plt.plot(col1_values,average_with_col1, label=time, color=color, linewidth=3)
    i+=1
plt.title("Column 2")
plt.xlabel("Colvar 2", fontweight='bold')
plt.ylabel("Free energy", fontweight='bold')
plt.legend(loc='best',bbox_to_anchor=(1,0.8))
plt.savefig("colvar2_convergence.png")

import numpy as np
import matplotlib.pyplot as plt

# Extract data from the metadynamics output file
# Load data from the file
data = np.loadtxt("nvt5."+str(time)+".pmf")
# Extract the first two columns as colvars
colvar1 = data[:, 0]
colvar2 = data[:, 1]
free_energy = data[:, 2]
# Sort the data based on colvar1 and colvar2
sorted_indices = np.lexsort((colvar2, colvar1))
colvar1 = np.array(colvar1)[sorted_indices]
colvar2 = np.array(colvar2)[sorted_indices]
free_energy = np.array(free_energy)[sorted_indices]

# Create 2D grid and reshape free energy values
n_colvar1 = len(set(colvar1))
n_colvar2 = len(set(colvar2))
colvar1_grid = colvar1.reshape((n_colvar1, n_colvar2))
colvar2_grid = colvar2.reshape((n_colvar1, n_colvar2))
free_energy_grid = free_energy.reshape((n_colvar1, n_colvar2))

# Optionally, you can apply some smoothing to the free energy surface
# You can use interpolation or Gaussian filtering from SciPy for this purpose.

# Plot the free energy landscape as a heatmap or contour plot
plt.figure(figsize=(8, 6))
plt.contourf( colvar1_grid ,colvar2_grid,free_energy_grid, cmap='jet')
plt.colorbar(label='Free Energy (kcal/mol)')
plt.xlabel('Collective Variable 2')
plt.ylabel('Collective Variable 1')
plt.title('Free Energy Landscape')
#plt.xlim(6,20)
#plt.ylim(5,14)
plt.savefig("heatmap.png")
