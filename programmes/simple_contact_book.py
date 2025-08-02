# # Simple Contact Book
#
# contacts ={}
# while True:
#     name = input("Enter name(or '0' to quit):")
#     if name == '0':
#         break
#     phone = input("Enter phone number:")
#     contacts[name] = phone
#     print("Contacts:", contacts)
# Simple Contact Book
contacts = {}

while True:
    name = input("Enter name (or '0' to quit): ")
    if name == '0':
        break
    phone = input("Enter phone number: ")
    contacts[name] = phone

    print("Contacts: {")
    for key, value in contacts.items():
        print(f" '{key}': '{value}',")
    print("}")
