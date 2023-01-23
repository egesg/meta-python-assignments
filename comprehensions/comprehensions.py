employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp


# Modifies the employee list of dictionaries into list of employee-department strings
def to_mod_list(employee_list):
   map_emp = list(map(mod, employee_list))
   return list(map_emp)


# Generates a list of usernames 
def generate_usernames(mod_list):
   my_list = [ x.replace(" ", "_") for x in mod_list ]
   return my_list


# Maps employee id to first initial
def map_id_to_initial(employee_list):
   
   def get_id(employee_list): 
      emp_id = employee_list['id']
      return emp_id

   def get_initial(employee_list):
      emp_initial = employee_list['name'][0]
      return emp_initial
   
   id = list(map(get_id, employee_list))
   initial = list(map(get_initial, employee_list))
   
   # dictionary comprehension using two lists
   emp_dict = { initial[i] : id[i] for i in range(len(initial)) }
   return emp_dict


def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")
   # Modified employee list: ['John_Kitchen', 'Paul_House Floor', 'Sarah_Management', 'Lisa_Cold Storage', 'Ryan_Inventory Mgmt', 'Gill_Cashier']

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")
   # List of usernames: ['John_Kitchen', 'Paul_House_Floor', 'Sarah_Management', 'Lisa_Cold_Storage', 'Ryan_Inventory_Mgmt', 'Gill_Cashier']

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")
   # Initials and ids: {'J': 12345, 'P': 12456, 'S': 12478, 'L': 12434, 'R': 12483, 'G': 12419}

if __name__ == "__main__":
   main()