from scheduler.scheduler import Scheduler
import numpy as np

class Sjf(Scheduler):

    def __init__(self):
        Scheduler.__init__(self)
        self.process_queue = []

    # Colocar processo na lista de processos
    def put_process(self, process):
        self.process_queue.append(process)

    # Ordenar proessos de acordo com o menor tempo de execução
    def ordination(self):
        self.process_queue.sort()

    # Executar processo
    def execute_process(self, time):
        self.ordination()

        process = self.process_queue[0] # Recuperando primeiro processo da lista
        process.last_execution = time # Última vez que o processo foi executado

        process.time_left -= 1 # Atualiza o tempo restante do processo
        self.executed_order.append(process.name) # Coloca o nome na lista de executados
        if process.time_left == 0: # Caso o processo tenha terminado, retira-o da lista
            self.kill_process()

    def kill_process(self):
        del self.process_queue[0] 

    def calculate_awaiting_time(self, process_list):
        awaiting_time = []
        for process in process_list:
            process.awaiting_time = process.last_execution - process.arrival_time - (process.burst_time - 1) # Awaiting time de cada processo 
                                                                                        # (última execução - tempo de chegada - o quanto foi executado)
            awaiting_time.append(process.awaiting_time)

        awaiting_time = np.array(awaiting_time)
        total_awaiting_time = sum(awaiting_time)
        self.average_awaiting_time = total_awaiting_time / len(awaiting_time)  # Tempo médio de espera