with open (USA_cars_dataset.csv) as file:
    file.readline()
    
class Car:

    def __init__(self, manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, interiorcolor, exteriorcolor, accident, price, orientation = None):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.mileage = mileage
        self.engine = engine
        self.transmission = transmission
        self.drivetrain = drivetrain
        self.mpg = mpg
        self.exteriorcolor = exteriorcolor
        self.interiorcolor = interiorcolor
        self.accident = accident 
        self.price = price
    
def Paint(self):
    exteriorcolor1 = input("enter exterior color")
    
    #change the exterior color of the car
    
    if (exteriorcolor1 == 'black'):
        newexteriorcolor = input("enter new exterior color")
        print("the new exterior color is", newexteriorcolor)
    
def Repair(self):
    replace = input("insert part that is being replaced")
    replace2 = input("insert the name of the replacement part")
    
    #change the corresponding attribute
    
    if (replace == 'brakes'):
        newreplace = input("enter changed attribute")
        print("the changed attribute is", newreplace)
        
    if (replace2 == 'brake pads'):
        newreplace2 = input("enter changed attribute")
        print("the changed attribute is", newreplace2)


def Reupholster(self):
    interiorcolor1 = input("enter interior color")
    
    #change the interior color of the car
    
    if (interiorcolor1 == 'beige'):
        newinteriorcolor = input("enter new interior color")
        print("the new interior color is", newinteriorcolor)
    
def Drive(self):
    number = input("enter mileage")
    
    #increase mileage by inputted amount 
    
    mileage = mileage + number
    print("the new mileage is", mileage)
    
def ModifyPrice(self):
    price = input("enter price")
    
    #change price to new number
    #if the # is <1, discount the car cost by that amount, print new amount
    #and ask to confirm if the new amount is correct
    
    if (price == '15000'):
        newprice = input("enter new price")
        print("the new price is", newprice)
        
    if (newprice < 1):
        price - newprice = discount
        newprice - discount = total
        print("the new amount is", total )
        
        total = input("is the new amount correct?")
        if (total == "yes"):
            print("glad it is correct!")

    
class Seller:
    
    def __init__(self, name, rating, inventory, orientation = None):
        self.name = name
        self.rating = rating
        self.inventory = inventory
        
def Buy(self):
    car = input("input a car that is not currently in the inventory")  
    
    #should add that car to that seller’s inventory
    
    inventory = inventory + car
    print("the new inventory has", car)
    
def Sell(self):
    car2 = input("input a car that is in the inventory")
    
    #remove it from the seller's inventory
    
    print("the new inventory does not have", car2)
    

    file.close()