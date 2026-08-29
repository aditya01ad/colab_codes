# Module 0, Topic 2: NumPy for OR — Session Notes

**Date:** July 30, 2026  
**Status:** Completed ✅

## Concepts covered
- Creating arrays: `np.array`, `zeros`, `ones`, `eye`, `arange`, `linspace`
- Indexing & slicing: row/column access, boolean masks, `np.where`
- Vectorized operations: arithmetic, broadcasting, reshaping
- Aggregations: `sum`, `mean`, `min`, `max`, `std`, axis parameter
- Linear algebra: matrix multiplication (`@`), `linalg.solve` for small systems
- Random number generation: `randint`, `normal`, `uniform`, seeding
- File I/O: `savetxt`, `loadtxt`, `save`, `load`

## OR applications
- Cost matrices for transportation models
- Constraint matrix assembly (`A @ x`)
- Random instance generation for testing models
- Broadcasting for adding fixed charges per warehouse

## Key takeaway
NumPy eliminates loops for array math. In OR, most model data lives in matrices (costs, distances, constraint coefficients). Mastering NumPy means you can prepare solver input with clean, fast vectorized code — essential for both small-scale PuLP models and large-scale commercial solver interfaces.
