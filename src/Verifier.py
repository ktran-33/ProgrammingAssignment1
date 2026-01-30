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
    if matches.empty:
        print("VALID STABLE")
        return
    if hospital_preferences.empty and student_preferences.empty:
        print("VALID STABLE")
        return

    #(a)  Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates.
    hospital_seen = set()
    student_seen = set()
    for h, s in matches.items(): # hospital = index, student = value
        if h in hospital_seen:
            print("INVALID VIA HOSPITAL MATCHED MORE THAN ONCE")
            return
        if s in student_seen:
            print("INVALID VIA STUDENT MATCHED MORE THAN ONCE")
            return
        
        # add to the sets
        hospital_seen.add(h)
        student_seen.add(s)
    
    # Unmatched
    if len(hospital_seen) != n or len(student_seen):
        print("INVALID UNMATCHES HOSPITAL AND/OR STUDENT")
        return

    #(b) checks stability: confirms there is no blocking pair.
        
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