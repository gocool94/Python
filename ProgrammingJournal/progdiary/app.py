from database import add_entry,get_entry, create_table

menu = """Please select your following options:

1) Add new entry for today
2) view entries
3) Exit.

Your selection: 

"""

welcome = "Welcome to the programming diary..!"

create_table()


def prompt_new_entry():
    entry_content = input("What have you learned.?..")
    entry_date = input("Enter the date")
    add_entry(entry_content, entry_date)

def view_entry(entrie):
    for individual_entry in entrie:
        print(f"{individual_entry[1]} \n \n {individual_entry[0]}")


# user_input = input(menu)

while (user_input := input(menu)) != "3":
    # do the stuff here

    if user_input == "1":
        prompt_new_entry()
        print("Adding..............................!")
    elif user_input == "2":
        entrie = get_entry()
        view_entry(entrie)


        print("View")
    else:
        print("Ivalid option..!")
