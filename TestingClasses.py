import random as rd
import pandas as pd

chlorodf = pd.read_csv('funny.csv', index_col='name')
flowernames = chlorodf.index.tolist()

class plant():
    def __init__(self, name, age):
        self.name   = name
        self.age    = age
        self.health = 100 - self.age**2
        self.series = chlorodf.loc[name]
        self.thirst = self.series['thirst']
        mean = int(str(self.series['maxage']).split(':')[0])
        devi = int(str(self.series['maxage']).split(':')[1])
        self.maxage = rd.randint(mean - devi, mean + devi)
        self.price  = self.series['price']
        self.water = 50
    
    def __str__(self):
        return f"name : {self.name}\nage : {self.age}\nhealth : {self.health}\nthirst : {self.thirst}\nmaxage : {self.maxage}\nprice : {self.price}"
    
    def progress(self):
        self.age += 1
        self.health = 100 - self.age**2

Shelf = []

for i in range(10):
    name = rd.choice(flowernames)
    age = rd.randint(0, 10)
    Shelf.append(plant(name, age))

for i in Shelf:
    print(i)
    print()
