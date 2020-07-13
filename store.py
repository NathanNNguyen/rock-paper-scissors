class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def print_welcome(self):
        print(f'Welcome to {self.name}! Which department would you like to visit?')

        for d in self.departments:
            print(d)

class Department:
    def __init__(self, id, name, products):
        self.id = id
        self.name = name
        self.products = products

    def __str__(self):
        return f"{self.id}: {self.name}"

store = Store("The Dugout", [
    Department(1, 'BaseBall', []),
    Department(2, 'Basketball', []),
    Department(3, 'Football', []),
    Department(4, 'Golf', [])
])
# loop forever while the user is browsing through departments
# use the `input` function to prompt user to select a department to browse

while True:
    # print a message for the Store    
    store.print_welcome()

    # get the department number user return to visit:
    selection = input('Which department would you like to visit? ')

    # if the user types "quit", exit the program

    if selection == "quit":
        exit()

    chosen_department = store.departments[int(selection - 1)]

    print(f'You selected the {chosen_department.name} \n')