# Primera-tarea-Paralelo

El link de este repositorio es : https://github.com/carlospuigserver/Primera-tarea-Paralelo.git


# Programación secuencial

```

import random
from time import sleep

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

```
    
    
    
    
    
    
Este código ejecuta las solicitudes a cada URL secuencialmente, lo que significa que cada solicitud se espera a que se complete antes de pasar a la siguiente solicitud. En este caso, el código ejecuta la función scrape para cada URL en la lista urls en orden, y luego agrega el resultado a una lista llamada output.

La ventaja de este código es que es más simple y fácil de entender que el código de multiproceso. 





# Multiprocesamiento

```
from multiprocessing import Pool
from time import sleep
import random
def scrape(url):
    print("starting", url)
    duration = round(random.random(),3)
    sleep(duration)
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
urls = ["a.com", "b.com", "c.com", "d.com"]

if __name__ == "__main__":
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)


```





Este código utiliza la biblioteca multiprocessing para ejecutar la función scrape en paralelo en cuatro procesos diferentes. El código crea un grupo de procesos Pool con cuatro procesos y usa la función map para aplicar la función scrape a cada URL en la lista urls. 

La ventaja de este código es que ejecuta las solicitudes a cada URL en paralelo, lo que significa que puede ser más rápido que ejecutar cada solicitud secuencialmente.













# Programa en paralelo

```
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

```




En este programa, hemos importado Process de multiprocessing, de esta manera hemos podido convertir dos scrpits en dos subprocesos y ejecutarlos en un mismo script, y así comparar el tiempo de ambos, que era la finalidad del trabajo. 
Esto lo hemos hecho definiendo una función scrape común a ambos, hemos transformado cada programa en una función, y finalmente con Process, hemos sido capaces de imprimirlos a la vez.


# Conclusión:
De esta manera podemos concluir, que trabajando en multiprocesamiento, el trabajo es más rápido y más ágil que trabajando de manera secuencial.


