import matplotlib.pyplot as plt
import numpy as np
fig,ax = plt.subplots() 
plt.rcParams["axes.labelsize"]=12
plt.rcParams["xtick.labelsize"]=12
plt.rcParams["ytick.labelsize"]=12
plt.rcParams["legend.fontsize"]=12

## Lennard-Jones potentail 
## Eps,i,j[(Rmin,i,j/ri,j)**12 - 2(Rmin,i,j/ri,j)**6]
# The Lennard-Jones parameters:

epsilon=   0.10 # Kcal/mol
r_min_by_2 = 1.9000   # J.nm^12

r = np.linspace(3, 6, 1000)
# Interatomic potential
U = epsilon *( (2*(r_min_by_2)/r)**12 - 2*((2*(r_min_by_2)/r)**6) )
# Interatomic force
F = (12*epsilon/r) *( (2*(r_min_by_2)/r)**12 - ((2*(r_min_by_2)/r)**6) ) 

line1 = plt.plot(r, U, 'k', lw=2, label=r'U(r)')
plt.xlim(3, 6)
plt.ylim(-0.12, 0.8)
ax.set_ylabel("Energy ($\mathrm{kcal/mol}$)",fontsize=12)
plt.grid(linestyle="--")
ax2=plt.twinx()
line2 = plt.plot(r, F, 'k', ls=':', lw=2, label=r'F(r)')
plt.xlim(3,6)
plt.ylim(-0.2, 0.3)
ax.set_xlabel("Interatomic distance ($\mathrm{\AA}$)",fontsize=12)
ax2.set_ylabel( "Force ($\mathrm{kcal/mol/\AA}$)",fontsize=12)


# Jump through some hoops to get the both line's labels in the same legend:

lines = line1 + line2
labels = []
for line in lines:
    labels.append(line.get_label())
plt.legend(lines, labels)
fig.savefig('LJ.png', format='png',bbox_inches='tight',dpi=600)

