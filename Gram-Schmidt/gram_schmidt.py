'''
Parsia Hedayat, 2023

This file is meant to find the best approximation of
a function in C_R[lower, upper] using a polynomial of 
degree at most N.

It implements inner product, length, and gram-schmidt
specific to C_R[lower, upper]. It also implements a
more general projection function, projecting a vector
onto a subset of C_R[lower, upper]. 

Note that this is made sure of, not a guarantee. The 
projection function could be used to project any 
vector onto any subspace as long as a basis (defined 
the way it is in this file) is defined.
'''

import numpy as np
import matplotlib.pyplot as plt

from sympy import (
    N,
    pi,
    sin,
    sqrt,
    Symbol,
    integrate,
    init_printing,
)

init_printing(use_unicode=True)

from sys import argv
coeff = int(argv[1])

DISP_INTERVAL = (-coeff*pi, coeff*pi)
INTERVAL = (float(N(DISP_INTERVAL[0])), float(N(DISP_INTERVAL[1])))

def inner_product(f, g, s):
    return integrate(f*g, (s, INTERVAL[0], INTERVAL[1]))

def length(f, s):
    return sqrt(inner_product(f, f, s))

def create_basis(dim, s):
    return [1, s]+[s**i for i in range(2, dim)]

def gram_schmidt(basis, s):
    e = dict()
    e[1] = basis[0] / length(basis[0], s)
    for i in range(1, len(basis)):
        e[i+1] = basis[i]
        for k in range(1, i):
            e[i+1] -= inner_product(basis[i], e[k], s)*e[k]
        e[i+1] *= 1/length(e[i+1], s)
    return e

def PU(v, s, basis):
    dim = len(basis)
    p = inner_product(v, basis[1], s)
    for i in range(2, dim+1):
        p += inner_product(v, basis[i], s)*basis[i]
    return p

def run(dim, f):
    x = Symbol("x")
    basis = create_basis(dim, x)
    orthonormal_basis = gram_schmidt(basis, x)
    projection = PU(f, x, orthonormal_basis)
    return projection

def plot_run(proj_evals, f_evals, ax):
    I = np.linspace(INTERVAL[0], INTERVAL[1], 1000)
    ax.plot(I, proj_evals, "r-")
    ax.plot(I, f_evals, "b-")

def mse(u, v):
    return (1/len(u))*np.sum(np.square(u-v))

def f(s):
    return sin(s)

if __name__ == "__main__":
    R1, C1 = 4, 4
    function_name = "sin(x)"
    fig1, axes1 = plt.subplots(R1, C1)
    fig1.suptitle(f"Approximating {function_name} using polynomials\n{DISP_INTERVAL}")
    fig1.supxlabel("Dimension of Basis (Degree of Polynomial - 1)")
    fig1.supylabel(f"Plot of Approximation against {function_name}")
    fig1.tight_layout(pad=2.0)

    fig2, axes2 = plt.subplots()
    fig2.suptitle(f"MSE on {function_name} and projection, based on basis dimension")
    fig2.supxlabel("Basis Dimension")
    fig2.supylabel(f"MSE of {function_name} and projection")
    fig2.tight_layout(pad=2.0)

    x = Symbol("x")
    I = np.linspace(INTERVAL[0], INTERVAL[1], 1000)
    f_results = np.asarray([f(i) for i in I])

    dim = 2
    proj_results = []
    for i in range(R1):
        print(i)
        for j in range(C1):
            axis = axes1[i, j].set_title(f"dim {dim}")
            proj = run(dim, f(x))
            res = [proj.evalf(subs={"x": k}) for k in I]
            proj_results.append(res)
            plot_run(res, f_results, axes1[i, j])
            dim += 1
    proj_results = np.asarray(proj_results)

    mse_results = [mse(f_results, proj_results[i]) for i in range(len(proj_results))]

    epsilon = 1e-5
    for i in range(len(mse_results)):
        if epsilon - mse_results[i] >= 0:
            print(f"For interval {DISP_INTERVAL}, dim is {i}")
            break

    axes2.plot(np.arange(2, dim), mse_results)

    plt.show()
