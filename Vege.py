import sys
import csv
import tabulate


def main():
    check_correct_args()
    # fruit = input("Fruit: ")
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("CSV file is not readable")
    
    # print(f"Data: {data}")
    
    output = []
    for row in data:
        type = select_type(row["type"])
        grade = select_grade(row["calories"])
        output.append({"name": row["name"],"calories": row["calories"], "season": row["season"], "seeds": row["seeds"], "req peel": row["req peel"], "type": type, "Diet": grade})
    # , "season": row["season"], "seeds": row["seeds"], "peel": row["peel"], "type": type, "diet": grade
    # print(f"Output: {output}")
    # name,calories,season,seeds,req peel,type

    Question = input("You want to see Total List of fruits (Press 1) OR any 1 fruit of your choice? (press 2)? ")

    if Question == "2":
        fruit = input("Name: ")
        nlist = []
        for d in output:
            if d['name'] == fruit:
                nlist.append(d)
        print("The filtered list is")
        # print(nlist)
        reader = nlist
        print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))


                                            #     res = {}
                                            #     # printing original list
                                            #     print("The original list is : " + str(output))
                                            
                                            #     for i in output:
                                            #         for j in i:
                                            #             if j in res.keys():
                                            #                 res[j].append(i[j])
                                            #             else:
                                            #                 res[j] = [i[j]]
                                            
                                            # # printing result
                                            #     print("The values corresponding to key : " + str(res))

# # Initializing key
#     value:1 = fruit
 
# # Using for loop to extract dictionaries with given key
#     result = []
#     for sub_dict in output:
#         if value in sub_dict:
#             result.append(sub_dict)
 
# # Printing result
#     print("The filtered dictionaries: ", result)

# res = {}
 
# initializing list

    else:
        with open(sys.argv[2], "w") as file:
            writer = csv.DictWriter(file, fieldnames=["name", "calories", "season", "seeds", "req peel", "type", "grade"])
            writer.writerow({"name": "name","calories": "calories","season": "season","seeds": "seeds", "req peel": "req peel", "type": "type", "grade": "Diet"})
            for row in output:
                writer.writerow({"name": row["name"], "calories": row["calories"], "season": row["season"], "seeds": row["seeds"], "req peel": row["req peel"], "type": row["type"], "grade": row["Diet"]})

            # , "grade": row["grade"]

        with open(sys.argv[2]) as file:
            reader = csv.DictReader(file)

            print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))


def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv) > 3:  
        sys.exit("Too many command-line arguments")
    
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV files")

def select_type(char):
    if char in ["one seed"]:
        return "Drupes"
    elif char in ["berry"]:
        return "Berries"
    elif char in ["seeds"]:
        return "Pomes"
    elif char in ["juicy"]:
        return "Citrus"
    elif char in ["melon"]:
        return "Pepo"
    elif char in ["exotic"]:
        return "Tropical"
    else:
        return "Not Fruit"



def select_grade(calo):
    portion = 2.5 * int(calo)
    if portion > 125:
        # print( "Not Good for Salad")
        return "Not Good for Salad"
    else:
        # print( "Good for Salad")
        return "Good for Salad"

if __name__ == "__main__":
    main() 