# BioNumbers - Biological Numbers Information

bionumbers = {
    1: ("Human cell diameter", "10-30 micrometers"),
    2: ("RBC diameter", "7-8 micrometers"),
    3: ("DNA diameter", "2 nanometers"),
    4: ("Cell membrane thickness", "7-10 nanometers"),
    5: ("Human genome size", "Approximately 3.2 billion base pairs")
}

print("===== BioNumbers =====")
print("Important Numbers in Biology\n")

for number, data in bionumbers.items():
    print(number, ".", data[0], ":", data[1])

choice = int(input("\nEnter the number you want to know more about: "))

if choice in bionumbers:
    print("\nSelected:")
    print("Quantity:", bionumbers[choice][0])
    print("Value:", bionumbers[choice][1])
else:
    print("Invalid choice!")
