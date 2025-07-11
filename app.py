import sys

DATA_FILE = "data.txt"

def read_file():
    """Reads lines from the file and returns them as a list."""
    try:
        with open(DATA_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["[ERROR] File not found: data.txt"]

def show_file():
    """Prints the contents of the file."""
    lines = read_file()
    for line in lines:
        print(line.strip())

def count_lines():
    """Prints number of lines in the file."""
    lines = read_file()
    print(f"Line count: {len(lines)}")

def help_message():
    print("Usage:")
    print("  python3 app.py --show     # Show file contents")
    print("  python3 app.py --count    # Show line count")
    print("  python3 app.py            # Default action")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("No command given. Showing help:")
        help_message()
    elif sys.argv[1] == "--show":
        show_file()
    elif sys.argv[1] == "--count":
        count_lines()
    else:
        print(f"Unknown argument: {sys.argv[1]}")
        help_message()
