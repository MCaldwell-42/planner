import datetime

class Building:

    def __init__(self, address, stories):
        # Establish the properties of each book
        # with a default value
        self.designer = ""
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def __str__(self):
        return f"{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories."


    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, name):
        self.owner = name

smal_haus = Building("312 Chong Phuak", 1)
Nss = Building("301 Plus Park", 4)
my_house = Building("East Nasty", 2)
lighthouse = Building("Ocean Blvd", 12)
gods_house = Building("Heaven", 777)


smal_haus.purchase("MC Fly Jo")
Nss.purchase("Johnny Boy")
my_house.purchase("Greg")
lighthouse.purchase("Jolene")
gods_house.purchase("THE LORD ALMIGHTY")

smal_haus.construct()
Nss.construct()
my_house.construct()
lighthouse.construct()
gods_house.construct()

print(smal_haus)
print(Nss)
print(my_house)
print(lighthouse)
print(gods_house)