# Customer Order Analysis

Small Python exercises in analysing order and sales data — written to practise the core moves (grouping, aggregating, ranking) with and without pandas.

## What's here

**`customer-order-analysis.py`** — pure standard library, no dependencies. Works over a small hardcoded order list and computes:

- total revenue
- revenue broken down by category
- spend per customer, and the top spender
- most-purchased product

Everything is built with `defaultdict` and comprehensions rather than a dataframe library, to keep the aggregation logic visible.

**`sale-analysis.py`** — the same territory using **pandas**: loads sales data from a CSV, then groups and summarises it.

## Running

```bash
python3 customer-order-analysis.py
```

The first script needs nothing installed. For the pandas one:

```bash
pip install pandas && python3 sale-analysis.py
```
