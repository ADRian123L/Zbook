# 3.20.py Author: Adrian

# The pogram outputs the provided services and then promps for two of them.

# Services:
services = {
    "Oil change" : 35,
    "Tire rotation" : 19,
    "Car wash" : 7,
    "Car wax" : 12,
    "-" : ""
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
print()

# Checks for '-' input:
if (first_serv == "-"):
    serv_1 = "No service"
if (second_serv == "-"):
    serv_2 = "No service"

# Outputs the selected services and their prices:
print("Davy's auto shop invoice")
print()
# Checks whether to change the formatting:
content_1 = ((", $" + str(services[first_serv])) if (first_serv != "-") else "")
content_2 = ((", $" + str(services[second_serv])) if (second_serv != "-") else "")
if first_serv in services.keys():
    print(f"Service 1: {serv_1}{content_1}")
if second_serv in services.keys():
    print(f"Service 2: {serv_2}{content_2}")

# Prints the total cost:
print()
# Checks whether the values are not integers:
total = (services[first_serv] if (first_serv != "-") else 0) \
      + (services[second_serv] if (second_serv != "-") else 0)
# Outputs the result:
print(f"Total: ${total}")