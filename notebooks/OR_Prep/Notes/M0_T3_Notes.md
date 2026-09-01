# Module 0, Topic 3: Pandas for OR — Session Notes

**Date:** July 31, 2026  
**Status:** Completed ✅

## Concepts covered
- DataFrame creation, loading CSV, inspection (head, shape, dtypes, isnull)
- Filtering with boolean conditions, .loc/.iloc
- GroupBy aggregation: sum, mean, count, custom agg
- Pivot tables: converting long data to matrix form for OR models
- Merging DataFrames (left join) to combine orders with capacity and cost data
- Data cleaning: dropna, fillna, handling negative/invalid values
- Export: to_csv, to_numpy

## OR applications
- Building distance/cost matrices via pivot_table
- Summarizing demand by store and supply by warehouse
- Preparing solver-ready NumPy arrays from raw logistics data
- Merging disparate data sources into a single clean table for modeling

## Key takeaway
Pandas is the data wrangling layer for OR. Real-world problems come as messy CSVs or database exports. Using groupby and pivot_table transforms them into the clean matrices and vectors that optimization models require.
