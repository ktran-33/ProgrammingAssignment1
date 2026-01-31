import time
import random
import csv
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import Match as match
import Verifier as verifier


# Benchmarking script for matcher and verifier, creates a CSV output in miliseconds
def random_pref(n):
    # Returns 1-based preference list (as expected by gale_shapley after fetch_input converts them)
    # We need to convert to 0-based for direct gale_shapley call
    l = list(range(0, n))  # 0-based
    random.shuffle(l)
    return l

n_vals = [1,2,4,8,16,32,64,128,256,512]

csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'benchmark_results.csv')
with open(csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['n', 'matcher_ms', 'verifier_ms'])
    
    for n in n_vals:
        hospital_preferences = [random_pref(n) for _ in range(n)]
        student_preferences = [random_pref(n) for _ in range(n)]

        start = time.perf_counter()
        matches = match.gale_shapley(n, hospital_preferences, student_preferences)
        end = time.perf_counter()
        matcher_time = (end - start) * 1000

        start = time.perf_counter()
        verifier.verifier(matches, n, hospital_preferences, student_preferences)
        end = time.perf_counter()
        verifier_time = (end - start) * 1000

        writer.writerow([n, f'{matcher_time:.2f}', f'{verifier_time:.2f}'])

print(f"Results are written to {csv_path}")
