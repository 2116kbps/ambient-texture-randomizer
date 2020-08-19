import os
import random

registers = ["Low","Mid","High"]
pad_types = ["swells","drones","3-5 Note melodies/arpeggios"]
intervals = ["dyads", "triads", "perfect 4ths", "perfect 5ths", "octaves"]
keys = ["A","C","D","E","G"]
modes = ["Minor", "Major"]
effects = ["Sub","Distortion","Clean", "Long Delay", "Short Delay", 
            ["Big Sky Room", "Big Sky Hall", "Big Sky Plate","Big Sky Spring", 
            "Big Sky Swell", "Big Sky Bloom", "Big Sky Cloud", "Big Sky Chorale", 
            "Big Sky Shimmer", "Big Sky Magneto", "Big Sky Nonlinear", "Big Sky Reflections"],
            ["Slo Dark", "Slo Rise", "Slo Dream"],
            ["Astronomer Short", "Astronomer Medium", "Astronomer Long"]]

class Atmosphere:

    def rand_index(self, lst):
        lst_len = len(lst) - 1
        return random.randint(0,lst_len)

    def get_random_item(self, lst):
        item = lst[self.rand_index(lst)]
        if type(item) == list:
            rand_elem = item[self.rand_index(item)]
            return rand_elem
        else:
            return item

    def __init__(self, interval, key, mode, register, pad_type, effect):
        self.interval = self.get_random_item(interval)
        self.key = self.get_random_item(key)
        self.mode = self.get_random_item(mode)
        self.register = self.get_random_item(register)
        self.pad_type = self.get_random_item(pad_type)
        self.effect = self.get_random_item(effect)
        self.concatenated = self.register + "-register " + self.pad_type + " focusing on " + \
            self.interval + " in " + self.key + " " + self.mode + " with " + self.effect + " effect"


# Recursively check txt file for pre-existing atmospheres
# (Big-O could possibly be improved by removing elements from list after maximum # of uses)

def check_file():
    new = Atmosphere(intervals, keys, modes, registers, pad_types, effects)
    cwd = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(cwd,"Already Used.txt")
    
    with open(filepath, 'r+') as au:
        for line in au:
            if line == new:
                check_file()
                break
        else:
            au.write(new.concatenated+'\n')
            print('\n' + new.concatenated + '\n')

check_file()
