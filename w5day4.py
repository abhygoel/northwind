import argparse
from pathlib import Path
import time

parser = argparse.ArgumentParser(description="Clean Northwind customer data.")
parser.add_argument("input_file", help="the CSV export to clean")
parser.add_argument("--output-dir", default=".", help="folder for the output files")
args = parser.parse_args()

print(args.input_file)
print(args.output_dir)

output_dir = Path(args.output_dir)
output_dir.mkdir(exist_ok=True)
clean_path = output_dir / "clean_customers.csv"

start = time.perf_counter()
#...the work....
elapsed = time.perf_counter() - start
print(f"Finished in {elapsed:.2f} seconds")

number_list = list(range(100000))
number_set = set(range(100000))

start = time.perf_counter()
for _ in range(1000):
    99999 in number_list
list_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(1000):
    99999 in number_set
set_time = time.perf_counter() - start

print(f"{list_time:.6f}")
print(f"{set_time:.6f}")