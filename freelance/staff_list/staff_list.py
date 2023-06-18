# menu
print("----------MENU----------\n")
print("1-Add Staff\n")
print("2-Search Staff\n")
print("3-List Staff\n")
print("----------Other Keys Exit----------\n")

# create staff list
staff_list = []

# staff adding function
def add_staff():
    print("----1-Add Staff----\n")
    name = input("Name: ").lower()
    surname = input("Surname: ").lower()
    address = input("Address: ").lower()
    phone = input("Phone: ").lower()
    new_staff = {}
    new_staff["Name"] = name
    new_staff["Surname"] = surname
    new_staff["Address"] = address
    new_staff["Phone"] = phone
    staff_list.append(new_staff)
    
    print("Added 1 staff record.\n")

# staff searching function
def search_staff():
    print("----2-Search Personnel----\n")
    search = input("Name Surname: ").lower()
    search_tokens = search.split()
    found_records = []
    for staff in staff_list:
        if staff["Name"] == search_tokens[0] and staff["Surname"] == search_tokens[1]:
            found_records.append(staff)
    if len(found_records) > 0:
        print("----Found Records----\n")
        for record in found_records:
            print(f"Name: {record['Name']}")
            print(f"Surname: {record['Surname']}")
            print(f"Address: {record['Address']}")
            print(f"Phone: {record['Phone']}")
            print(f"{len(found_records)} record found.\n")
            
    else:
        print("No records found.")

# staff listing function
def list_staff():
    print("----3-List Staff----\n")
    if len(staff_list) > 0:
        headers = ["Name", "Surname", "Address", "Phone"]
        formatted_headers = [f"{header:<15}" for header in headers]  # alignment setting
        lines = ["-" * 15] * len(headers)
        formatted_lines = [f"{line:<15}" for line in lines]  # alignment setting
        print("\t".join(formatted_headers))
        print("\t".join(formatted_lines))
        for staff in staff_list:
            values = [staff["Name"], staff["Surname"], staff["Address"], staff["Phone"]]
            formatted_values = [f"{value:<15}" for value in values]  # alignment setting
            print("\t".join(formatted_values))
        print()
    else:
        print("No staff records found.")

continues = False
while not continues:
    choice = input("Your Choice: ")

    if choice == "1":
        add_staff()
    elif choice == "2":
        search_staff()
    elif choice == "3":
        list_staff()
    else:
        continues = True