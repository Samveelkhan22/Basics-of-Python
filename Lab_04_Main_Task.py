# import Environment 
# import Room 
# import VaccumAgent
# class TwoRoomVaccumCleanerEnvironment(Environment.Environment):
#     def __init__(self, agent):
#         self.r1 = Room.Room('A','dirty')
#         self.r2 = Room.Room('B','dirty')
#         self.r3 = Room.Room('C','dirty')
#         self.agent = agent
#         self.currentRoom = self.r1
#         self.delay = 1000 
#         self.step = 1
#         self.action = ""

#     def executeStep(self, n=1):
#         for _ in range(0,n):
#           self.displayPerception()
#           self.agent.sense(self) 
#           res = self.agent.act() 
#           self.action = res
#           if res == 'clean':
#             self.currentRoom.status = 'clean' 
#           elif res == 'right':
#             if self.currentRoom.location == 'A':
#               self.currentRoom = self.r2
#             elif self.currentRoom.location == 'B':
#               self.currentRoom = self.r3
#           elif res == 'left':
#             if self.currentRoom.location == 'B':
#               self.currentRoom = self.r1 
              
#             elif self.currentRoom.location == 'C':
#               self.currentRoom = self.r2
#           self.displayAction()
#           self.step += 1

# def executeAll(self):
#  raise NotImplementedError('action must be defined!') 

# def displayPerception(self):
#  print("Perception at step %d is [%s,%s]"%(self.step,self.currentRoom.status,self.currentRoom.location))

# def displayAction(self):
#  print("------- Action taken at step %d is [%s]" %(self.step,self.action))

# def delay(self,n=100):
#  self.delay = n

# if __name__ == '__main__': 
#  vcagent = VaccumAgent.VaccumAgent() 
#  env = TwoRoomVaccumCleanerEnvironment(vcagent)
#  env.executeStep(50)

#1
import random

class VacuumCleaner:
    def __init__(self):
        self.current_room = 1  # start in room 1
        self.cleaned_rooms = set()  # no rooms cleaned yet
    
    def get_current_room(self):
        return self.current_room
    
    def get_cleaned_rooms(self):
        return self.cleaned_rooms
    
    def clean_room(self):
        print(f"Cleaning room {self.current_room}...")
        self.cleaned_rooms.add(self.current_room)
    
    def move_to_room(self, room):
        if room < 1 or room > 3:
            print(f"Error: Invalid room {room}")
            return
        
        print(f"Moving to room {room}...")
        self.current_room = room
    
    def choose_action(self):
        if self.current_room not in self.cleaned_rooms:
            return "CLEAN"  # clean the current room if it's dirty
        
        # otherwise, randomly choose a neighboring room to move to
        next_room = random.choice([1, 2, 3])
        while next_room == self.current_room:
            next_room = random.choice([1, 2, 3])
        
        if next_room < self.current_room:
            return "LEFT"  # move to the room to the left
        elif next_room > self.current_room:
            return "RIGHT"  # move to the room to the right
    
    def run(self):
        print("Starting cleaning...")
        
        while len(self.cleaned_rooms) < 3:  # clean all three rooms
            action = self.choose_action()
            
            if action == "CLEAN":
                self.clean_room()
            elif action == "LEFT":
                self.move_to_room(self.current_room - 1)
            elif action == "RIGHT":
                self.move_to_room(self.current_room + 1)
            
            print(f"Current room: {self.current_room}")
            print(f"Cleaned rooms: {self.cleaned_rooms}")
        
        print("Cleaning finished!")
        
if __name__ == "__main__":
    vc = VacuumCleaner()  # create a new vacuum cleaner agent
    vc.run()  # run the cleaning process

#2
import random

class VacuumCleaner:
    def __init__(self, num_rooms):
        self.current_room = 1  # start in room 1
        self.cleaned_rooms = set()  # no rooms cleaned yet
        self.num_rooms = num_rooms
    
    def get_current_room(self):
        return self.current_room
    
    def get_cleaned_rooms(self):
        return self.cleaned_rooms
    
    def clean_room(self):
        print(f"Cleaning room {self.current_room}...")
        self.cleaned_rooms.add(self.current_room)
    
    def move_to_room(self, room):
        if room < 1 or room > self.num_rooms:
            print(f"Error: Invalid room {room}")
            return
        
        print(f"Moving to room {room}...")
        self.current_room = room
    
    def choose_action(self):
        if self.current_room not in self.cleaned_rooms:
            return "CLEAN"  # clean the current room if it's dirty
        
        # otherwise, randomly choose a neighboring room to move to
        next_room = random.choice(list(range(1, self.num_rooms+1)))
        while next_room == self.current_room:
            next_room = random.choice(list(range(1, self.num_rooms+1)))
        
        if next_room < self.current_room:
            return "LEFT"  # move to the room to the left
        elif next_room > self.current_room:
            return "RIGHT"  # move to the room to the right
    
    def run(self):
        print("Starting cleaning...")
        
        while len(self.cleaned_rooms) < self.num_rooms:  # clean all rooms
            action = self.choose_action()
            
            if action == "CLEAN":
                self.clean_room()
            elif action == "LEFT":
                self.move_to_room(self.current_room - 1)
            elif action == "RIGHT":
                self.move_to_room(self.current_room + 1)
            
            print(f"Current room: {self.current_room}")
            print(f"Cleaned rooms: {self.cleaned_rooms}")
        
        print("Cleaning finished!")
        
if __name__ == "__main__":
    num_rooms = 5  # set the number of rooms
    vc = VacuumCleaner(num_rooms)  # create a new vacuum cleaner agent
    vc.run()  # run the cleaning process

#3
import random

class VacuumCleaner:
    def __init__(self, num_rooms):
        self.current_room = 1  # start in room 1
        self.cleaned_rooms = set()  # no rooms cleaned yet
        self.num_rooms = num_rooms
        self.max_steps = num_rooms * 3  # maximum number of steps is 3 times the number of rooms
    
    def get_current_room(self):
        return self.current_room
    
    def get_cleaned_rooms(self):
        return self.cleaned_rooms
    
    def clean_room(self):
        print(f"Cleaning room {self.current_room}...")
        self.cleaned_rooms.add(self.current_room)
    
    def move_to_room(self, room):
        if room < 1 or room > self.num_rooms:
            print(f"Error: Invalid room {room}")
            return
        
        print(f"Moving to room {room}...")
        self.current_room = room
    
    def choose_action(self):
        if self.current_room not in self.cleaned_rooms:
            return "CLEAN"  # clean the current room if it's dirty
        
        # otherwise, randomly choose a neighboring room to move to
        next_room = random.choice(list(range(1, self.num_rooms+1)))
        while next_room == self.current_room:
            next_room = random.choice(list(range(1, self.num_rooms+1)))
        
        if next_room < self.current_room:
            return "LEFT"  # move to the room to the left
        elif next_room > self.current_room:
            return "RIGHT"  # move to the room to the right
    
    def run(self):
        print("Starting cleaning...")
        steps = 0
        
        while len(self.cleaned_rooms) < self.num_rooms and steps < self.max_steps:  # clean all rooms or until max steps reached
            action = self.choose_action()
            
            if action == "CLEAN":
                self.clean_room()
            elif action == "LEFT":
                self.move_to_room(self.current_room - 1)
            elif action == "RIGHT":
                self.move_to_room(self.current_room + 1)
            
            print(f"Current room: {self.current_room}")
            print(f"Cleaned rooms: {self.cleaned_rooms}")
            
            steps += 1
        
        print("Cleaning finished!")
        if steps >= self.max_steps:
            print(f"Stopped cleaning after {self.max_steps} steps.")
        
if __name__ == "__main__":
    num_rooms = 5  # set the number of rooms
    vc = VacuumCleaner(num_rooms)  # create a new vacuum cleaner agent
    vc.run()  # run the cleaning process

#4
import random
import time

class VacuumCleaner:
    def __init__(self, num_rooms):
        self.current_room = 1  # start in room 1
        self.cleaned_rooms = set()  # no rooms cleaned yet
        self.num_rooms = num_rooms
        self.max_steps = num_rooms * 3  # maximum number of steps is 3 times the number of rooms
        self.score = 0  # start with a score of 0
    
    def get_current_room(self):
        return self.current_room
    
    def get_cleaned_rooms(self):
        return self.cleaned_rooms
    
    def clean_room(self):
        print(f"Cleaning room {self.current_room}...")
        self.cleaned_rooms.add(self.current_room)
        self.score += 25
    
    def move_to_room(self, room):
        if room < 1 or room > self.num_rooms:
            print(f"Error: Invalid room {room}")
            return
        
        print(f"Moving to room {room}...")
        if room < self.current_room:
            self.score -= 1  # penalty for moving left
        self.current_room = room
    
    def choose_action(self):
        if self.current_room not in self.cleaned_rooms:
            self.score -= 10  # penalty for cleaning already clean room
            return "CLEAN"  # clean the current room if it's dirty
        
        # otherwise, randomly choose a neighboring room to move to
        next_room = random.choice(list(range(1, self.num_rooms+1)))
        while next_room == self.current_room:
            next_room = random.choice(list(range(1, self.num_rooms+1)))
        
        if next_room < self.current_room:
            return "LEFT"  # move to the room to the left
        elif next_room > self.current_room:
            return "RIGHT"  # move to the room to the right
    
    def calculate_score(self):
        dirty_rooms = set(range(1, self.num_rooms+1)) - self.cleaned_rooms
        self.score -= len(dirty_rooms) * 10
        print(f"Score: {self.score}")
    
    def run(self):
        print("Starting cleaning...")
        steps = 0
        
        while len(self.cleaned_rooms) < self.num_rooms and steps < self.max_steps:  # clean all rooms or until max steps reached
            action = self.choose_action()
            
            if action == "CLEAN":
                self.clean_room()
            elif action == "LEFT":
                self.move_to_room(self.current_room - 1)
            elif action == "RIGHT":
                self.move_to_room(self.current_room + 1)
            
            print(f"Current room: {self.current_room}")
            print(f"Cleaned rooms: {self.cleaned_rooms}")
            
            self.calculate_score()
            time.sleep(1)  # pause for 1 second
            
            steps += 1
        
        print("Cleaning finished!")
        if steps >= self.max_steps:
            print(f"Stopped cleaning after {self.max_steps} steps.")
        
if __name__ == "__main__":
    num_rooms = 5  # set the number of rooms
    vc = VacuumCleaner(num_rooms)  # create a new vacuum cleaner agent
    vc.run()  # run the cleaning process

#5
def choose_action(self):
    if self.current_room not in self.cleaned_rooms:
        return "CLEAN"  # clean the current room if it's dirty
    
    # otherwise, move to the nearest dirty room
    dirty_rooms = set(range(1, self.num_rooms+1)) - self.cleaned_rooms
    if not dirty_rooms:
        return None  # all rooms are clean
    
    nearest_room = min(dirty_rooms, key=lambda x: abs(x - self.current_room))
    if nearest_room < self.current_room:
        return "LEFT"  # move to the room to the left
    elif nearest_room > self.current_room:
        return "RIGHT"  # move to the room to the right

def run(self):
    print("Starting cleaning...")
    steps = 0
    
    while len(self.cleaned_rooms) < self.num_rooms:  # clean all rooms
        action = self.choose_action()
        
        if action == "CLEAN":
            self.clean_room()
        elif action == "LEFT":
            self.move_to_room(self.current_room - 1)
        elif action == "RIGHT":
            self.move_to_room(self.current_room + 1)
        
        self.calculate_score()
        time.sleep(1)  # pause for 1 second
        
        steps += 1
    
    print("Cleaning finished!")
