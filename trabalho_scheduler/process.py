import numpy as np

class Process():

    def __init__(self, name, arrival_time, burst_time):

        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.time_left = burst_time
        self.awaiting_time = np.inf

        self.first_execution = None
        self.last_execution = None

    def __repr__(self):
        return(f"{self.name} - time: {self.time_left}")

    def __lt__(self, other):
        return (self.time_left < other.time_left)