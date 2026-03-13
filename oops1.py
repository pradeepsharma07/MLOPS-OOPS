# Initiate a class
class employee:
    #Special method.magic method/dunder method - constructor
    def __init__(self):
        print(id(self))
        #print("Started Executing the constructor")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        #print("Attributes/Data have been initialized")

    def travel(self,destination):
        print("This function was called manually")
        print(f"Employee is travelling to {destination}")

# Create an object/Instance of the class
sam = employee()
#sam.name = "Sam Kumar"
# print(id(sam)) 
print(sam.name)

# sundar = employee()
# print(id(sundar))

#print(sam.salary)
#sam.travel("Bangalore")
# print(type(sam))