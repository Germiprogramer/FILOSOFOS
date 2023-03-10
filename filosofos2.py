import threading

from threading import BoundedSemaphore

#semaforos

a = BoundedSemaphore(1)
b = BoundedSemaphore(1)
c = BoundedSemaphore(1)
d = BoundedSemaphore(1)
e = BoundedSemaphore(1)

class Filosofo(threading.Thread):
    def __init__(self, tenedor, num):
        threading.Thread.__init__(self)
        self.tenedor = tenedor
        self.num = num
        self.temp = self.num + 1 % 5

    def come(self):
        print ("El filosofo "+str(self.num)+" come")

    def piensa(self):
        print ("El filosofo "+str(self.num)+" piensa")

    

