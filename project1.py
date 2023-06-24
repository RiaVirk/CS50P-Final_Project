# Import required modules
import sys
import csv
import tabulate


def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("CSV file is not readable")
    
    output = []
    for row in data:
        house = select_house(row["characteristic"])
        grade = select_grade(row["birthdate"])
        output.append({"name": row["name"], "house": house, "grade": grade})
    
    print(output)
    
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house", "grade"])
        writer.writerow({"name": "name", "house": "name", "grade": "name"})
        for row in output:
            writer.writerow({"name": row["name"], "house": row["house"], "grade": row["grade"]})

    with open(sys.argv[2]) as file:
        reader = csv.reader(file)
        headers = ["name", "house", "grade"]
        print(tabulate.tabulate(reader, headers, tablefmt="grid"))


def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv) > 3:  
        sys.exit("Too many command-line arguments")
    
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")

def select_house(char):
    if char in ["courage", "loyalty", "adventure"]:
        return "Gryffindor"
    elif char in ["dedication", "patience", "honesty"]:
        return "Hufflepuff"
    elif char in ["wisdom", "creativity", "perfectionism"]:
        return "Ravenclaw"
    elif char in ["ambition", "competitive", "leadership"]:
        return "Slytherin"
    else:
        return "No House"



def select_grade(year):
    age = 2022 - int(year)
    grade = age - 5
    return "Grade-" + str(grade) 
    


if __name__ == "__main__":
    main() 