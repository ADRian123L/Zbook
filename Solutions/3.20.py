# 3.20.py Author: Adrian

# The pogram outputs the provided services and then promps for two of them.

# Services:
services = {
    "Oil change" : 35,
    "Tire rotation" : 19,
    "Car wash" : 7,
    "Car wax" : 12,
    "-" : 0
}

# Outputs the services:
print("Davy's auto shop services")
count = 0
for key, value in services.items():
    if (count == 4):
        break
    print(F"{key} -- ${value}")
    count += 1


# Promps for the two services:
print()
first_serv = input("Select first service:\n")
second_serv = input("Select second service:\n")
serv_1, serv_2 = first_serv, second_serv

# Checks for '-' input:
if (first_serv == "-"):
    serv_1 = "No service"
if (second_serv == "-"):
    serv_2 = "No service"

# Outputs the selected services and their prices:
if first_serv in services.keys():
    print(f"Service 1: {serv_1}, ${services[first_serv]}")

if second_serv in services.keys():
    print(f"Service 2: {serv_2}, ${services[second_serv]}")

# Prints the total cost:
total = services[first_serv] + services[second_serv]
print(f"Total: ${total}")

