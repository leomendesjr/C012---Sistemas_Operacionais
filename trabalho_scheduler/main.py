from process import Process
from scheduler.fcfs import Fcfs
from scheduler.sjf import Sjf

# Inicializando processos
p1 = Process(name = "p1", arrival_time = 0, burst_time =  8)
p2 = Process(name = "p2", arrival_time = 1, burst_time =  4)
p3 = Process(name = "p3", arrival_time = 2, burst_time =  9)
p4 = Process(name = "p4", arrival_time = 3, burst_time =  5)

processos = [p1, p2, p3, p4]

algoritmo = "sjf"

if algoritmo == "sjf":
    queue = Sjf()
elif algoritmo == "fcfs":
    queue = Fcfs()

inicio = True
time = 0

while inicio or (algoritmo == "sjf" and len(queue.process_queue) != 0) or (algoritmo == "fcfs" and queue.process_queue.empty() == False):
    inicio = False

    # Colocando na fila todos os processos que chegaram no tempo 'time'
    for p in processos:
        if p.arrival_time == time:
            queue.put_process(p)

    queue.execute_process(time)

    time += 1

# Calculando tempo de espera
queue.calculate_awaiting_time(processos)
# Casting de lista para string
queue.executed_order = queue.execution_order()

print(f"Ordem de execução dos processos\n{queue.executed_order}")
print(f"Tempo médio de espera na fila: {queue.average_awaiting_time} ms")