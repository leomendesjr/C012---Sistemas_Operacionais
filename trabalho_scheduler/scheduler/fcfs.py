from scheduler.scheduler import Scheduler
from queue import Queue
import numpy as np

class Fcfs(Scheduler):

    def __init__(self):
        Scheduler.__init__(self)
        self.process_queue = Queue()

    # Colocar processo na lista de processos
    def put_process(self, process):
        self.process_queue.put(process)

    # Verifica se é a primeira execução do processo
    def verify_execution(self, process, time):
        if process.first_execution is None:
            process.first_execution = time

    # Executar o processo
    def execute_process(self, time):
        process = self.process_queue.queue[0] # Recuperando primeiro processo da lista

        self.verify_execution(process, time)  # verify if a process was already executed

        process.time_left -= 1                # Atualiza o tempo restante do processo
        self.executed_order.append(process.name)  # Coloca o nome na lista de executados
        if process.time_left == 0:            # Caso o processo tenha terminado, retira-o da lista
            self.kill_process()

    def kill_process(self):
        return self.process_queue.get() 

    def calculate_awaiting_time(self, process_list):
        awaiting_time = []
        for process in process_list:
            process.awaiting_time = process.first_execution - process.arrival_time # Awaiting time de cada processo (primeira execução - tempo de chegada)
            awaiting_time.append(process.awaiting_time)

        awaiting_time = np.array(awaiting_time)
        total_awaiting_time = sum(awaiting_time)
        self.average_awaiting_time = total_awaiting_time / len(awaiting_time) # Tempo médio de espera