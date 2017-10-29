from sympy import Symbol, solve
r = Symbol ('r')
equation = 2000000*(1+r)*(1-(1+r)**6)/(1-(1+r))-12500000
print (solve(equation, dict=True))