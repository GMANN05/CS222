people = int(input("Enter the amount of people coming: "))
dogs = int(input("Enter the amount of hotdogs per person: "))
 
total = (people * dogs)
packs = ((total +9) // 10)
buns = ((total +7) // 8)
leftoverDogs = ((packs * 10) - total)
leftoverBuns = ((buns * 8) - total)

print("You will need " + str(packs) + " packs of hotdogs.")
print("You will need " + str(buns) + " pack of hotdog buns.")
print("You will have " + str(leftoverDogs) + " hotdogs left over. ")
print("You will have " + str(leftoverBuns) + " buns left over.")

