import sys
import types

#strategy pattern implementation based off here: https://stackoverflow.com/questions/963965/how-to-write-strategy-pattern-in-python-differently-than-example-in-wikipedia

create_bound_method = types.MethodType

#creating the interface for implementing the strategy pattern for the makeNoise behavior
class MakeNoiseStrategy:
    def __init__(self, animalName, animalType, func = None):
        self.name = animalName
        self.type = animalType
        if func == None: #if no strategy is specified it defaults to the base implementation 
            self.makeNoise
        elif func:
            self.makeNoise = create_bound_method(func, self)

    @property #honestly not postive if the @property is correct but it solved an error and everything works properly
    def makeNoise(self):# default implementation
        print(self.name, "the", self.type, "makes whatever noise an animal makes.")

#all the different types of makeNoise strategies used
def dogNoise(self):
    print(self.name, "the", self.type, "barks like a dog.")

def wolfNoise(self):
    print(self.name, "the", self.type, "howls like a wolf.")

def catNoise(self):
    print(self.name, "the", self.type, "meows like a cat.")

def lionNoise(self):
    print(self.name, "the", self.type, "roars like a lion.")

def tigerNoise(self):
    print(self.name, "the", self.type, "growls like a tiger.")

def elephantNoise(self):
    print(self.name, "the", self.type, "blares like an elephant.")

def hippoNoise(self):
    print(self.name, "the", self.type, "yawns like a hippo.")

def rhinoNoise(self):
    print(self.name, "the", self.type, "grunts like a rhino.")