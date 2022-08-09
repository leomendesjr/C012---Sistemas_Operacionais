from threading import Thread
import multiprocessing
import time
from playsound import playsound

class Music(Thread):
    def __init__(self, path, start_delay, duration):
        '''
        Construtor

        Args:
            - path: caminho para o arquivo
            - start_delay: tempo (s) esperado para início do áudio
            - duration: duração do áudio
        '''
        Thread.__init__(self)
        # Tocar o áudio
        self.p = multiprocessing.Process(target=playsound, args=(path,))
        self.path = path
        self.start_delay = start_delay
        self.duration = duration

    def run(self):
        # Aguardar, tocar o áudio por start_delay segundos, parar o áudio
        print(f"Thread to play {self.path} created")
        time.sleep(self.start_delay)
        print(f"==== Playing: {self.path} ====")
        self.p.start()
        time.sleep(self.duration)
        print(f"==== Stoping: {self.path} ====")
        self.stop()

    def stop(self):
        self.p.terminate()
        
        
if __name__ == '__main__':

    music1 = Music("mus1.wav", 0, 20)
    music1.start()

    music2 = Music( "mus3.mp3", 10, 20)
    music2.start()