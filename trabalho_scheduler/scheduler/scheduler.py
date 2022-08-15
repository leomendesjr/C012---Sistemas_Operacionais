from queue import Queue
import numpy as np

class Scheduler():

    def __init__(self):
        self.executed_order = []
        self.average_awaiting_time = np.inf

    def execution_order(self):
        return(" | ".join(self.executed_order))
