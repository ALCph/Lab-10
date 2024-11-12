# 1.) The pet class
# The class
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
        
    def set_name(self, name):
        self.__name = name
    
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
        
    def set_age(self, age):
        self.__age = age
        
    def get_name(self):
        return self.__name
        
    def get_animal_type(self):
        return self.__animal_type
        
    def get_age(self):
        return self.__age

# The program
import pet

# User input
name = input('Enter the pet name: ')
animal_type = input('Enter the type of animal: ')
age = input('How old is the pet: ')
# Printing the output
my_pet = Pet(name, animal_type, age)
print('Pet name:', my_pet.get_name())
print('Pet type:', my_pet.get_animal_type())
print('Pet age:', my_pet.get_age())
#=======================================================

# 2.) Car class
# The class
class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
        
    def accelerate(self):
        self.__speed += 5
    
    def brake(self):
        self.__speed -= 5
    
    def get_speed(self):
        return self.__speed

# The program
import car
my_car = Car(1996, 'Toyota')
# Speed loops and printing output
for i in range(5):
    my_car.accelerate()
    print(f"Accelerating the car. Current speed: {my_car.get_speed()} mph")
for i in range(5):
    my_car.brake()
    print(f"Hiting the brakes. Current speed: {my_car.get_speed()} mph")
#=======================================================

# 3.) Personal information class
# The class
class TMI:
    def __init__(self, name, address, age, phone):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
# Getting the info
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone
# Setting the info
    def set_name(self, name):
        self.__name = name
    def set_address(self, address):
        self.__address = address
    def set_age(self, age):
        self.__age = age
    def set_phone(self, phone):
        self.__phone = phone
# Sample people info
person1 = TMI('Freddy', 'Elm street', '42', '555-1111')
person2 = TMI('Jason', 'Crystal lake', '11', '555-2222')
person3 = TMI('Micheal', 'Lampkin lane', '31', '555-3333')
# Printing the output
print("Person 1 - Name:", person1.get_name(), 
"\nAddress:", person1.get_address(), 
"\nAge:", person1.get_age(), 
"\nPhone Number:", person1.get_phone())
print()

print("Person 2 - Name:", person2.get_name(), 
"\nAddress:", person2.get_address(), 
"\nAge:", person2.get_age(), 
"\nPhone Number:", person2.get_phone())
print()

print("Person 3 - Name:", person3.get_name(), 
"\nAddress:", person3.get_address(), 
"\nAge:", person3.get_age(), 
"\nPhone Number:", person3.get_phone())
#=======================================================

# 4.) Employee class
# The class
class Employee:
    def __init__(self, name, ID, department, job_title):
        self.name = name
        self.ID = ID
        self.department = department
        self.job_title = job_title

# The employees
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Printing lots of output
print("Employee 1:")
print("Name:", employee1.name)
print("ID Number:", employee1.ID)
print("Department:", employee1.department)
print("Job Title:", employee1.job_title)
print() # empty statement for a space between the printed names.
# was not sure if I should have done this or tried some \n tricks

print("Employee 2:")
print("Name:", employee2.name)
print("ID Number:", employee2.ID)
print("Department:", employee2.department)
print("Job Title:", employee2.job_title)
print()

print("Employee 3:")
print("Name:", employee3.name)
print("ID Number:", employee3.ID)
print("Department:", employee3.department)
print("Job Title:", employee3.job_title)
#=======================================================

# 5.) Retail item class
# A problem similar to #4, and so I reused some code
# The class
class Retailitem:
    def __init__(self, Description, Units, Price):
        self.Description = Description
        self.Units = Units
        self.Price = Price

# The Items
item1 = Retailitem("Jacket", 12, 59.95)
item2 = Retailitem("Designer Jeans", 40, 34.95)
item3 = Retailitem("Shirt", 20, 24.95)

# Printing lots of output
print("Item 1:")
print("Description:", item1.Description)
print("Units Number:", item1.Units)
print("Price:", item1.Price)
print()

print("Item 2:")
print("Description:", item2.Description)
print("Units Number:", item2.Units)
print("Price:", item2.Price)
print()

print("Item 3:")
print("Description:", item3.Description)
print("Units Number:", item3.Units)
print("Price:", item3.Price)
#=======================================================

# 6.) Patient Charges
# The Patient class
class Patient:
    def __init__(self, first_name, middle_name, 
                 last_name, address, city, state, 
                 ZIP, user_phone, emer_name, emer_phone):
# Lots of self 
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.ZIP = ZIP
        self.user_phone = user_phone
        self.emer_name =emer_name
        self.emer_phone = emer_phone    
# Setting the name
    def set_first(self, first_name):
        self.first_name = first_name
    def set_middle(self, middle_name):
        self.middle_name = middle_name
    def set_last(self, last_name):
        self.last_name = last_name
# Setting the address
    def set_address(self, address): 
        self.address = address 
    def set_city(self, city): 
        self.city = city 
    def set_state(self, state): 
        self.state = state 
    def set_ZIP(self, ZIP): 
        self.ZIP = ZIP
# Setting the phone numbers
    def set_user_phone(self, user_phone): 
        self.user_phone = user_phone 
    def set_emer_name(self, emer_name): 
        self.emer_name = emer_name 
    def set_emer_phone(self, emer_phone): 
            self.emer_phone = emer_phone

# Returning the full name
    def get_first_name(self):
        return self.first_name
    def get_middle_name(self):
        return self.middle_name
    def get_last_name(self):
        return self.last_name
# Returning the full address
    def get_address(self):
        return self.address
    def get_city(self):
        return self.city
    def get_state(self):
        return self.state
    def get_ZIP(self):
        return self.ZIP
# Returning the phone numbers
    def get_user_phone(self):
        return self.user_phone
    def get_emer_name(self):
        return self.emer_name
    def get_emer_phone(self):
        return self.emer_phone

# The other class
class Procedure:
    def __init__(self, name, date, practioner, charges):
        self.name = name
        self.date = date
        self.practioner = practioner
        self.charges = charges

# Setting procedure values
    def set_name(self, name):
        self.name = name
    def set_date(self, date):
        self.date = date
    def set_practioner(self, practioner):
        self.practioner = practioner
    def set_charges(self, charges):
        self.charges = charges
# Returning procedure values
    def get_name(self):
        return self.name
    def get_date(self):
        return self.date
    def get_practioner(self):
        return self.practioner
    def get_charges(self):
        return self.charges

# Sample patient
patient = Patient("This", "Problem", "Toolong", "1111 Pearson Street",
                  "Revel", "CA", "90210", 
                  "555-111-2222", "Mr. Send help", "911-111-1111")

# Procedure data
procedure1 = Procedure("Physical Exam", "11-06-2024", "Dr. Irvine", 250.00)
procedure2 = Procedure("X-ray", "11-06-2024", "Dr. Jamison", 500.00)
procedure3 = Procedure("Blood Test", "11-06-2024", "Dr. Smith", 200.00)

# Printing patient info
print("Patient Information:")
print("Name:", patient.get_first_name(), patient.get_middle_name(), patient.get_last_name())
print("Address:", patient.get_address(), patient.get_city(), patient.get_state(), patient.get_ZIP())
print("Phone Number:", patient.get_user_phone())
print("Emergency Contact:", patient.get_emer_name())
print("Emergency Contact Phone:", patient.get_emer_phone())
print()

# Printing procedure info
total_charges = 0
for procedure in [procedure1, procedure2, procedure3]:
    print("Procedure Information:")
    print("Procedure Name:", procedure.get_name())
    print("Date:", procedure.get_date())
    print("practioner:", procedure.get_practioner())
    print("Charges:", procedure.get_charges())
    print()
    total_charges += procedure.get_charges()

# Display total charges
print("Total for all Procedures:", total_charges)