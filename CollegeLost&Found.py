def load_items():
    found_items = {}

    try:
        f = open("found_items.txt", "r")

        for line in f:
            data = line.strip().split("|")

            if len(data) == 3:
                found_items[data[0]] = {
                    "colour": data[1],
                    "location": data[2]
                }

        f.close()

    except:
        f = open("found_items.txt", "w")
        f.close()

    return found_items


def save_items(found_items):
    f = open("found_items.txt", "w")

    for item in found_items:
        f.write(item + "|" + found_items[item]["colour"] + "|" +
                found_items[item]["location"] + "\n")

    f.close()


found_items = load_items()

print("\n     COLLEGE LOST AND FOUND     ")
print("1. I Lost Something")
print("2. I Found Something")
print("3. Show Found Items")
print("4. Exit")

choice = input("Enter your choice: ")

if choice == "1":

    item = input("Enter lost item: ").lower()
    colour = input("Enter colour: ").lower()
    location = input("Enter where you lost it: ").lower()

    match = False
    exact_item = None

    print("\nPossible matches:")

    for name in found_items:

        score = 0

        if name == item:
            score = score + 1

        if found_items[name]["colour"] == colour:
            score = score + 1

        if found_items[name]["location"] == location:
            score = score + 1

        if score >= 2:
            match = True

            print("\nItem:", name)
            print("Colour:", found_items[name]["colour"])
            print("Location:", found_items[name]["location"])
            print("Match:", score, "/ 3")

            if score == 3:
                exact_item = name

    if exact_item != None:
        del found_items[exact_item]
        save_items(found_items)
        print("\nExact match found.")
        print("Item removed from found items.")

    if match == False:
        print("No possible match found.")


elif choice == "2":

    print("\n     REPORT FOUND ITEM     ")

    item = input("Enter item name: ").lower()
    colour = input("Enter colour: ").lower()
    location = input("Enter where you found it: ").lower()

    found_items[item] = {
        "colour": colour,
        "location": location
    }

    save_items(found_items)

    print("Item added successfully.")


elif choice == "3":

    print("\n     FOUND ITEMS      ")

    if len(found_items) == 0:
        print("No items found.")

    else:
        for item in found_items:
            print("\nItem:", item)
            print("Colour:", found_items[item]["colour"])
            print("Location:", found_items[item]["location"])


elif choice == "4":
    print("Thank you for using the system.")


else:
    print("Invalid choice.")