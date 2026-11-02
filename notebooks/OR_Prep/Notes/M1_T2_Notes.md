# Module 1, Topic 2: OR Theory — Quick Revision Notes

## Topics Covered
1. Python Essentials  
2. Pandas for Data Handling  
3. Linear Programming (LP)  
5. Graphical Method  
6. Duality and Shadow Prices  
7. Sensitivity and Scenario Analysis

---

## 1) Python Essentials
Python is used to implement mathematical and analytical ideas.

- **Variables**: store values (cost, profit, capacity)
- **Lists**: ordered collections
- **Dictionaries**: key-value data
- **Functions**: reusable operations
- **Conditions**: decision logic
- **Loops**: repeated operations
- **Validation**: input/result checks

**Key point:** Python implements the model; it does not replace mathematical reasoning.

---

## 2) Pandas — Data Handling
Pandas converts raw data into structured, analyzable information.

- **Series**: 1D labeled data
- **DataFrame**: 2D tabular data
- **Cleaning**: handle missing, duplicate, invalid entries
- **Validation**: ensure consistency and correctness

**Key point:** Bad input data can produce an optimal but practically wrong solution.

---

## 3) Linear Programming (LP)
LP optimizes a linear objective under linear constraints.

\[
\max Z = c^T x
\]

Subject to:

\[
Ax \le b, \quad x \ge 0
\]

### Core concepts
- **Decision variables**: controllable quantities
- **Objective function**: maximize/minimize target
- **Constraints**: limits/restrictions
- **Feasible solution**: satisfies all constraints

**Optimal solution:** best objective value among all feasible solutions.

### Possible outcomes
- Unique optimum
- Multiple optima
- Infeasible
- Unbounded

### SciPy + HiGHS
- `linprog` solves minimization forms
- For maximization of \(c^Tx\), minimize \(-c^Tx\)
- HiGHS provides optimization algorithms
- Always check solver success and feasibility

---

## 5) Graphical Method (2 Variables)
Used for geometric solution of two-variable LPs.

- **Constraint line**: boundary of a constraint
- **Feasible region**: satisfies all constraints
- **Corner point**: vertex of feasible region
- **Binding constraint**: active at equality
- **Slack**: unused resource

\[
\text{Slack} = b_i - a_i^T x
\]

If slack = 0, the constraint is binding.

**LP theorem (corner-point idea):** when an optimum exists and extreme points exist, at least one optimum is attained at an extreme point.

---

## 6) Duality and Shadow Prices

### A) Duality
Every LP has a corresponding dual.

| Primal | Dual |
|---|---|
| Maximizes profit | Minimizes resource valuation |
| Chooses production quantities | Chooses implicit resource values |
| Uses capacity constraints | Uses value constraints |
| Optimal value = ₹2,200 | Optimal value = ₹2,200 |

**Weak duality** (for this max-form primal setup):
\[
Z_{\text{primal}} \le W_{\text{dual}}
\]

**Strong duality:**
\[
Z^*_{\text{primal}} = W^*_{\text{dual}}
\]

**Interpretation:**
- Primal: what should we produce?
- Dual: how should we value resources?

### B) Shadow Price
Marginal change in optimal objective due to one-unit increase in a resource RHS:

\[
\text{Shadow Price} = \frac{\partial Z^*}{\partial b_i}
\]

Example:
\[
u = \frac{50}{3} \approx 16.67\;\text{₹/hour}
\]

Meaning: +1 Machine 1 hour increases maximum profit by ~₹16.67 (within valid sensitivity range).

### C) Complementary Slackness

\[
u_i s_i = 0
\]

Where \(u_i\) is dual variable and \(s_i\) is primal slack.

- Positive slack \(\Rightarrow\) zero shadow price
- Positive shadow price \(\Rightarrow\) binding constraint
- A binding constraint may still have zero shadow price

---

## 7) Sensitivity and Scenario Analysis

### A) Sensitivity Analysis
Studies effect of parameter changes on optimal solution/objective.

1. **RHS sensitivity**:
\[
b_i \rightarrow b_i + \Delta b_i
\]

2. **Objective-coefficient sensitivity**:
\[
c_i \rightarrow c_i + \Delta c_i
\]

For valid RHS range:
\[
\Delta Z = u_i \Delta b_i
\]

Example (+5 Machine 1 hours):
\[
\Delta Z = \frac{50}{3}\times 5 \approx 83.33
\]

### B) Scenario Analysis
Compares outcomes across explicit alternative conditions.

Example scenarios:
- Normal capacity
- Increased capacity
- Reduced capacity
- Increased production costs

**Difference:**
- Sensitivity analysis: parameter effect (often local)
- Scenario analysis: comparison across full assumption sets

---

## One Integrated Example

\[
\max Z = 40x + 30y
\]

Subject to:

\[
2x + y \le 100
\]
\[
x + 2y \le 80
\]
\[
x, y \ge 0
\]

| Concept | Result | Interpretation |
|---|---|---|
| Decision variables | \(x, y\) | Production quantities |
| Objective | \(40x + 30y\) | Maximize contribution margin |
| Constraints | Machine capacities | Limited resources |
| Optimal solution | \(x=40, y=20\) | Best production mix |
| Optimal value | ₹2,200 | Maximum contribution margin |
| Binding constraints | Both machines | Full capacity used |
| Slack | 0 for both | No unused machine hours |
| Dual objective | ₹2,200 | Equals primal optimum |
| Machine 1 shadow price | ₹16.67/hour | Marginal value of capacity |
| Machine 2 shadow price | ₹6.67/hour | Marginal value of capacity |
| Sensitivity | +5 Machine 1 hours | Profit increases ₹83.33 |
| Scenario analysis | Compare capacity plans | Identify preferable decisions |

---

## Workflow Summary

**Python → Pandas → LP → Graphical → Duality → Sensitivity**  
**Code → Data → Optimize → Visualize → Value → Analyze**

Guiding questions:
1. How do we compute?
2. What data do we have?
3. What is the best decision?
4. Why is it optimal?
5. What are resources worth?
6. What changes under new conditions?
