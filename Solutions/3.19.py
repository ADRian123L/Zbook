# 3.29.py  Author: Adrian
 
# The program promps the user for information and outputs an appropiate answer.

# Promps for the type of service:
auto_service = input("Enter desired auto service:\n")

# Creates a dictionary for storing the service's cost:
services = {

	"Oil change" : "$35",
	"Tire rotation" : "$19",
	"Car wash" : "$7"
}

# Prints the input:
print(f"You entered: {auto_service}")

# Checks if the input exists and if it does it outputs the cost:
if (auto_service in services.keys()): 

	for key, cost in services.items():
		if (auto_service == key):
			print(f"Cost of {key.lower()}: {cost}")
			break
else:
	print("Error: Requested service is not recognized")