from numpy import *
from pylab import *

#%% 1D problem - backward approximation (Neumann BC)

def FDA_backward(L, N, qN, r):
    #inputs: L - 1D domain length
    #        N - number of sample points
    #       qN - Neumann BC
    #        r - source term/function
    
    #initialization
    h = L/(N-1) # N-1: number of steps 
    x = linspace(0,L,N) #3rd argument: sample points NOT step
    U = zeros((N,1))
    M = zeros((N,N))
    S = zeros((N,1)) #pre-assignment
    
    #declaration
    M[0,0] = 1 #Dirichlet BC
    for i in range(1, N-1): # 0 & 10 excluded : repectively store Dirichlet & Neumann BCs
        M[i,i-1] = M[i,i+1] = 1/h**2
        M[i,i] = -2/(h**2)
    M[N-1,N-2] = -1/h #Neumann BC: backward approximation
    M[N-1,N-1] = 1/h
    
    S[0,0] = 0 #Dirichlet BC
    for i in range (1,N-1): #solves the source term for each sample point
        if isinstance(r, int)== False:
            S[i,0] = -r(x[i])
        elif isinstance(r, int) == True:
            S[i,0] = -r
            
    S[N-1,0] = qN #Neumann BC
    U = solve(M,S)
    
    #code checking
    # print('backward method:')
    # print('Matrix M:\n', M)
    # print('Solution vector S:\n', S)
    # print('Column vector U:\n', U)
   
    return U

#%% 1D problem - fictitious point method (Neumann BC)

def FDA_fictitious(L, N, qN, r):
    #inputs: L - 1D domain length
    #        N - number of sample points
    #       qN - Neumann BC
    #        r - source term/function
   
    
    #initialization
    h = L/(N-1) # N-1: number of steps 
    x = linspace(0,L,N)
    U = zeros((N,1))
    M = zeros((N,N))
    S = zeros((N,1)) #pre-assignment
    
    #declaration
    M[0,0] = 1 #Dirichlet BC
    for i in range(1, N-1): # 0 & 10 excluded : repectively store Dirichlet & Neumann BCs
        M[i,i-1] = M[i,i+1] = 1/h**2
        M[i,i] = -2/(h**2)
    M[N-1,N-2] =  -1/h #Neumann BC: fictitious point method
    M[N-1,N-1] = 1/h
    
    S[0,0] = 0 #Dirichlet BC
    for i in range (1,N-1): #solves the source term for each sample point
        if isinstance(r, int)== False:
            S[i,0] = -r(x[i])
            S[N-1,0] = qN + (h*r(L))/2 #Neumann BC
        elif isinstance(r, int) == True:
            S[i,0] = -r
            S[N-1,0] = qN + (h*r)/2 #Neumann BC
            
    U = solve(M,S)
    
    #code checking
    # print('fictitious method:')
    # print('Matrix M:\n', M)
    # print('Solution vector S:\n', S)
    # print('Column vector U:\n', U)
   
    return U

#%% computing of the evolution of epsilon in function of 1/h

def f1(x):
    return (-x**2/2)+2*x
r1 = 1
def f2(x):
    return (1/pi**2)*sin(pi*x)+((pi+1)/pi)*x
def r2(x):
    return sin(pi*x/1) 
def f3(x):
    return (4/pi**2)*sin(pi*x/2)+x
def r3(x):
    return sin(pi*x/2)

#function computing epsilonfor a specific number of nodes
def error(x,f,F):
    e = zeros(size(x))
    for i in range(0, size(x)):
        e[i] = abs(F[i]-f[i])
    epsilon = e.max()
    return epsilon

e1_backward_full = zeros(5)
e1_fictitious_full = zeros(5)
e2_backward_full = zeros(5)
e2_fictitious_full = zeros(5)
e3_backward_full = zeros(5)
e3_fictitious_full = zeros(5)

counter = 0
for i in range (5, 26, 5 ): # for N= 5, 10, 15, 20, 25
    x = linspace(0,1,i)
    f1_full = f1(x)
    f2_full = f2(x)
    f3_full = f3(x)
    
    e1_backward_full[counter] = error(x, f1_full, FDA_backward(1, i, 1, r1))
    e1_fictitious_full[counter] = error(x, f1_full, FDA_fictitious(1, i, 1, r1))
    
    F2_backward = FDA_backward(1, i, 1, r2)
    e2_backward_full[counter] = error(x, f2_full, F2_backward)
    F2_fictitious= FDA_fictitious(1, i, 1, r2) 
    e2_fictitious_full[counter] = error(x, f2_full, F2_fictitious)
    
    F3_backward = FDA_backward(1, i, 1, r3)
    e3_backward_full[counter] = error(x, f3_full, F3_backward)
    F3_fictitious = FDA_fictitious(1, i, 1, r3)
    e3_fictitious_full[counter]= error(x, f3_full, F3_fictitious)
    
    counter +=1


#%% plotting of the loglog error plots

inverse_h = array([1/(5-1),1/(10-1),1/(15-1),1/(20-1),1/(25-1)]) 

fig1 = figure()
loglog(inverse_h, e1_backward_full,label='backward approximation')
loglog(inverse_h, e1_fictitious_full,label='fictitious point method')
xlabel('1/h')
ylabel('epsilon(1/h)')
title('r(x) = 1')
legend()

fig2 = figure()
loglog(inverse_h, e2_backward_full,label='backward approximation')
loglog(inverse_h, e2_fictitious_full,label='fictitious point method')
xlabel('1/h')
ylabel('epsilon(1/h)')
title('r(x) = sin(pix/L)')
legend()

fig3 = figure()
loglog(inverse_h, e3_backward_full,label='backward approximation')
loglog(inverse_h, e3_fictitious_full,label='fictitious point method')
xlabel('1/h')
ylabel('epsilon(1/h)')
title('r(x) = sin(pix/(2L))')
legend()

#%% EXTRA: case 1 plotting

N = 10

x = linspace(0, 1, N) #x = linspace(0,L,N)
f1 = f1(x)
F1_backward = FDA_backward(1, N, 1, r1)
F1_fictitious = FDA_fictitious(1, N, 1, r1)

figure()   
plot(x, f1, label='exact solution')
xlabel('x')
ylabel('y')
title('r(x) = 1')
legend()
plot(x, F1_backward,'--',label='backward approximation')
legend()
plot(x, F1_fictitious,'--',label='fictitious point method')
legend()

#%% EXTRA: case 2 plotting

x = linspace(0, 1, N) #x = linspace(0,L,N)
f2 = f2(x)
F2_backward = FDA_backward(1, N, 1, r2)
F2_fictitious = FDA_fictitious(1, N, 1, r2)

figure()
plot(x, f2, label='exact solution')
xlabel('x')
ylabel('y')
title('r(x) = sin(pix/L)')
legend()
plot(x, F2_backward,'--',label='backward approximation')
legend()
plot(x, F2_fictitious,'--',label='fictitious point method')
legend()



#%% EXTRA: case 3 plotting

x = linspace(0, 1, N) #x = linspace(0,L,N)
f3 = f3(x)
F3_backward = FDA_backward(1, N, 1, r3)
F3_fictitious = FDA_fictitious(1, N, 1, r3)

figure()
plot(x, f3, label='exact solution')
xlabel('x')
ylabel('y')
title('r(x) = sin(pix/(2L)')
legend()
plot(x, F3_backward,'--',label='backward approximation')
legend()
plot(x,F3_fictitious,'--',label='fictitious point method')
legend()



