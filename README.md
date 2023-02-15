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


Si la tarea es intensiva en recursos y necesita ser completada lo más rápido posible, entonces la ejecución en paralelo puede ser la mejor opción. Si la tarea no es crítica en tiempo y los recursos son limitados, la ejecución secuencial puede ser suficiente.


Por tanto vemos que justo en este caso, con solo 4 urls, si ejecutamos ambos programas sucesivas veces, nos damos cuenta de que en algunas ocasiones, es más rápida la programación secuencial, y en otras ocasiones lo es el multiprocesamiento, de esta manera vemos que para nuestros programas, la importtancia sobre como trabajarlo, teniendo en cuenta ambas maneras, no es tan importante o significativa.




