print("✅ Python app.py is running from Jenkins pipeline!")
from flask import Flask, jsonify
import sys

app = Flask(__name__)
DATA_FILE = "data.txt"

def read_data():
    try:
        with open(DATA_FILE, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return ["data.txt not found"]

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data')
def get_data():
    lines = read_data()
    return jsonify(lines)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # No arguments: run the web app
        app.run(host="0.0.0.0", port=5000)
    elif sys.argv[1] == "--show":
        print("Reading file:")
        for line in read_data():
            print(line.strip())
    elif sys.argv[1] == "--count":
        print("Line count:", len(read_data()))
    else:
        print("Unknown command")
        print("Usage:")
        print("  python3 app.py            # Run Flask web server")
        print("  python3 app.py --show     # Print file contents")
        print("  python3 app.py --count    # Count lines in file")


