# Initiate a class
class employee:
    #Special method.magic method/dunder method - constructor
    def __init__(self):
        print("Started Executing the constructor")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes/Data have been initialized")


    def travel(self,destination):
        print("This function was called manually")
        print(f"Employee is travelling to {destination}")

# Create an object/Instance of the class
sam = employee()

#print(sam.salary)
sam.travel("Bangalore")

print(type(sam))