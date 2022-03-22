import sys

if __name__ == "__main__":
    print(f"There are {len(sys.argv)} arguments and the first one is {sys.argv[0]}")
    with open(sys.argv[1]) as input:
        for line in input:
            print(f"{line.strip()}")