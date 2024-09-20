#
# Code written for course Google Cibersecurity Professional Certified
#

# Define the function to update the IP addresses file
def update_file(import_file, remove_list):
    
    # Step 1: Open the file and read the contents
    with open(import_file, "r") as file:
        ip_addresses = file.read()

    # Step 2: Convert the string of IP addresses into a list
    ip_addresses = ip_addresses.split()

    # Step 3: Iterate through the remove_list
    for element in remove_list:

        # Step 4: Remove IP addresses that are in both ip_addresses and remove_list
        if element in ip_addresses:
            ip_addresses.remove(element)

    # Step 5: Convert the list back into a string with each IP on a new line
    ip_addresses = "\n".join(ip_addresses)

    # Step 6: Write the updated list back to the file
    with open(import_file, "w") as file:
        file.write(ip_addresses)

# Sample usage of the function

# List of IP addresses to be removed
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# The name of the file containing the allow list
import_file = "allow_list.txt"

# Call the function to update the allow list
update_file(import_file, remove_list)

# Verify by reading and printing the updated content
with open(import_file, "r") as file:
    updated_content = file.read()
    print(updated_content)
