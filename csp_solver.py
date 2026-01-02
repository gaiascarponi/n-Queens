# csp_solver.py
from constraint import Problem, AllDifferentConstraint
import time

def solve_nqueens_csp(n):
    """    Solves the n-queen problem by reducing it to a problem of 
    Constraint Satisfaction (CSP)."""
    start_time = time.perf_counter()
    p = Problem()
    p.addVariables(range(n), range(n))
    p.addConstraint(AllDifferentConstraint())
    for i in range(n):
        for j in range(i + 1, n):
            p.addConstraint(lambda r1, r2, c1=i, c2=j: abs(r1 - r2) != abs(c1 - c2), (i, j))
    sol = p.getSolution()
    return {"time": time.perf_counter() - start_time, "solution": sol}
