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