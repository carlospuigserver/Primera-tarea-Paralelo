from multiprocessing import Process
from multiprocessing import Pool
from time import sleep
import random
import time

# define la función scrape
def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

# programa secuencial
def run_sequential():
    tiempoInicial = time.time()
    urls = ["a.com", "b.com", "c.com", "d.com"]
    output = []
    for url in urls:
        result = scrape(url)
        output.append(result)
    Tiempo=(time.time()-tiempoInicial, "segundos")
    print("El tiempo en secuencial es: ",Tiempo)

# define la función para el programa en multiprocesamiento
def run_multiprocessing():
    tiempo_inicial=time.time()
    urls = ["a.com", "b.com", "c.com", "d.com"]
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()
    Tiempo=(time.time()-tiempo_inicial,"segundos")
    print("El tiempo en multiprocesamiento es: ",Tiempo)

# Ejecuta ambos programas en subprocesos separados
if __name__ == '__main__':
    p1 = Process(target=run_sequential)
    p2 = Process(target=run_multiprocessing)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
