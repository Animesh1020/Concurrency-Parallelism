import random
import time
import multiprocessing
from faker import Faker

fake = Faker()

def generate_orders():
    orders = []
    for _ in range(10000):
        orders.append({
            "order_id":fake.uuid4(),
            "supplier":fake.company(),
            "quantity":random.randint(1, 500),
            "unit_price":round(random.uniform(5.0, 500.0), 2),
            "days_since_dispatch": random.randint(1, 30),
        })
    return orders

def process_order(order):

    order["total_value"] = order["quantity"] * order["unit_price"]

    if order["days_since_dispatch"] > 10:
        order["shipment_status"] = "overdue"
    else:
        order["shipment_status"] = "on track"

    if order["quantity"] < 20:
        order["stock_alert"] = "low stock"
    else:
        order["stock_alert"] = "ok"

    return order

def run_single(orders):
  
    start = time.perf_counter()
    results = []
    for order in orders:
        results.append(process_order(order))

    end = time.perf_counter()
    print(f"Single time: {end - start:.2f}s")

def run_multi(orders):
  
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        results = pool.map(process_order, orders)

    end = time.perf_counter()
    print(f"Multi time: {end - start:.2f}s")

if __name__ == "__main__":
  
    orders = generate_orders()
    print(f"Generated {len(orders)} orders\n")
    run_single(orders)
    run_multi(orders)
