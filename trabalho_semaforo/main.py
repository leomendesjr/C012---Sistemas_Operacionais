import threading
import time

# Processador simulando a sessão crítica
def processador(nome, tempo):
    print(f"Processo {nome} aguardando")
    semaforo.acquire()
    print(f"Acessou {nome}")
    time.sleep(float(tempo))
    print(f"Finalizou {nome}")
    semaforo.release()

# Quantidade de núcleos do processador
nucleos = int(input("Quantos núcleos seu processador tem: "))
semaforo = threading.Semaphore(nucleos)

# Duração dos processos
processos_tempo = []
while True:
    tempo = input("Entre com a duração do processo: (-1 para sair)\n")
    if tempo == "-1":
        break
    processos_tempo.append(float(tempo))

# Criação dos processos
for i, t in enumerate(processos_tempo):
    threads = threading.Thread(target = processador, args=(i, t))
    threads.start()