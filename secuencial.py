import random
from time import sleep
import time

tiempoInicial = time.time()

urls = ["a.com", "b.com", "c.com", "d.com"]

def scrape(url):
    print("starting", url)
    duration = round(random.random(), 3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration

output = []
for url in urls:
    result = scrape(url)
    output.append(result)

Tiempo=(time.time()-tiempoInicial, "segundos")
print("El tiempo en secuencial es:  ",Tiempo)


