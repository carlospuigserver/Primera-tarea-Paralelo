from multiprocessing import Process
from multiprocessing import Pool
from time import sleep
import random
import time

#defino la funcion scrape
def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration


#programa secuencial
def sequencial():
    tiempoInicial = time.time()
    urls = ["a.com", "b.com", "c.com", "d.com"]
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    Tiempo=(time.time()-tiempoInicial, "segundos")
    print("El tiempo en secuencial es: ",Tiempo)


#programa multiprocesamiento
def multiprocesamiento():
    tiempo_inicial=time.time()
    urls = ["a.com", "b.com", "c.com", "d.com"]
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()
    Tiempo=(time.time()-tiempo_inicial,"segundos")
    print("El tiempo en multiprocesamiento es: ",Tiempo)

#ejecuto en paralelo ambos programas

if __name__ == '__main__':
    p1=Process(target=sequencial)
    p2=Process(target=multiprocesamiento)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

