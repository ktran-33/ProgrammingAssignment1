# Programming Assignment 1
UFIDs:  
89625286  
75200264

## Overview
The assignment has been written in Python 3. 

## Task A and B Information:
### Compile/Build Instructions
No compilation is required. The assignment was tested in a virtual environment but it may not be strictly necessary.

The commands are  
python3 -m venv venv  
venv\Scripts\activate  # On Windows
#### or
source venv/bin/activate  # On macOS/Linux

### Instructions to Run Matcher and Verifier

The command usage to run the matcher file is:  
python3 src/Match.py <input_file> <output_file>  
E.g.:  
python3 src/Match.py data/example.in data/example.out  
Expected output in `example.out`  
1 1  
2 2  
3 3  

The command usage to run the matcher file is:  
python3 src/Verifier.py <input_file>  

E.g.:  
python3 src/Verifier.py data/example.in  
Expected output:  
VALID STABLE  

### Assumptions
Out input was received from a file named `example.in` in the data folder, while output written to `example.out`. It has been formatted by the assignment specifications.  

For Task C plotting, matplotlib is required, which may be installed using:  

pip install matplotlib  

Suggestion: On MacOS devices, the python or pip command may not work if using the built-in python installation. In such case, add a '3' to the end of the keyword, ie (python3, pip3).  

### Dependencies (condensed)

Core: Python 3.x (standard library only: sys, collections, csv)  
For Task C plotting: matplotlib (install via pip install matplotlib)  

## Task C:

The commands I used to plot are the following:  

python3 scripts/benchmark.py  

This generates timing data across n = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512] and writes results to:  
data/benchmark_results.csv

Next, the scalability graph was created using this command:  

python3 scripts/plot_scalability.py  

This command reads the CSV and generates a graph in:  

results/scalability_plot.png  

Our test results yielded the following graph:  
![alt text](image.png)  
