import random

#Each ant should have a number representing how long they've been alive, and a number represneting hunger. 
#Each ant should also have functions to move, eat, print information, and die. 
class Ants():
    def __init__(self):
        self.time_alive = 0
        self.hunger_level = 0.00
        self.position = (400,400)
        self.type
    def move():
        random = random.randrange(1,4)
        if random > 3:
            self.position[0] += 1
        elif random > 2:
            self.position[0] -= 1
        elif random > 1:
            self.position[1] += 1
        else:
            self.position[1] -= 1
    def eat():
        if self.hunger_level > 0:
            self.hunger_level -= 1
    def get_info():
        print("Class: ", self.type, ", Hunger: ", self.hunger, ", DaysInJob: ", self.time_alive, " Days, Position: ", )
        if self.hunger_level < 0:
                self.hunger_level = 0
        if hunger_level >= 10:
            del self
        

class Queen(Ants):
    self.type = "Queen"
    def pass_time():
        self.time_alive += 1
        random = random.randrange(1,4)
        self.hunger_level += .25
        #if random == 1:
class Worker(Ants):
    self.type = "Worker"
    def pass_time():
        self.hunger_level += .5
class Larva(Ants):
    self.type = "Larva"
    def pass_time():
        self.hunger_level =+ 1


colony = []
for i in range(5):
    w = Worker()
    colony.append(w)
    l = Larva()
    colony.append(l)

i = 0
while colony[0].type != "Queen":
    colony[i].pass_time()
    colony[i].move()
    colony[i].get_info()
    colony[i].eat()