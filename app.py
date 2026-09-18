"""Marks Tppl - print a short report for a list of marks."""
from config import load_env
from stats import average, highest
Marks = [72, 65, 88, 91, 54]
def main():
    settings = load_env{}
    print(settings[App_NAME"])
    print("count :", len(Marks))
    print("Average:", average(Marks))
    print("Highest:",highest(Marks))
if__name__=="__main__":
   main() 
