# -*- coding: utf-8 -*-
"""
UPDATED
Mon Sept 25 2018

@author: G.Legrain
"""

#To avoid problems with integer divisions
#from __future__ import division; 
#To use a matlab-like syntax
from numpy import *
from pylab import *


#%% --------------------- Assign variable : ---------------------
#On the left of the equal, the variable, and on the right its value
#Be carefull python uses automatic type deduction !!!
a=10 #(integer)
b=10.#(float)


#%% --------------------- Vectors : ---------------------
# Vectors initialized with zero values :
# 'zero' function is part of numpy
V1 = zeros(10) #Vector with 4 components
V2 = zeros((10,1)) #Alternative definition as a matrix with one column

#Split [0,1] in 10 intervals
#linspace function is part of numpy
V3 = linspace(0,1,10)
#Create a vector between 0 (included) and 1 (excluded) with step 0.1
V4 = arange(0,1,0.1)

#Vector initialized with ones:
V5 = ones(5)

#Access / modification of the values stored inside the vectors:
V1[3] = 3.

#%% --------------------- Matrices : ---------------------
# Matrix initialized with zero values
M1 = zeros((4,4)) #4x4 matrix
# Matrix initialized with ones
M3 = ones((2,2))

#Access / modification of the values stored inside the matrices :
M1[0,0] = 1

#Get the shape of a matrix / vector :
print('The shape of M1 is', M1.shape)

#%% --------------------- Loops : ---------------------
# Here, we create a loop where we enter ten times
# Variable i will vary from 0 to 9 within this loop
for i in range(10):
    print ('In loop, i=',i)


# We can change the beginning of the loop
for i in range(5, 10):
    print ('In second loop, i=',i)


#%% --------------------- Solving: ---------------------
#Create a diagonal matrix
M2 = eye(4)
#Create a vector filled with 2.
V5 = 2.*ones(4)

#Solve the linear system M2 * V6 = V5
V6 = solve(M2,V5)

#Check if we really have M2 * V6 = V5
residual = M2 @ V6 - V5

#Norm of the residual
print('After solve, residual norm is', norm(residual))



#%% --------------------- Functions: ---------------------
#You can define functions
def myFunction(inputVariable):
    print('Input is', inputVariable)
    return 2*inputVariable

result = myFunction(45)
print('result is', result)


#%% ---------------------  1D plot ---------------------
x = V3
y = V3**2 #(y = x²)

#Open a figure
figure()
plot(x,y,label='x**2');
xlabel('x')#Set a label to horizontal axis
ylabel('y')#Set a label to vertical axis
legend()#Display the legend

#Plot a second curve with a dashed line
plot(x,x**3,'--',label='x**3');
legend()#Update the legend

#Open another figure
figure()
#Loglog plot:
loglog(x,y,label='name (loglog)');
xlabel('x')
ylabel('y')
legend()



#%% ---------------------  2D / 3D plot ---------------------

# x and y nodes grid
x=linspace(-1,1,100);
y=linspace(-1,1,100);
# Combination of the x and y grids
[X,Y]=meshgrid(x,y);

#To plot in 3D
from mpl_toolkits.mplot3d import Axes3D

#We want to plot f(x,y)= (x^2-1)*(y^2-1)
Z = (X**2 - 1)* (Y**2 - 1)

#Open another figure
figure()
#Contour plot
contourf(X, Y, Z)
#Same scale for x and y :
axis('equal')
#Color bar:
colorbar()
#Axis labels
xlabel('x')#Set a label to horizontal axis
ylabel('y')#Set a label to vertical axis

fig=figure()
ax=fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=cm.viridis)
#Axis labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#Draw the colorbar (note that it is not like in 2D):
colorbar(surf)

#if you don't want to plot all point, you can change rstride and cstride
#To plot every two points:
fig2=figure()
ax2=fig2.gca(projection='3d')
surf2 = ax2.plot_surface(X, Y, Z,rstride=2, cstride=2, cmap=cm.viridis)
#Draw the colorbar:
colorbar(surf2)
#Axis labels
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

#You can also change the colormap
fig3=figure()
ax3=fig3.gca(projection='3d')
surf3 = ax3.plot_surface(X, Y, Z,rstride=2, cstride=2, cmap=cm.coolwarm)
#Draw the colorbar:
colorbar(surf3)

#Axis labels
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('z')
