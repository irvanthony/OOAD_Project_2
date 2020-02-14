import abc #python's abstract class library
import sys #for writing to the output file
import RoamStrategy #interface for the roam behavior for the animals
import NoiseStrategy #interface for the makeNoise behavior for the animals

#for easier referencing and clarity declaring each of the different types of 'strategies' for the animals from the interfaces
canine_roam_strategy = RoamStrategy.canineRoam
feline_roam_strategy = RoamStrategy.felineRoam
pachyderm_roam_strategy = RoamStrategy.pachydermRoam

dog_noise_strategy = NoiseStrategy.dogNoise
wolf_noise_strategy = NoiseStrategy.wolfNoise
cat_noise_strategy = NoiseStrategy.catNoise
lion_noise_strategy = NoiseStrategy.lionNoise
tiger_noise_strategy = NoiseStrategy.tigerNoise
elephant_noise_strategy = NoiseStrategy.elephantNoise
hippo_noise_strategy = NoiseStrategy.hippoNoise
rhino_noise_strategy = NoiseStrategy.rhinoNoise

#top of the class hierarchy
class Animal():
    def __init__(self, name, roam_strategy = None, noise_strategy = None):
        self.name = name
        self.type = "Animal"
        self.roam_strategy = roam_strategy #for the roam strategy 
        self.noise_strategy = noise_strategy #for the makeNoise strategy

    def wakeUp(self):
        print(self.name, "the", self.type, "woke up.")

    def roam(self):
        #self.roam_strategy.roam()
        RoamStrategy.RoamStrategy(self.name, self.type, self.roam_strategy).roam() #calling the appropriate roam method based on the defined roam strategy

    def makeNoise(self):
        NoiseStrategy.MakeNoiseStrategy(self.name, self.type, self.noise_strategy).makeNoise() #calling the appropriate makeNoise method basedon the defined noise strategy

    def eat(self):
        print(self.name, "the", self.type, "ate their food")

    def sleep(self):
        print(self.name, "the", self.type, "went to sleep")

class Canine(Animal):
    def __init__(self, name):
        super(Canine, self).__init__(name, canine_roam_strategy, None) #roam strategy is determined at the middle level (canine, feline pachyderm)
        self.type = "Canine"

class Dog(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Dog"
        self.noise_strategy = dog_noise_strategy #noise strategy is determined at the bottom level (dog, cat, hippo, etc)

class Wolf(Canine):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Wolf"
        self.noise_strategy = wolf_noise_strategy

class Feline(Animal):
    def __init__(self, name):
        super(Feline, self).__init__(name, feline_roam_strategy)
        self.type = "Feline"

class Cat(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Cat"
        self.noise_strategy = cat_noise_strategy

class Lion(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Lion"
        self.noise_strategy = lion_noise_strategy

class Tiger(Feline):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Tiger"
        self.noise_strategy = tiger_noise_strategy

class Pachyderm(Animal):
    def __init__(self, name):
        super(Pachyderm, self).__init__(name, pachyderm_roam_strategy)
        self.type = "Pachyderm"

class Elephant(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Elephant"
        self.noise_strategy = elephant_noise_strategy

class Hippo(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Hippo"
        self.noise_strategy = hippo_noise_strategy

class Rhino(Pachyderm):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Rhino"
        self.noise_strategy = rhino_noise_strategy

#class for the zookeeper which is the 'observed' item in the observer pattern
class Zookeeper():
    def __init__(self, name):
        self.name = name
        self._observers = set()
        self._subject_state = None

    #https://sourcemaking.com/design_patterns/observer/python/1
    def attach(self, observer): # for adding observers/subcribers to the zookeeper
        observer.subject = self
        self._observers.add(observer)

    def detach(self, observer): # for removing observers/subscribers form the zookeeper
        observer.subject = None
        self._observers.discard(observer)

    def _notify(self): # function to notify the observer
        for observer in self._observers:
            observer.update(self._subject_state)

    @property #getting the state of the zookeeper ('ie the state of what is being observed')
    def subject_state(self):
        return self._subject_state

    @subject_state.setter #setting the state of the zookeeper which then notifies the observer of a change
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()

    def wakeUpAnimals(self, animals):
        self.subject_state = "wakeUp" #specfic message for the observer to let it know what behavior to execute
        print(self.name, "wakes up the animals.")
        for i in animals:
            i.wakeUp()

    def rollCall(self, animals):
        self.subject_state = "rollCall" #message for observer
        print(self.name, "roll calls the animals")
        for i in animals:
            i.makeNoise()

    def feedAnimals(self, animals):
        self.subject_state = "feed" #message for observer
        print(self.name, "feeds teh animals.")
        for i in animals:
            i.eat()

    def exerciseAnimals(self, animals):
        self.subject_state = "exercise" #message for observer
        print(self.name, "feeds the animals.")
        for i in animals:
            i.roam()

    def shutDownZoo(self, animals):
        self.subject_state = "shutDown" #message for observer
        print(self.name, "shuts down the zoo.")
        for i in animals:
            i.sleep()

        self._observers.clear()# removing all observers from the zookeeper once the last task for the day is done

#abstract class for the observer part of the observer pattern
#based on: https://sourcemaking.com/design_patterns/observer/python/1
class ZooAnnouncerAbstract(metaclass = abc.ABCMeta):
    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod
    def update(self, arg):
        pass

#concrete class for the observer
class ZooAnnouncer(ZooAnnouncerAbstract):
    def update(self, arg):
        self._observer_state = arg
        #the zoo anouncer (observer) prints different messages based on the state seen of the zookeeper
        if self._observer_state == "wakeUp":
            print("This is the zoo anouncer! The zookeeper is about to wake up the animals.")
        elif self._observer_state == "rollCall":
            print("This is the zoo anouncer! The zookeeper is about to roll call the animals.")
        elif self._observer_state == "feed":
            print("This is the zoo anouncer! The zookeeper is about to feed the animals.")
        elif self._observer_state == "exercise":
            print("This is the zoo anouncer! The zookeeper is about to exercise the animals.")
        elif self._observer_state == "shutDown":
            print("This is the zoo anouncer! The zookeeper is about to shut down the zoo.")
        

if __name__ == "__main__":
    # for the output stuff
    # https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python    
    orig_stdout = sys.stdout
    f = open('output.txt', 'w')
    sys.stdout = f

    zooAnimals = []

    za = ZooAnnouncer()
    zelda = Zookeeper("Zelda")
    zelda.attach(za)

    charlie = Cat("Charlie")
    zooAnimals.append(charlie)
    chloe = Cat("Chloe")
    zooAnimals.append(chloe)
    
    daniel = Dog("Daniel")
    zooAnimals.append(daniel)
    dorothy = Dog("Dorothy")
    zooAnimals.append(dorothy)
    
    ernie = Elephant("Ernie")
    zooAnimals.append(ernie)
    elizabeth = Elephant("Elizabeth")
    zooAnimals.append(elizabeth)

    harley = Hippo("Harley")
    zooAnimals.append(harley)
    herald = Hippo("Herald")
    zooAnimals.append(herald)

    larry = Lion("Larry")
    zooAnimals.append(larry)
    lisa = Lion("Lisa")
    zooAnimals.append(lisa)

    richie = Rhino("Richie")
    zooAnimals.append(richie)
    rachel = Rhino("Rachel")
    zooAnimals.append(rachel)

    tony = Tiger("Tony")
    zooAnimals.append(tony)
    trish = Tiger("Trish")
    zooAnimals.append(trish)

    william = Wolf("William")
    zooAnimals.append(william)
    wendy = Wolf("Wendy")
    zooAnimals.append(wendy)

    zelda.wakeUpAnimals(zooAnimals)
    zelda.rollCall(zooAnimals)
    zelda.feedAnimals(zooAnimals)
    zelda.exerciseAnimals(zooAnimals)
    zelda.shutDownZoo(zooAnimals)

    sys.stdout = orig_stdout
    f.close()