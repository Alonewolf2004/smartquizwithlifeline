num = int(input("Enter the number of names you want to input: "))

name_list = []  # Initialize an empty list to store the names

for j in range(num):
    name = input("\nEnter name: ")
    name_list.append(name)  # Append each name to the list

    if name == "shambu":
        print("Good")

    for i in name:
        print(i)
