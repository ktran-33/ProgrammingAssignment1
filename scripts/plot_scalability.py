import matplotlib.pyplot as plt
import csv
import os

# Used to plot scalability results from benchmark.py
csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'benchmark_results.csv')

n_values = []
matcher_times = []
verifier_times = []

# Read the CSV file created by benchmark.py
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        n, matcher_ms, verifier_ms = row
        n_values.append(int(n))
        matcher_times.append(float(matcher_ms))
        verifier_times.append(float(verifier_ms))

# Create results directory if it doesn't exist
results_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
os.makedirs(results_dir, exist_ok=True)

# Plot
plt.figure(figsize=(10,6))
plt.plot(n_values, matcher_times, marker='o', label='Matcher Runtime (ms)')
plt.plot(n_values, verifier_times, marker='s', label='Verifier Runtime (ms)')
plt.xlabel("Number of Hospitals/Students (n)")
plt.ylabel("Time (ms)")
plt.title("Task C: Scalability of Matcher and Verifier")
plt.xscale('log', base=2)  # log scale for better visualization
plt.yscale('log', base=10)  # log scale for wide time ranges
plt.xticks(n_values, n_values)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend()
plt.tight_layout()

plot_path = os.path.join(results_dir, 'scalability_plot.png')
plt.savefig(plot_path)
print(f"Plot saved to {plot_path}")
plt.show()
