# Module 0, Topic 1: Python Boot Camp for OR — Session Notes

**Date:** July 29, 2026
**Status:** Completed ✅

---

## What we built

A single Colab notebook containing a mini logistics data pipeline — the exact pattern used before feeding data into optimization models.

---

## Concepts covered

### 1. Functions with default arguments
```python
def shipping_cost(weight_kg, distance_km, base_rate=5.0):
```
- Default values make functions flexible.
- Docstrings explain what the function does — write them always.
- Input validation (`if weight <= 0`) prevents garbage results.

### 2. Control flow for business logic
- `if/elif/else` for discounts and surcharges.
- Real-world logic: bulk discount (>100 kg → 15% off), long-distance surcharge (>1000 km → 10% extra).
- `round()` for clean currency output.

### 3. Lists and iteration
- Storing structured data as lists of lists: `[weight, distance]`.
- `enumerate()` for index + value in loops.
- f-strings for formatted printing.

### 4. List comprehensions
- Generating cost matrices: `[[2 * d for d in row] for row in distances]`.
- Random data generation with `random.seed()` for reproducibility.
- Cleaner than nested loops — use when building matrices for OR models.

### 5. File I/O
- Writing CSV: `open(file, 'w')` then `f.write()`.
- Reading CSV: `open(file, 'r')` then `f.readlines()`.
- Parsing: `line.strip().split(',')`.
- Skipping headers with slice: `lines[1:]`.

### 6. Data pipeline pattern
```
Raw CSV → load → parse → transform (compute cost) → structure (matrix) → analysis
```
This is the exact flow for every OR project:
- Load supply/demand/distance data
- Compute cost coefficients
- Build constraint matrices
- Feed into solver

### 7. Functions as reusable blocks
- `load_shipping_data(filepath)` → returns list of dicts.
- `compute_route_cost(distance_km, ...)` → single responsibility.
- `build_cost_matrix(data, warehouses, stores)` → transforms flat data to 2D matrix.
- Composition: small functions combined to do complex tasks.

### 8. Dictionaries for structured data
- `{'warehouse': 'WH1', 'store': 'S1', 'distance_km': 210.0, ...}`
- More readable than parallel lists.
- Easy to filter, transform, and pass between functions.

---

## OR-relevant patterns introduced

| Pattern | OR application |
|---------|---------------|
| Cost matrix generation | Objective coefficients for transportation LP |
| Distance matrix | Constraint RHS for vehicle routing |
| Bulk discount logic | Piecewise linear cost functions |
| File reading pipeline | Loading real-world logistics data |
| Function composition | Building solver input data cleanly |

---

## Files created

- `M0_T1_Python_Bootcamp.ipynb` — Colab notebook with all code
- `shipping_data.csv` — sample logistics dataset
- `M0_T1_Notes.md` — this file

---

## Solo practice completed

- Added cost per unit column
- Wrote `cheapest_route_from_warehouse()` function
- Generated 5×6 random dataset and built cost matrix

---

## Key takeaway

> Before optimization comes data. Every LP, IP, or network model needs clean, structured input. Python functions + file I/O + list comprehensions are the tools that bridge raw data and the solver. Master these, and you'll never struggle to set up a model.

