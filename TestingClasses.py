import random as rd
import pandas as pd

chlorodf = pd.read_csv('funny.csv')
flowernames = chlorodf['name'].tolist()

class plant():
    def __init__(self, name, age):
        self.name   = name
        self.age    = age
        self.health = 100 - self.age**2
        self.series = chlorodf.loc[name]
        self.thirst = None
        self.maxage = None
        self.price  = None
    
    def __str__(self):
        return f'name : {self.name}/nage : {self.age}/nhealth : {self.health}/nthirst : {self.thirst}/nmaxage : {self.maxage}/nprice : {self.prive}'
    
    def progress(self):
        self.age += 1
        self.health = 100 - self.age**2

Shelf = []

p1 = plant('Rose', 1)
print(p1)
