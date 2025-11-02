import csv
import os

FILENAME = 'contacts.csv'
datas = ['Name','Number','Email']
if not os.path.exists(FILENAME):
        with open(FILENAME,'w',newline='',encoding='utf-8') as f:
            csv.writer(f).writerow(datas)

def add_contact(name,number,email):
    data = [name,number,email]
    with open(FILENAME,'a',newline='',encoding='utf-8') as f:
        csv.writer(f).writerow(data)

def view_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME,'r',encoding='utf-8',newline='') as f:
                
            reader = csv.reader(f)
            try:
                header = next(reader)
                first_data_row = next(reader)
            except Exception:
                print("No contacts saved.")
            
        with open(FILENAME,'r',encoding='utf-8',newline='') as f:
            print()
            for i,item in enumerate(list(csv.DictReader(f))):
                print(f"{i+1}: {item['Name']}  ||  {item['Number']}  ||  {item['Email']}")
            print()
                


def search_contact(name):
    with open(FILENAME,'r',encoding='utf-8',newline='') as f:
        print()
        for i in csv.DictReader(f):
            if i['Name'].lower() == name.lower():
                print("Contact found")
                print(i['Name'],'  ||  ',i['Number'],'  ||  ',i['Email']) 
        print()

def delete_contact(name):
    row_to_keep = []
    with open(FILENAME,'r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        row_to_keep.append(header)

        for row in reader:
            if row[0].lower() != name.lower():
                row_to_keep.append(row)
            else:
                print(f"\nDeleting row: {row} ...")
    with open(FILENAME,'w',encoding='utf-8',newline='') as f:
        csv.writer(f).writerows(row_to_keep)

    print(f"\nFile {FILENAME} updated. {name} removed.")

def update_contact(name,number,email):
    rows = []
    with open(FILENAME,'r',encoding='utf-8',newline='') as f:
        reader = csv.reader(f)
        header = next(reader)
        rows.append(header)
        
        for i in reader:
            if i[0].lower() == name.lower():
                i[1] = number
                i[2] = email
                rows.append(i)
            else:
                rows.append(i)
    with open(FILENAME,'w',encoding='utf-8',newline='') as f:
        csv.writer(f).writerows(rows)
    print("\nContact updated.\n")


print('*'*15+'Contact book'+'*'*15)
while True:
    print("1. Add a new contact")
    print("2. View all contacts")
    print("3. Search for a contact by name")
    print("4. Delete a contact by name")
    print("5. Update a contact by name")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    match choice:
        case '1':
            name = input("Enter the name: ")
            number = input("Enter the number: ")
            email = input("Enter the email: ")
            add_contact(name,number,email)
        case '2':
            view_contacts()
        case '3':
            name = input("Enter the name to be searched: ")
            search_contact(name)
        case '4':
            name = input("Enter the name to be deleted: ")
            delete_contact(name)
        case '5':
            name = input("Enter the name to be updated: ")
            number = input("Enter the number: ")
            email = input("Enter the email: ")
            update_contact(name,number,email)
        case '6':
            print("Thanks for using our software😉😉")
            exit(0)
        case _:
            print("Invalid choice. Try again")
            continue