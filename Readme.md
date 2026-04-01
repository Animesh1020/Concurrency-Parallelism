# Concurrency & Parallelism in Python

A practical project demonstrating async I/O and multiprocessing in Python.

---

## Task 1 — Async API Fetcher (`task1_supplier_fetch.py`)

Fetches supplier and product data from a fake API using `asyncio` and `aiohttp`.

- Uses `asyncio.gather()` to fetch all suppliers **concurrently**
- Compares **sequential vs concurrent** timing
- Shows how `await` suspends coroutines without blocking

**Libraries:** `asyncio`, `aiohttp`

---

## Task 2 — Parallel Order Processing (`task2_order_processing.py`)

Generates 10,000 fake order records and processes them using `multiprocessing`.

- Generates orders using `Faker` library
- Computes total value, shipment status, stock alert per order
- Compares **single process vs multiprocessing.Pool** timing

**Libraries:** `multiprocessing`, `faker`

---

## Setup
```bash
pip install aiohttp faker
```

---

## Branch Structure
```
main
├── feature/task-1
└── feature/task-2
```