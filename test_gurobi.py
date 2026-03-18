import gurobipy as gp
from gurobipy import GRB

# 数据
values = [6, 10, 12]
weights = [2, 2, 3]
W = 5
n = len(values)

# 模型
m = gp.Model("knapsack")

# 变量：x_i ∈ {0,1}
x = m.addVars(n, vtype=GRB.BINARY, name="x")

# 目标函数
m.setObjective(gp.quicksum(values[i]*x[i] for i in range(n)), GRB.MAXIMIZE)

# 约束
m.addConstr(gp.quicksum(weights[i]*x[i] for i in range(n)) <= W, name="capacity")

# 求解
m.optimize()

# 输出结果
print("Optimal value:", m.objVal)

for i in range(n):
    print(f"x[{i}] =", x[i].x)
    