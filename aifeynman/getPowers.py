import numpy as np
import pandas as pd
from scipy.sparse.linalg import lsqr
from scipy.linalg import *
from sympy import Matrix
from sympy import symbols, Add, Mul, S
from numpy.linalg import matrix_rank
from itertools import combinations


N = np.array([[ 0,  1,  1],
              [ 0, -1, -1],
              [ 1,  0, 0],
              [ 0,  0,  0],
              [ 0,  0,  0],
              [ 0,  0, 0],])

N = np.array([[ 0,  0,  3,  1,  1,  1,  1,  1,  1],
              [ 0,  0, -2,  0,  0,  0,  0,  0,  0],
              [ 1,  1, -1,  0,  0,  0,  0,  0,  0],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
              [ 0,  0,  0,  0,  0,  0,  0,  0,  0]])

a = np.array([ 1, -2,  1,  0,  0,  0])

def getPowers(N,a):
    rand_drop_cols = np.arange(0,len(N[0]),1)
    rand_drop_rows = np.arange(0,len(N),1)
    rand_drop_rows = np.flip(rand_drop_rows)
    rank = matrix_rank(N) #find rank of matrix
    d_cols = list(combinations(rand_drop_cols,len(N[0])-rank)) #create combinations of columns that when deleted result in full rank matrix (note, combinations, NOT permutations, order is kept)
    d_rows = list(combinations(rand_drop_rows,len(N)-rank))
    for i in d_cols: #purpose of this nested loop is to find the full rank matrix representing linear equations
        M = N
        M = np.delete(M,i,1)
        M = np.transpose(M)
        for j in d_rows:
            P = M
            P = np.delete(P,j,1)
            if np.linalg.det(P)!=0:
                solved_M = np.transpose(P)
                indices_sol = j
                indices_powers = i
                break

    b = np.delete(a,indices_sol) #create another vector representing solutions of the linear equations
    params = np.linalg.solve(solved_M,b) #solve simultaneous equation problem

    sol = []
    for i in range(len(N[0])): #allocate the solutions of simultaneous equation problem to a vector to return it
        if i in indices_powers: # if the index was to be removed, put i
            sol = sol + [0]
        else:
            sol = sol + [params[0]]
            params = np.delete(params,0)

    # this is the solution:
    sol = np.array(sol)
    return(sol)


