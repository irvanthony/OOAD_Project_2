import sys
import types

#strategy pattern implementation based off here: https://stackoverflow.com/questions/963965/how-to-write-strategy-pattern-in-python-differently-than-example-in-wikipedia

create_bound_method = types.MethodType

#creating the interface for implementing the strategy pattern for the makeNoise behavior
class RoamStrategy:
    def __init__(self, animalName, animalType, func = None):
        self.name = animalName
        self.type = animalType
        if func == None: #if no strategy is specified it defaults to the base implementation
            self.roam
        elif func:
            self.roam = create_bound_method(func, self)

    @property #same as noise strategy, not sure if correct but solved error and everything works
    def roam(self):#base implementation
        print(self.name, "the", self.type, "moves however an animal does.")

#all the different roam strategies implemented
def canineRoam(self):
    print(self.name, "the", self.type, "runs around like a canine.")

def felineRoam(self):
    print(self.name, "the", self.type, "stalks around like a feline.")

def pachydermRoam(self):
    print(self.name, "the", self.type, "stomps around like a pachyderm.")
