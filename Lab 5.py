from scipy.optimize import linprog
from pulp import *

if __name__ == '__main__':
    a = [[0, 180, 170, 160, 150],
         [190, 0, 170, 160, 150],
         [190, 180, 0, 160, 150],
         [190, 180, 170, 0, 150],
         [190, 180, 170, 160, 0]]
    q1 = LpVariable("q1", lowBound=0)
    q2 = LpVariable("q2", lowBound=0)
    q3 = LpVariable("q3", lowBound=0)
    q4 = LpVariable("q4", lowBound=0)
    q5 = LpVariable("q5", lowBound=0)
    problem = LpProblem('0', LpMaximize)
    problem += q1 + q2 + q3 + q4 + q5, "1"
    for i in range(len(a)):
        problem += a[0][i] * q1 + a[1][i] * q2 + a[2][i] * q3 + a[3][i] * q4 + a[4][i] * q5 <= 1, str(i + 2)
    problem.solve()
    v = 1 / sum([elem.varValue for elem in problem.variables()])
    print("v = {} грн.".format(v))
    y = [elem.varValue * v for elem in problem.variables()]
    for i in range(len(y)):
        print('y{} = {}'.format(i+1, y[i]))
    f = [-1, -1, -1, -1, -1]
    A = [[a[i][j] for i in range(len(a))] for j in range(len(a))]
    b = [1, 1, 1, 1, 1]
    print('------------------------------------------')
    res = linprog(f, A_ub=A, b_ub=b, bounds=[(0, None), (0, None), (0, None), (0, None), (0, None)], method='simplex')
    v2 = 1 / (-res.fun)
    print("v = {} грн.".format(v2))
    y2 = [elem * v2 for elem in res.x]
    for i in range(len(y)):
        print('y{} = {}'.format(i+1, y2[i]))