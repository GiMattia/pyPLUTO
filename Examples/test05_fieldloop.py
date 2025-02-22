"""
Classical MHD Field loop test

This test shows how to compute streamlines and field lines of the magnetic field
in a display with two subplots.

The data are the ones obtained from the PLUTO test problem
$PLUTO_DIR/Test_Problems/MHD/Field_Loop (configuration 5).

The data is loaded into a pload object D and the Image class is created. The
display method is used to plot the x and y components of the magnetic field. The
find_fieldlines method is used to compute the field lines of the magnetic field.
The streamplot method is used to plot the streamlines of the magnetic field in
the first display, while the plot method is used to plot the field lines
previously computed. The image is then saved and shown on screen.
"""

# Loading the relevant packages
import pyPLUTO as pp

# Loading the data into a pload object D
D = pp.Load(path="Test_Problems/MHD/Field_Loop")

# Creating the image
I = pp.Image(figsize=[13, 5], suptitle="Test 05 - MHD Field loop test")

# Creating the subplots
ax = I.create_axes(ncol=2, top=0.91)

# Integrate the field line
lines = D.find_fieldlines(
    D.Bx1,
    D.Bx2,
    x1=D.x1,
    x2=D.x2,
    x0=[0.1, 0.2, 0.3],
    y0=[0.0, 0.0, 0.0],
    order="RK45",
    maxstep=0.1,
    numsteps=25000,
)

# Plotting the data
I.display(
    1000 * D.Bx1,
    x1=D.x1,
    x2=D.x2,
    ax=0,
    cmap="RdBu_r",
    aspect="equal",
    xrange=[-0.5, 0.5],
    cpos="right",
    vmin=-1.5,
    vmax=1.5,
    shading="gouraud",
    title=r"$B_x$ (+ streamplot)",
    xtitle="x",
    ytitle="y",
)

I.display(
    1000 * D.Bx2,
    x1=D.x1,
    x2=D.x2,
    ax=1,
    cmap="RdBu_r",
    aspect="equal",
    xrange=[-0.5, 0.5],
    cpos="right",
    vmin=-1.5,
    vmax=1.5,
    shading="gouraud",
    title=r"$B_y$ (+ find$\_$fieldlines)",
    xtitle="x",
)

# Plot the field lines in two different ways
I.streamplot(D.Bx1, D.Bx2, x1=D.x1, x2=D.x2, ax=0, lw=1.5, vmin=1.0e-4, c="k")

I.plot(lines[0][0], lines[0][1], ax=1, c="k", lw=1.5)
I.plot(lines[1][0], lines[1][1], ax=1, c="k", lw=1.5)
I.plot(lines[2][0], lines[2][1], ax=1, c="k", lw=1.5)

# Saving the image and showing the plots
I.savefig("test05_fieldloop.png")
pp.show()
