"""
MHD Rotor test

This test shows how to compute and plot contour lines of the vector potential
from a test problem in non-cartesian coordinates.

The data are the ones obtained from the PLUTO test problem
$PLUTO_DIR/Test_Problems/MHD/Rotor (configuration 4).

The data is loaded into a pload object D and the Image class is created. The
display method is used to plot the density and the magnetic field magnitude. The
contour_lines method is used to compute the contour lines of the vector
potential. The plot method is used to plot the contour lines on the density and
magnetic field magnitude plots. The image is then saved and shown on screen.

Note thast in the left subplot the lines are all in red, although, by applying
the cmap keyword to the method "find_contour", they can be associated to the
different colors of a cmap. Conversely, the lines in the right plot have
different colors based on their contour level.

IMPORTANT: in order to produce the contour lines of the vector potential, the
following lines should be added to the definitions.h file:

#define  UPDATE_VECTOR_POTENTIAL        YES

in the user-defined constants section.
"""

import numpy as np

import pyPLUTO as pp

# Loading the data into a pload object D
D = pp.Load(path="Test_Problems/MHD/Rotor")

# Creating the image
I = pp.Image(
    nwin=2,
    suptitle="Test 04 - MHD Rotor test",
    figsize=[11, 5],
    suptitlesize=22,
)

# Creating the subplots (2 for the different variables)
ax = I.create_axes(ncol=2)

# Compute the magnetic field magnitude
B2 = np.sqrt(D.Bx1**2 + D.Bx2**2 + D.Bx3**2)

# Plotting the data (colorbars adaptively positioned)
I.display(
    D.rho,
    x1=D.x1rc,
    x2=D.x2rc,
    cpos="right",
    aspect="equal",
    ax=0,
    cscale="log",
    title="Density",
    xtitle="x",
    ytitle="y",
)

I.display(
    B2,
    x1=D.x1rc,
    x2=D.x2rc,
    cpos="right",
    aspect="equal",
    ax=1,
    title="Magnetic field magnitude",
    xtitle="x",
)

# Compute the contour lines of the vector potential in two different ways
lines = D.find_contour(D.Ax3, cmap="hot")
contours = [I.plot(line[0], line[1], ax=I.ax[0], c="r") for line in lines]

I.contour(
    D.Ax3,
    levels=[-0.1, -0.05, -0.01, 0.01, 0.05, 0.1],
    ax=I.ax[1],
    x1=D.x1c,
    x2=D.x2c,
)

# Saving the image and showing the plots
I.savefig("test04_rotor.png")
pp.show()
