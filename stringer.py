import sys

def print_usage():
    print("Usage:")
    print("stringer.py 1 <file> <string_to_count>")
    print("            2 <file> <string_to_remove>")

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "-h":
        print_usage()
        exit(1)

    with open(sys.argv[1]) as input:
        for line in input:
            print(f"{line.strip()}")