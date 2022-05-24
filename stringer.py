import sys
import os

def print_usage():
    print("Usage:")
    print("stringer.py 1 <file> <string_to_count>")
    print("            2 <file> <string_to_remove>")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        print_usage()
        exit(1)

    if (sys.argv[1] == '1'):
        print(f"Counting '{sys.argv[3]}' in {os.path.join(os.getcwd(), sys.argv[2])}")

        occurrences = 0
        with open(sys.argv[2]) as input_file:
            for line in input_file:
                if line.find(sys.argv[3]) != -1:
                    occurrences += 1

        print(f"There are {occurrences} occurrences")
