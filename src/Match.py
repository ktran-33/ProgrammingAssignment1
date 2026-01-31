import sys
from collections import deque

def fetch_input(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()
        if not line:
            raise ValueError("Empty input file") # Empty File Edge Case
        n = int(line)

        # Obtain hospital preferences
        hospital_preferences = []
        for _ in range(n):
            row = file.readline().split()
            if len(row) != n:
                raise ValueError("Invalid hospital preference row length") # Invalid Row Length Edge Case
            preferences = list(map(int, row))
            if sorted(preferences) != list(range(1, n+1)):
                raise ValueError("Invalid hospital preference list") # Invalid Preference List Edge Case
            preferences = [x-1 for x in preferences] # Using zero-based indexing
            hospital_preferences.append(preferences)

        # Obtain student preferences
        student_preferences = []
        for _ in range(n):
            row = file.readline().split()
            if len(row) != n:
                raise ValueError("Invalid student preference row length") # Invalid Row Length Edge Case
            preferences = list(map(int, row))
            if sorted(preferences) != list(range(1, n+1)):
                raise ValueError("Invalid student preference list") # Invalid Preference List Edge Case
            preferences = [x-1 for x in preferences] # Using zero-based indexing
            student_preferences.append(preferences)
    return n, hospital_preferences, student_preferences

def gale_shapley(n, hospital_preferences, student_preferences):

    if n == 0:
        return []  # Edge Case: no hospitals or students
    
    # -1 for unmatched, 0 is inital next proposal for all hospitals
    hospital_match = [-1] * n
    student_match = [-1] * n
    next_proposal = [0] * n

    # Ranking of hospitals for each student
    student_rank = []
    for i in range(n):
        row = [0] * n
        student_rank.append(row)

    for s in range(n):
        for rank, h in enumerate(student_preferences[s]):
            student_rank[s][h] = rank
    
    # Updated to a deque for more efficiency
    # List of free hospitals
    free_hospitals = deque(range(n))
    
    # Main loop of Gale-Shapley algorithm
    while free_hospitals:
        h = free_hospitals.popleft() # Hospital that proposes
        if next_proposal[h] >= n: # Check to avoid over-proposing
            continue

        s = hospital_preferences[h][next_proposal[h]] # Student to propose to
        next_proposal[h] += 1 # Move pointer to next student for hospital h

        if student_match[s] == -1: # Assign if student is free
            hospital_match[h] = s
            student_match[s] = h
        else: # Student is already matched
            h_prime = student_match[s]
            # Check if student prefers new hospital `h` over current `h_prime`
            if student_rank[s][h] < student_rank[s][h_prime]: 
                # If student prefers h over h_prime, reassign
                hospital_match[h] = s
                student_match[s] = h
                hospital_match[h_prime] = -1
                free_hospitals.append(h_prime)
            else: 
                # Student rejects hospital h
                free_hospitals.append(h)

    return hospital_match

def main():
    if len(sys.argv) != 3:
        print("Usage: python Match.py <input_file> <output_file>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # n, hospital_preferences, student_preferences = fetch_input(input_file)

    try: # For handling invalid input cases
        n, hospital_preferences, student_preferences = fetch_input(input_file)
    except ValueError as e:
        print(f"INVALID INPUT: {e}")
        return

    matches = gale_shapley(n, hospital_preferences, student_preferences)

    # Writing output to file in one-based indexing
    with open(output_file, 'w') as file:
        for h, s in enumerate(matches):
            file.write(f"{h+1} {s+1}\n")


if __name__ == "__main__":
    main()
