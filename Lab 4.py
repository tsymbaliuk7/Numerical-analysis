from scipy.optimize import linprog
from pulp import *

if __name__ == '__main__':
    x1 = LpVariable("x1", lowBound=100)
    x2 = LpVariable("x2", lowBound=50)
    problem = LpProblem('0', LpMaximize)
    problem += 100*x1 + 150*x2 - 12000, "1"
    problem += 50*x1 + 100*x2 <= 15000, "2"
    problem.solve()
    print('Func:')
    print(value(problem.objective))
    print('Result:')
    for elem in problem.variables():
        print(elem.name, '=', elem.varValue)
    print('------------------------------------------')
    f = [-100, -150, 12000]
    A = [[50, 100, 0]]
    b = 15000
    x0_bounds = (200, None)
    x1_bounds = (50, None)
    x2_bounds = (1, 1)
    res = linprog(f, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds, x2_bounds], method='simplex')
    print('Function:')
    print(-res.fun)
    print('Result:')
    print(res.x[0], res.x[1])
