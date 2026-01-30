import sys

#Get matches and preferences from match.py
import match

def verifier(matches, n, hospital_preferences, student_preferences):
    # Edge Cases
    # Equal Hospitals and Students
    if len(hospital_preferences) != len(student_preferences):
        print("INVALID DIFFERING AMOUNTS OF HOSPITALS AND STUDENTS")

    if n == 0:
        print("VALID STABLE")
        return
    if not matches:
        print("INVALID NO MATCHES")
        return

    #(a)  Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates.
    hospital_seen = set()
    student_seen = set()
    for h, s in enumerate(matches): # hospital = index, student = value
        if h in hospital_seen:
            print("INVALID HOSPITAL MATCHED MORE THAN ONCE")
            return
        if s in student_seen:
            print("INVALID STUDENT MATCHED MORE THAN ONCE")
            return
        
        # add to the sets
        hospital_seen.add(h)
        student_seen.add(s)
    
    # Unmatched
    if len(hospital_seen) != n or len(student_seen) != n:
        print("INVALID UNMATCHED HOSPITAL AND/OR STUDENT")
        return

    #(b) checks stability: confirms there is no blocking pair.
    # Citation: Algorithm Design Textbook pg 46-47

    # Student Pref Ranking
    student_rank = []
    for i in range(n):
        row = [0] * n
        student_rank.append(row)

    for s in range(n):
        for rank, h in enumerate(student_preferences[s]):
            student_rank[s][h] = rank

    # Hospital Pref Ranking
    hospital_rank = []
    for i in range(n):
        row = [0] * n
        hospital_rank.append(row)

    for h in range(n):
        for rank, s in enumerate(hospital_preferences[h]):
            hospital_rank[h][s] = rank

    # Get Index Student, Value Hospital
    matches_swap = [0]*n
    for h, s in enumerate(matches):
        matches_swap[s] = h
    
    # S and H must BOTH prefer each other, but are not matched to each other
    for h in range(n):
        s_prime = matches[h]

        for s in range(n):
            if s_prime == s:
                continue # Matched with each other already

            h_prime = matches_swap[s]
            # Compare values student_ranking[s, h] and student_ranking[s, h'] (from TB)
            # Both prefer each other
            if (student_rank[s][h] < student_rank[s][h_prime]) and (hospital_rank[h][s] < hospital_rank[h][s_prime]):
                blocking_pair = "Hospital " + {h+1} + ", Student " + {s+1} # not the current partners
                print("UNSTABLE Example Blocking Pair: ", blocking_pair)
                return
        
    print("VALID STABLE")
    return

        
def main():
    if len(sys.argv) != 2:
        print("Usage: python match.py <input_file>")
        return
    
    input_file = sys.argv[1]

    n, hospital_preferences, student_preferences = match.fetch_input(input_file)
    matches = match.gale_shapley(n, hospital_preferences, student_preferences)

    verifier(matches, n, hospital_preferences, student_preferences)

if __name__ == "__main__":
    main()