def main():
    students = ["Alice", "Bob", "Carol", "Dave", "Eve"]
    print(len(students)) 
    print(len(students[2]))
    for s in students:
       for c in s:
            print(c)

    afc = [["Colts", "Titans", "Jaguars", "Texans"],
           ["Patriots", "Jets", "Dolphins", "Bills"],
           ["Steelers", "Bengals", "Ravens", "Browns"],
           ["Broncos", "Chargers", "Cheifs", "Raiders"]]
    print(afc)

main()