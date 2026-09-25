"""Marks Tool - print a short report for a list of marks."""
from config import load_env
from stats import average, highest, lowest
Marks = [72, 65, 88, 91, 54]
def main():
    settings = load_env()
    print(settings["APP_NAME"])
    print("count :", len(Marks))
    print("Average:", average(Marks))
    print("Highest:", highest(Marks))
    print("lowest:", lowest(Marks))
if __name__ == "__main__":
    main() 
