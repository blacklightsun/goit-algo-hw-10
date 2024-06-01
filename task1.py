from pulp import *

# Create an object of a model
prob = LpProblem("Max Total Producing qty", LpMaximize)

#  Define the decision variables
x1 = LpVariable("Lemonade qty", 0)
x2 = LpVariable("Fruit Juice qty", 0)

# Define the objective function
prob += 1*x1 + 1*x2  # цінність кожного виду продукції не вказана в умовах завдання, вважаємо їх рівними

# Define the constraints
prob += 2*x1 + 1*x2 <= 100.0
prob += 1*x1 + 0*x2 <= 50.0
prob += 1*x1 + 0*x2 <= 30.0
prob += 0*x1 + 2*x2 <= 40.0

# Solve the linear programming problem
prob.solve()

# Print the results
print("Status: ", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("The optimal value of the objective function is = ", value(prob.objective))
