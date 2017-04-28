
import pandas as pd

class Khaos:
    
    def __init__(self):
        self.actors = { }
        self.actor_map = { }  # map frame number to list of actors 
        self.dataframe = { }  

    # placeholder
    def calculate_khaos(self):
        return 0

    def create_actor_map(self, mapping):
        self.actor_map = mapping

    def get_actor_map(self):
        return self.actor_map

    def get_actors(self):
        return self.actors


