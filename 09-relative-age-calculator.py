age = input("Enter animal age (in years): ")
while age.isnumeric() == False:
    age = input("Invalid Input. Enter animal age: ")

type = input("Enter 'd' for dog, 'c' for cat or 'e' for elephantEnter the type of animal: ")
while type not in ["d", "c", "e", "dog", "cat", "elephant"]:
    type = input("Invalid Input. Enter animal type: ")

if type in ["d", "dog"]:
    print(f"Equivalent human age: {7*age}")
elif type in ["c", "cat"]:
    print(f"Equivalent human age: {6*age}")
elif type in ["e", "elephant"]:
    print(f"Equivalent human age: {3*age}")
