import random
temperatura = []
for i in range(10):    
    temperatura_random = int(random.uniform(-10.0, 40.0))
    temperatura.append(temperatura_random)
for temp in temperatura:
    print("Las temperaturas generadas fueron:",f"{temp}°C")