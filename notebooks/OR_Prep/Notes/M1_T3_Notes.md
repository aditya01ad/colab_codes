# Module 1, Topic 3: Day 01 — Python Coding Notes

## Scope
Topics covered: Python, NumPy, Pandas, SciPy (`linprog`), Matplotlib, Duality, Sensitivity.

---

## 1) Python Basics

### Variables and data types
```python
x = 10                  # int
y = 3.14                # float
name = "Product A"      # str
active = True           # bool

type(x)                 # Check type
int(3.8)                # 3
float(5)                # 5.0
str(100)                # "100"
```

### Data structures
```python
# List — ordered, mutable
a = [10, 20, 30]
a[0]                    # 10
a.append(40)
a.pop()
len(a)

# Tuple — ordered, immutable
t = (10, 20)

# Dictionary — key-value pairs
d = {"A": 40, "B": 30}
d["A"]
d.keys()
d.values()
d.items()

# Set — unique elements
s = {1, 2, 3}
s.add(4)
```

### Operators
```python
a + b
a - b
a * b
a / b
a // b
a % b
a ** b

a == b
a != b
a > b
a <= b

and, or, not
```

### Conditions
```python
if x > 10:
    print("High")
elif x == 10:
    print("Equal")
else:
    print("Low")
```

### Loops
```python
for i in range(5):
    print(i)

for item in a:
    print(item)

for key, value in d.items():
    print(key, value)

while x > 0:
    x -= 1
```

### Functions and lambda
```python
def profit(x, y):
    return 40*x + 30*y

profit(40, 20)          # 2200

f = lambda x: x**2
f(5)                    # 25
```

### Comprehensions and aggregation
```python
squares = [x**2 for x in range(5)]
positive = [x for x in a if x > 0]
total = sum(d.values())
```

### Assertions and validation
```python
assert x >= 0

if x < 0:
    raise ValueError("Negative value")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero")
```

**Key points**
- Indentation defines blocks.
- Lists are mutable; tuples are immutable.
- Functions improve reusability.

---

## 2) NumPy — Numerical Computing

```python
import numpy as np
```

### Arrays
```python
a = np.array([1, 2, 3])

A = np.array([
    [2, 1],
    [1, 2]
])

np.zeros((2, 3))
np.ones((2, 2))
np.eye(3)
np.arange(0, 10, 2)
np.linspace(0, 10, 50)
```

### Array properties
```python
A.shape
A.ndim
A.size
A.dtype
A.T
```

### Mathematical operations
```python
a + 2
a * 2
a ** 2

np.sum(a)
np.mean(a)
np.max(a)
np.min(a)

A @ np.array([40, 20])
np.dot(a, a)
```

### Linear algebra
```python
b = np.array([100, 80])

np.linalg.solve(A, b)
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.eig(A)
np.linalg.matrix_rank(A)
```

**Important**
- `*` is elementwise multiplication.
- `@` is matrix multiplication.
- Prefer `np.linalg.solve(A, b)` over computing `A^{-1}b` explicitly.

---

## 3) Pandas — Data Analysis

```python
import pandas as pd
```

### Create DataFrame
```python
df = pd.DataFrame({
    "Product": ["A", "B"],
    "Profit": [40, 30],
    "Machine1": [2, 1],
    "Machine2": [1, 2]
})
```

### Inspection
```python
df.head()
df.tail()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

### Selection
```python
df["Profit"]
df.loc[0, "Profit"]
df.iloc[0, 1]
df[df["Profit"] > 30]
```

### Cleaning
```python
df.isnull().sum()
df.duplicated().sum()
df.drop_duplicates()

df.dropna()
df.fillna(0)

df["Profit"].astype(float)
```

### Operations
```python
df["Revenue"] = df["Profit"] * 10
df.sort_values("Profit", ascending=False)
df.groupby("Product")["Profit"].sum()

df["Profit"].mean()
df["Profit"].sum()
```

### File handling
```python
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)

df = pd.read_excel("data.xlsx")
df.to_excel("output.xlsx", index=False)
```

**Remember**
- `loc` = label-based selection
- `iloc` = position-based selection
- `groupby` = grouped aggregation
- `merge` = combine datasets

---

## 4) SciPy — Linear Programming

```python
from scipy.optimize import linprog
```

### Model
\[
\max Z = 40x + 30y
\]

Subject to:
\[
2x + y \le 100
\]
\[
x + 2y \le 80, \quad x,y \ge 0
\]

### Implementation
```python
c = [-40, -30]          # Negative for maximization

A = [
    [2, 1],
    [1, 2]
]

b = [100, 80]

result = linprog(
    c=c,
    A_ub=A,
    b_ub=b,
    bounds=[(0, None), (0, None)],
    method="highs"
)

if result.success:
    print("Solution:", result.x)
    print("Maximum profit:", -result.fun)
else:
    print(result.message)
```

Output:
```text
Solution: [40. 20.]
Maximum profit: 2200.0
```

### Parameters summary

| Syntax | Meaning |
|---|---|
| `c` | Objective coefficients |
| `A_ub` | Inequality constraint matrix |
| `b_ub` | Inequality RHS |
| `A_eq` | Equality constraint matrix |
| `b_eq` | Equality RHS |
| `bounds` | Variable limits |
| `method="highs"` | HiGHS solver |
| `result.x` | Optimal variables |
| `result.fun` | Minimized objective |
| `result.success` | Solver success flag |
| `result.message` | Solver information |

---

## 5) Matplotlib — Graphical LP

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 60, 200)

y1 = 100 - 2*x
y2 = (80 - x)/2

plt.plot(x, y1, label="2x + y = 100")
plt.plot(x, y2, label="x + 2y = 80")

y_feasible = np.maximum(
    0,
    np.minimum(y1, y2)
)

plt.fill_between(
    x, 0, y_feasible,
    where=(y1 >= 0) & (y2 >= 0),
    alpha=0.3
)

plt.scatter(40, 20, color="red", label="Optimal")

plt.xlim(0, 60)
plt.ylim(0, 60)
plt.xlabel("Product A")
plt.ylabel("Product B")
plt.title("LP Feasible Region")
plt.legend()
plt.grid(True)
plt.show()
```

### Plotting syntax

| Syntax | Purpose |
|---|---|
| `plt.plot()` | Draw lines |
| `plt.scatter()` | Plot points |
| `plt.fill_between()` | Shade regions |
| `plt.xlabel()` | X-axis label |
| `plt.ylabel()` | Y-axis label |
| `plt.title()` | Graph title |
| `plt.legend()` | Show labels |
| `plt.grid()` | Show grid |
| `plt.show()` | Display plot |

---

## 6) Duality and Shadow Prices in Python

### Shadow prices
```python
result.ineqlin.marginals
```

SciPy returns sensitivities for the minimization problem provided to `linprog`. Since we negated the maximization objective, reverse sign for original max interpretation:

```python
shadow_prices = -result.ineqlin.marginals
print(shadow_prices)
```

Expected:
```text
[16.66666667  6.66666667]
```

### Constraint slack
```python
slack = result.ineqlin.residual
print(slack)
```

Expected:
```text
[0. 0.]
```

### Verify constraints
```python
A = np.array(A)
b = np.array(b)

usage = A @ result.x
slack = b - usage

print("Resource usage:", usage)
print("Remaining capacity:", slack)

assert np.all(usage <= b + 1e-7)
assert np.all(result.x >= -1e-7)
```

### Duality check
```python
primal_value = -result.fun
dual_value = np.dot(b, shadow_prices)

print(primal_value, dual_value)
assert np.isclose(primal_value, dual_value)
```

Both values:
\[
2200
\]

---

## 7) Sensitivity and Scenario Analysis

### Capacity change
```python
new_b = [105, 80]

new_result = linprog(
    c=c,
    A_ub=A,
    b_ub=new_b,
    bounds=(0, None),
    method="highs"
)

if new_result.success:
    print(new_result.x)
    print(-new_result.fun)
```

Expected:
```text
[43.33333333 18.33333333]
2283.3333333333335
```

### Shadow-price estimate
```python
change = 5
estimated_gain = shadow_prices[0] * change
print(estimated_gain)
```

Result:
\[
83.33
\]

### Multiple scenarios
```python
scenarios = {
    "Baseline": [100, 80],
    "Expansion A": [105, 80],
    "Expansion B": [100, 90],
    "Reduced": [90, 70]
}

results = []

for name, capacity in scenarios.items():
    sol = linprog(
        c=c,
        A_ub=A,
        b_ub=capacity,
        bounds=(0, None),
        method="highs"
    )

    results.append({
        "Scenario": name,
        "Profit": -sol.fun if sol.success else None,
        "Success": sol.success
    })

comparison = pd.DataFrame(results)
print(comparison)
```

Concept: solve the same model under alternative parameter sets and compare outcomes.

---

## Essential Syntax — Final Revision

| Syntax | Meaning |
|---|---|
| `=` | Assignment |
| `==` | Equality comparison |
| `!=` | Not equal |
| `:` | Start indented block / slicing |
| `def` | Define function |
| `return` | Return value |
| `for` | Iteration |
| `if/elif/else` | Conditional logic |
| `lambda` | Anonymous function |
| `import` | Import library |
| `try/except` | Exception handling |
| `assert` | Development-time assertion |
| `sum()` | Summation |
| `len()` | Length |
| `range()` | Integer sequence |
| `enumerate()` | Index-value iteration |
| `zip()` | Iterate multiple iterables |
| `np.array()` | Numerical array |
| `@` | Matrix multiplication |
| `np.linalg.solve()` | Solve linear equations |
| `pd.DataFrame()` | Tabular data |
| `df.loc[]` | Label-based selection |
| `df.iloc[]` | Position-based selection |
| `linprog()` | Linear programming solver |
| `result.x` | Optimization solution |
| `result.fun` | Minimized objective |
| `result.ineqlin.marginals` | RHS sensitivities |
| `result.ineqlin.residual` | Constraint slack |
| `plt.plot()` | Plot lines |

---

## Workflow Rule

**Data → Model → Solve → Validate → Interpret**

Study status: Theory completed ✅ | Coding concepts revised ✅ | Independent Colab implementation ⬜
