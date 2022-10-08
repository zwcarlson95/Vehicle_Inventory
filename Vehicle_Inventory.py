


class Automobile:

    inventory_list = []

    def __init__(self):
        self._make = ''
        self._model = ''
        self._color = ''
        self._year = 0
        self._mileage = 0
        self.vehicle_dict = {}


    def add_vehicle(self):
        self._make = input("Enter make: ").title()
        self._model = input("Enter model: ").title()
        self._color = input("Enter color: ").title()
        self._year = int(input("Enter year: "))
        self._mileage = int(input("Enter mileage: "))

        self.create_dict()
        
    def create_dict(self):       
        self.vehicle_dict = {
            'Make': self._make,
            'Model': self._model,
            'Color': self._color,
            'Year': self._year,
            'Mileage': self._mileage
            }
        
        self.create_list()

    def create_list(self):        
        Automobile.inventory_list.append(self.vehicle_dict)


    def delete_entry(self):
        pos = int(input('Enter the inventory position of the vehicle you want to remove: '))
        if (pos <= 0) or (pos > len(Automobile.inventory_list)):
            print('!!INVALID POSITION!!')
            return self.delete_entry()
            
        Automobile.inventory_list.pop(pos - 1)   
        print('Vehicle successfully removed')


    def edit_entry(self):
        pos = int(input('Enter the inventory position of the vehicle you want to edit: '))
        if (pos <= 0) or (pos > len(Automobile.inventory_list)):
            print('!!INVALID POSITION!!')
            return self.edit_entry()
            
        key = input('Enter the key for the value you want to edit: ').title()
        if key not in self.vehicle_dict:
            print('!!INVALID KEY!!')
            return self.edit_entry()
            
        new_val = input('Enter the new value: ').title()
        Automobile.inventory_list[pos - 1][key] = new_val
        print('Entry edited successfully')
        



user = True

while user == True:
    print ("""
    - Enter [1] to Add a Vehicle
    - Enter [2] to Delete a Vehicle
    - Enter [3] to View Inventory
    - Enter [4] to Edit Inventory
    - Enter [5] to Export Inventory
    - Enter [6] to Quit
    """)
    
    user_entry = input("Enter Action: ")
    
    if user_entry == '1':
        inventory = Automobile()
        inventory.add_vehicle()

    elif user_entry == '2':
        inventory.delete_entry()

    elif user_entry == '3':
        print(inventory.inventory_list)
        
    elif user_entry == '4':
        inventory.edit_entry()
        
    elif user_entry == '5':
        f = open('vehicle_inv.txt', 'w')
        f.write(str(inventory.inventory_list))
        f.close()
        print('Export successful')

    elif user_entry == '6':
        print('Goodbye')
        break
        
    else:
        print('Invalid Entry')



        

